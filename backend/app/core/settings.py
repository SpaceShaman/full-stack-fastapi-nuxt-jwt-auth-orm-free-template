from os import getenv

DB_URL = getenv("DB_URL", "sqlite:///db.sqlite")
SECRET_KEY = getenv("SECRET_KEY", "secret")
DEBUG = getenv("DEBUG", "False").lower() == "true"
SMTP_HOST = getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(getenv("SMTP_PORT", 465))
SMTP_USER = getenv("SMTP_USER", "")
SMTP_PASSWORD = getenv("SMTP_PASSWORD", "")
BASE_URL = getenv("BASE_URL", "http://localhost:3000")
