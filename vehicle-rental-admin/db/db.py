import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("sqlite:///data.sqlite")
connection = engine.connect()
metadata = db.MetaData

Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()