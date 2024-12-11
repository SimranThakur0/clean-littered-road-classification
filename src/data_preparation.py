import os
import glob
import shutil
import logging
import argparse
import zipfile
from dotenv import load_dotenv
from typing import Optional


# Load environment variables from .env file
load_dotenv()

class DatasetDownloader:
    def __init__(self, 
                 username: Optional[str] = None, 
                 api_key: Optional[str] = None,
                 log_level: int = logging.INFO):
        """
        Initialize the DatasetDownloader with Kaggle credentials and logging.
        """

        # Configure logging
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(self.__class__.__name__)

        # Retrieve credentials from environment variables
        self.username = username or os.getenv('KAGGLE_USERNAME')
        self.api_key = api_key or os.getenv('KAGGLE_KEY')

        # Validate credentials
        if not (self.username and self.api_key):
            self.logger.error("Kaggle credentials not found in .env file")
            raise ValueError("Kaggle credentials are required. Please check your .env file.")

    def download_dataset(self, 
                         dataset_name: str, 
                         download_path: str = "../data"):
        """
        Download a specific Kaggle dataset.
        
        Args:
            dataset_name (str): Kaggle dataset identifier
            download_path (str): Path to download the dataset
        
        Returns:
            str: Path to the downloaded and extracted dataset
        """
        try:
            # Set environment variables
            os.environ['KAGGLE_USERNAME'] = self.username
            os.environ['KAGGLE_KEY'] = self.api_key

            # Import Kaggle API
            from kaggle.api.kaggle_api_extended import KaggleApi

            # Ensure download directory exists
            os.makedirs(download_path, exist_ok=True)

            # Authenticate and download
            api = KaggleApi()
            api.authenticate()
            
            self.logger.info(f"Downloading dataset: {dataset_name}")
            api.dataset_download_files(dataset_name, path=download_path)

            # Find the downloaded zip file
            zip_files = glob.glob(os.path.join(download_path, '*.zip'))
            if not zip_files:
                raise FileNotFoundError("No zip file found after download")

            # Extract the first zip file found
            zip_path = zip_files[0]
            self.logger.info(f"Extracting {zip_path}")
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(download_path)

            self.logger.info("Dataset downloaded and extracted successfully")
            return download_path

        except Exception as e:
            self.logger.error(f"Error downloading dataset: {e}")
            raise

    def group_images(self, path: str):
        """
        Organize images into class-specific directories.
        
        Args:
            path (str): Directory containing images to organize
        """
        try:
            # Create class directories
            class_dirs = ['dirty', 'clean']
            for class_dir in class_dirs:
                os.makedirs(os.path.join(path, class_dir), exist_ok=True)

            # Find and move images
            image_paths = glob.glob(os.path.join(path, '*.jpg'))
            self.logger.info(f"Found {len(image_paths)} images to organize")

            for image in image_paths:
                try:
                    # Extract class from filename
                    image_filename = os.path.basename(image)
                    image_class = image_filename.split('_')[0]

                    # Validate class
                    if image_class not in class_dirs:
                        self.logger.warning(f"Skipping {image_filename}: Unknown class {image_class}")
                        continue

                    # Move image
                    destination = os.path.join(path, image_class, image_filename)
                    shutil.move(image, destination)
                    self.logger.debug(f"Moved {image_filename} to {image_class} directory")

                except Exception as e:
                    self.logger.error(f"Error processing {image}: {e}")

            self.logger.info("Image organization complete")

        except Exception as e:
            self.logger.error(f"Error organizing images: {e}")
            raise

def main():
    # Specific Kaggle dataset path
    dataset_name = 'faizalkarim/cleandirty-road-classification'
    download_path = '../data'

    try:
        # Initialize DatasetDownloader
        downloader = DatasetDownloader()

        # Download dataset
        downloaded_path = downloader.download_dataset(
            dataset_name=dataset_name,
            download_path=download_path
        )

        # Organize images (adjust path as needed)
        images_path = os.path.join(downloaded_path, 'Images', 'Images')
        downloader.group_images(images_path)

    except Exception as e:
        logging.error(f"Operation failed: {e}")
        exit(1)

if __name__ == '__main__':
    main()
    

