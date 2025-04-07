import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']
    ASYNCHRONOUS = True  # Enable asynchronous support if needed
    # Add other configuration variables as needed