from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()


MONGODB_URL = os.getenv("MONGODB_URL")
AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""
REGION_NAME = ""

