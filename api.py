import requests
import jenkins
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

def connectToJenkins(url, username, password):
    server = jenkins.Jenkins(url,
    username=username, password=password)
    return server

def initializeDb():
    engine = create_engine('sqlite:///storage.db', echo=False)
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)
    return session
