<!DOCTYPE html> 
<html lang="en">  

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
 
<body> 
  <h1>Clean Littered Road Classification</h1> 

  <p>This project aims to classify images of roads into two categories: <strong>Clean</strong> and <strong>Littered</strong>. The dataset used for this project is obtained from <a href="https://www.kaggle.com/datasets/faizalkarim/cleandirty-road-classification" target="_blank">Kaggle</a>.</p>

  <h2>📁 Directory Structure</h2>
    <pre>
    ├── src
    │   └── data_preparation.py     # Script to download, extract, and prepare the dataset
    ├── data
    │   └── cleandirty-road-classification  # Contains extracted images
    ├── artifacts                    # Folder for processed images
    ├── README.md                    # Project documentation (this file)
    └── requirements.txt             # List of required libraries
    </pre>

  <h2>📦 Dataset</h2>
    <ul>
        <li><strong>Source:</strong> <a href="https://www.kaggle.com/datasets/faizalkarim/cleandirty-road-classification" target="_blank">Clean/Dirty Road Classification</a></li>
        <li><strong>Data Format:</strong> Images of clean and littered roads.</li>
        <li><strong>Categories:</strong>
            <ul>
                <li><strong>Clean</strong> - Images of roads that are clean.</li>
                <li><strong>Littered</strong> - Images of roads that have litter or waste on them.</li>
            </ul>
        </li>
    </ul>

  <h2>📜 Prerequisites</h2>
    <p>To run this project, you need to have the following installed:</p>
    <ul>
        <li>Python 3.x</li>
        <li>Pip (Python package manager)</li>
        <li>Kaggle API (for downloading the dataset)</li>
    </ul>

  <h2>⚙️ Installation</h2>
    <p>Follow these steps to set up the project locally:</p>
    <pre>
    git clone https://github.com/your-repo-name.git
    cd Clean_Littered_Road_Classification
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    </pre>

  <h2>📥 Dataset Download</h2>
    <p>To download and extract the dataset, you will need a Kaggle account and an API key. Follow these steps:</p>
    <ol>
        <li>Go to <a href="https://www.kaggle.com/account" target="_blank">Kaggle Account</a> and create an API token.</li>
        <li>Place the 'kaggle.json' file in your system's <code>~/.kaggle/</code> directory (or <code>C:\Users\<username>\.kaggle\</code> on Windows).</li>
        <li>Run the following command to download and extract the dataset:</li>
    </ol>
    <pre>
    python src/data_preparation.py --username "your_kaggle_username" --key "your_kaggle_api_key"
    </pre>

  <h2>🚀 Usage</h2>
    <p>After downloading and extracting the dataset, you can prepare and classify the images by running the following command:</p>
    <pre>
    python src/data_preparation.py --username "your_kaggle_username" --key "your_kaggle_api_key"
    </pre>
    <p>This script will:</p>
    <ul>
        <li>Download and extract the dataset.</li>
        <li>Automatically detect image directories.</li>
        <li>Group images into <code>clean</code> and <code>dirty</code> folders under the <code>artifacts/</code> directory.</li>
    </ul>

  <h2>🔍 Troubleshooting</h2>
    <p>If you encounter issues like <strong>"No image files found"</strong>, try the following steps:</p>
    <ul>
        <li>Check if the dataset was extracted properly. The folder structure should look like <code>../data/cleandirty-road-classification/Images</code>.</li>
        <li>Ensure that image files exist in the directory. You can use a Python script to list all files in the directory.</li>
        <li>If subdirectories are created after extraction (like <code>../data/cleandirty-road-classification/cleandirty-road-classification/Images</code>), update the path accordingly in the script.</li>
    </ul>

  <h2>🤖 Scripts</h2>
    <ul>
        <li><strong>data_preparation.py</strong>: Downloads, extracts, and organizes the dataset.</li>
    </ul>

  <h2>📂 Artifacts</h2>
    <p>After running the script, images will be organized in the following structure:</p>
    <pre>
    └── artifacts
        ├── clean_files   # Images of clean roads
        └── dirty_files   # Images of littered roads
    </pre>
    
  <h2>🌟 Features</h2>
    <ul>
        <li>Automated dataset download and extraction.</li>
        <li>Dynamic image classification into clean and littered categories.</li>
        <li>Handles nested directory structures automatically.</li>
    </ul>

  <h2>📋 To Do</h2>
    <ul>
        <li>Build a machine learning model to classify the road images.</li>
        <li>Visualize the dataset and image distributions.</li>
        <li>Improve logging and error handling in scripts.</li>
    </ul>

  <h2>🙌 Contributing</h2>
    <p>Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes.</p>

  <h2>📄 License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>

  <h2>🤝 Contact</h2>
    <p>For any questions, feel free to reach out at <a href="shivangithakur7300@gmail.com">shivangithakur7300@gmail.com</a>.</p>
</body>

</html>





