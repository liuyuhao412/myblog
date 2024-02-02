from .default import Config


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'testSecretKey'
