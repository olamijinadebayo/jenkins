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

def addJob(session, jlist):
    for j in jlist:
        session.add(j)
    session.commit()

def getLastJobId(session, name):
    job = session.query(Jobs).filter_by(name=name).order_by(Jobs.jen_id.desc()).first()
    if (job != None):
        return job.jen_id
    else:
        return None

class Jobs(Base):
    __tablename__ = 'Jobs'

    id = Column(Integer, primary_key = True)
    jen_id = Column(Integer)
    name = Column(String)
    timeStamp = Column(DateTime)
    result = Column(String)
    building = Column(String)
    estimatedDuration = Column(String)
