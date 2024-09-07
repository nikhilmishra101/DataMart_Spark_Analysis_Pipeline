import os
from src.main.utility.encrypt_decrypt import encrypt, decrypt
from dotenv import load_dotenv

load_dotenv()

aws_encrypted_access_key = encrypt(os.getenv("aws_access_key"))
aws_encrypted_access_key_secret = encrypt(os.getenv("aws_secret_key"))
print(f"output = {aws_encrypted_access_key}")
