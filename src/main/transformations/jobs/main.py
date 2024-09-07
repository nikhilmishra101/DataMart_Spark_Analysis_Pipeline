import sys
import os

# Add the project root to the sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
sys.path.append(project_root)
from resources.dev import config
from src.main.utility.encrypt_decrypt import decrypt
from src.main.utility.s3_client_object import S3ClientProvider
from src.main.utility.logging_config import logger

aws_access_key = config.aws_access_key
aws_secret_key = config.aws_secret_key

s3_client_provider = S3ClientProvider(decrypt(aws_access_key), decrypt(aws_secret_key))
s3_client = s3_client_provider.get_client()

response = s3_client.list_buckets()
logger.info(f"List of Buckets : {response["Buckets"]}")
