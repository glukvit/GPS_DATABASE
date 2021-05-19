from sqlalchemy import Column, Integer, String,Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

#Здесь объявляем таблицы в виде декларатативного объявления для sqlalchemy

Base = declarative_base()


class File(Base):
    __tablename__ = 'File'
    file_id = Column(Integer,unique=True, autoincrement=True, primary_key=True)
    file_name = Column(String(128), unique=True, primary_key=True)
    marker_name = Column(String(128))
    marker_number = Column(String(128), nullable=True)
    observer = Column(String(128))
    agency = Column(String(128))
    rec = Column(String(128))
    rec_type = Column(String(128))
    rec_vers = Column(String(128))
    ant = Column(String(128))
    ant_type = Column(String(128))
    dome = Column(String(128),nullable=True)
    x = Column(Float) #Необязательное
    y = Column(Float) #Необязательное
    z = Column(Float) #Необязательное
    h = Column(Float) #Необязательное
    e = Column(Float) #Необязательное
    n = Column(Float) #Необязательное
    interval = (Integer)
    time_first_obs = (DateTime)

    def __init__(self, file_name, marker_name, marker_number, observer, agency, rec, rec_type,
                rec_vers,ant, ant_type, dome, x, y, z, h, e,n,interval,time_first_obs):
        self.file_name = file_name 
        self.marker_name = marker_name
        self.marker_number = marker_number
        self.observer = observer
        self.ant_type = agency
        self.rec = rec
        self.rec_type = rec_type
        self.rec_vers = rec_vers
        self.ant = ant
        self.ant_type = ant_type
        self.dome = dome
        self.x = x
        self.y = y
        self.z = z
        self.h = h
        self.e = e
        self.n = n
        self.interval = interval
        self.time_first_obs = time_first_obs


















class Station(Base):
    __tablename__ = 'Station'
    station_id = Column(Integer,unique=True, autoincrement=True,primary_key=True)
    site = Column(String, ForeignKey(File.marker_name))

    def __init__(self, station_id, site):
        #self.station_id = station_id
        self.site = site


class Recorder(Base):
    __tablename__ = 'Recorder'
    recorder_id = Column(Integer,unique=True, autoincrement=True,primary_key=True)
    rec = Column(String(128), ForeignKey(File.rec))
    rec_type = Column(String(128),ForeignKey(File.rec_type))
    rec_vers = Column(String(128), ForeignKey(File.rec_vers))

    def __init__(self, rec, rec_type, rec_vers):
        self.rec = rec
        self.rec_type = rec_type
        self.rec_vers = rec_vers


class Antenna(Base):
    __tablename__ = 'Antenna'
    antenna_id = Column(Integer, unique=True, autoincrement=True,primary_key=True)
    ant = Column(String(128),ForeignKey(File.ant))
    ant_type = Column(String(128),ForeignKey(File.ant_type))

    def __init__(self, ant, ant_type):
        self.ant = ant
        self.ant_type = ant_type


class Dome(Base):
    __tablename__ = 'Dome'
    dome_id = Column(Integer,unique=True, autoincrement=True,primary_key=True)
    dome_type = Column(String(128),ForeignKey(File.dome))

    def __init__(self, dome_type):
        self.dome_type = dome_type


    



