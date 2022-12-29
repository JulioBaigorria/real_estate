from pydantic import BaseSettings, validator, constr
from typing import Any
import yaml
from project.config.models import MONGO, MYSQL, REDIS
from functools import lru_cache
from project.utils import key_formatter


##############################################################
# Custom Load config.file ####################################
##############################################################
def yaml_config_settings_source(settings: BaseSettings) -> dict[str, Any]:
    with open('config.yml') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


class YamlBaseSettings(BaseSettings):
    class Config:
        extra = 'ignore'

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings, ):
            return init_settings, yaml_config_settings_source, env_settings, file_secret_settings


##############################################################
# APP Settings Model #########################################
##############################################################
class Settings(YamlBaseSettings):
    APP_NAME: constr(strip_whitespace=True, to_upper=True) = "real_estate"
    TEST: str = False
    LOCAL: bool
    DEBUG: bool = True
    ENVIRONMENT: str

    MYSQL: MYSQL
    # MONGO: MONGO
    # REDIS: REDIS

    @validator('APP_NAME', always=True)
    def url_generator(cls, v):
        return key_formatter(v)


@lru_cache()
def get_settings():
    return Settings()
