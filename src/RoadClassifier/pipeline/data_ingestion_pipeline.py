from RoadClassifier.components.data_ingestion import DataIngestion
from RoadClassifier.config.configuration import ConfigurationManager
from RoadClassifier import logger

logger.info(f"Data ingestion stage started")

config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(config = data_ingestion_config)

data_ingestion.download_file()
data_ingestion.unzip_and_clean()

logger.info(f"Data ingestion stage completed")

