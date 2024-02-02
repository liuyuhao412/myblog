import os


def load_config():
    env = os.environ.get('FLASK_ENV', 'default')
    if env == 'production':
        from .production import ProductionConfig
        return ProductionConfig
    elif env == 'testing':
        from .testing import TestingConfig
        return TestingConfig
    else:
        from .default import Config
        return Config
