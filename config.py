import os


# Flask app configuration
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your-secret-key"
    JSON_FILE_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data", "data.json"
    )
