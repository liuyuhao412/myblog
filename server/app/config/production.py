from .default import Config


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'superSecretKeyForProduction'
