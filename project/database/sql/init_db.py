from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project.config import get_settings

config = get_settings()

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://" + config.MYSQL.CONN_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
