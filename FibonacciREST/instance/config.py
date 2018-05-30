import os

class EnvConfig(object):
    """Parent config class"""
    ENV = 'development'
    DEBUG = True
    CSRF_ENABLED = True
    SECRET = 'ThisIsMySecretKey'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:P1assword@localhost/FibRest_db'

class DevEnvConfig(EnvConfig):
    """ Dev Env config"""
    ENV = 'development'
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/FibRest_db'

class TestEnvConfig(EnvConfig):
    """Non local testing config"""
    ENV = 'development'
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/FibRest_db'
    DEBUG = True

class StagingEnvConfig(EnvConfig):
    """Staging config"""
    ENV = 'staging'
    DEBUG = True

class ProductionEnvConfig(EnvConfig):
    """Production config"""
    ENV = 'production'
    DEBUG = False
    TESTING = False

app_config = {
    'development' : DevEnvConfig,
    'testing' : TestEnvConfig,
    'staging' : StagingEnvConfig,
    'production' : ProductionEnvConfig,
}
