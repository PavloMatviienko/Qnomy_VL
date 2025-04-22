import os
from dotenv import load_dotenv


load_dotenv()

VL_URL = os.getenv("VL_URL")
PERSONAL_ID = os.getenv("PERSONAL_ID")
BIRTH_DATE = os.getenv("BIRTH_DATE")
PERSONAL_ID_WRONG = os.getenv("PERSONAL_ID_WRONG")
BIRTH_DATE_WRONG = os.getenv("BIRTH_DATE_WRONG")
