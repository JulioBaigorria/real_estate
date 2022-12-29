from pydantic import BaseModel, validator


##############################################################
#  Standard Services Config  #################################
##############################################################
class MYSQL(BaseModel):
    NAME: str
    USER: str
    PASS: str
    HOST: str = 'mysql'
    PORT: int = 3306

    CONN_URL: str = "{user}:{password}@{host}:{port}/{dbname}"

    @validator('CONN_URL', always=True)
    def url_generator(cls, v, values, **kwargs):
        return v.format(
            user=values['USER'],
            password=values['PASS'],
            host=values['HOST'],
            port=values['PORT'],
            dbname=values['NAME'],
        )


class MONGO(BaseModel):
    NAME: str
    USER: str
    PASS: str
    HOST: str = 'mongodb'
    PORT: int = 27017

    CONN_URL: str = "mongodb://{user}:{password}@{host}:{port}"

    @validator('CONN_URL', always=True)
    def url_generator(cls, v, values, **kwargs):
        return v.format(
            user=values['USER'],
            password=values['PASS'],
            host=values['HOST'],
            port=values['PORT'],
        )


class REDIS(BaseModel):
    HOST: str = 'redis'
    PORT: int = 6379
