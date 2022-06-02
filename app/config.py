class LocalConfig:
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:jude123@localhost/book'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '67ad41191a14125b92a988d6f1a8112a8b9f20a4'
    APP_NAME = 'MY BOOK SHOP'
