import os
from dataclasses import dataclass


def get_flask_env_conf():
    env = os.getenv(key='FLASK_CONFIG', default='production')
    prefix = 'conf.flask_conf.'
    class_name = None

    if env == 'production':
        class_name = 'ProductionConfig'
    elif env == 'development':
        class_name = 'DevelopmentConfig'
    elif env == 'test':
        class_name = 'TestingConfig'

    return prefix + class_name


@dataclass(frozen=True)
class BaseConfig(object):
    JSON_AS_ASCII = False
    MAX_CONTENT_LENGTH = 100 * (1024 ** 1)


@dataclass(frozen=True)
class DevelopmentConfig(BaseConfig):

    # Flask
    DEBUG = True
    TESTING = False


@dataclass(frozen=True)
class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


@dataclass(frozen=True)
class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
