import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Date
from sqlalchemy import Boolean
from sqlalchemy import Text
from sqlalchemy import JSON
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import SmallInteger
from sqlalchemy import Sequence
from sqlalchemy.orm import relationship

Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, Sequence('client_aid_seq', start=1, increment=1), primary_key=True, autoincrement=True)
    dni = Column(Integer, primary_key=True, index=True, unique=True)
    type = Column(String(15), nullable=False)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    tel = Column(String(30), nullable=False)
    address = Column(JSON, nullable=True)
    comment = Column(String(200), nullable=True)
    CREATED_AT = Column(DateTime, default=datetime.datetime.utcnow)
    UPDATED_AT = Column(DateTime, default=None, onupdate=datetime.datetime.utcnow)
    DELETED_AT = Column(DateTime, default=None)


class Estate(Base):
    __tablename__ = 'estates'

    id = Column(Integer, Sequence('estate_aid_seq', start=1, increment=1), primary_key=True, autoincrement=True)
    type = Column(String(15), nullable=True)
    id_client = Column(Integer, ForeignKey('clients.id'), nullable=True)
    address = Column(JSON, nullable=True)
    properties = Column(JSON, nullable=True)
    comment = Column(String(200), nullable=True)
    CREATED_AT = Column(DateTime, default=datetime.datetime.utcnow)
    UPDATED_AT = Column(DateTime, default=None, onupdate=datetime.datetime.utcnow)
    DELETED_AT = Column(DateTime, default=None)


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, Sequence('contract_aid_seq', start=1, increment=1), primary_key=True, autoincrement=True)
    start_contract_date = Column(Date, nullable=True)
    end_contract_date = Column(Date, nullable=True)
    id_estate = Column(Integer, ForeignKey('estates.id'), nullable=True)
    id_client = Column(Integer, ForeignKey('clients.id'), nullable=True)
    rental_value = Column(Float, nullable=True)
    water = Column(Float, nullable=True)
    gas = Column(Float, nullable=True)
    insurance = Column(Float, nullable=True)
    garage = Column(Float, nullable=True)
    tgi = Column(Float, nullable=True)
    expenses = Column(Float, nullable=True)
    comment = Column(String(200), nullable=True)
    CREATED_AT = Column(DateTime, default=datetime.datetime.utcnow)
    UPDATED_AT = Column(DateTime, default=None, onupdate=datetime.datetime.utcnow)
    DELETED_AT = Column(DateTime, default=None)
