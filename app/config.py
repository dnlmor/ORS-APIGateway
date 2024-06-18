class Config:
    SECRET_KEY = 'your_secret_key'
    JWT_SECRET_KEY = 'your_jwt_secret_key'

    # Microservices URLs
    USER_SERVICE_URL = 'http://localhost:5001/graphql'
    MENU_SERVICE_URL = 'http://localhost:5002/graphql'
    ORDER_SERVICE_URL = 'http://localhost:5003/graphql'
    PAYMENT_SERVICE_URL = 'http://localhost:5004/graphql'
    NOTIFICATION_SERVICE_URL = 'http://localhost:5005/graphql'
    SERVICE_DISCOVERY_URL = 'http://localhost:5006/graphql'
