import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv("email")
telethon = os.getenv("telethon")
new_telethon = os.getenv("new_telethon")
password = os.getenv("password")
personal_account = os.getenv("personal_account")