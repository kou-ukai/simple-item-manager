class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DATABASE_URI = 'postgresql://simple:password@db/simple'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://simple:password@db/simple'
