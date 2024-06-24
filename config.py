import os

class Config:
    SERVICE_DISCOVERY_URL = os.getenv('SERVICE_DISCOVERY_URL', 'http://localhost:5005')
