import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os
from dotenv import load_dotenv

load_dotenv()

# local
# DATABASE_URL = "postgresql://postgres:postgres@localhost/kotol_db"
# docker
# DATABASE_URL = "postgresql://postgres:postgres@db/kotol_db"
# HEROKU

DATABASE_URL = "postgresql://kextbizpyqxtjw:2b9ac6403b8e65b032187b44a9d68e5ef546e5f1e0a6718315eb1e53c3138907@ec2-52-215-68-14.eu-west-1.compute.amazonaws.com:5432/d3vhnkodcdf04h"
engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
