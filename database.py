import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os
from dotenv import load_dotenv

load_dotenv()

# local
#DATABASE_URL = "postgresql://postgres:postgres@localhost/kotol_db"
# docker
# DATABASE_URL = "postgresql://postgres:postgres@db/kotol_db"
# HEROKU

DATABASE_URL = "postgres://ctyrblrziomgze:5530c754683beb73f436c5a259dd92a70f97e4a08130f794e4f41169e8ed4146@ec2-54-155-46-64.eu-west-1.compute.amazonaws.com:5432/dkacujkg8ru5h"
engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
