from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
import psycopg2
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import session_user
from model import Base, File, Station, Recorder, Antenna, Dome

def db_session(header):
    engine = create_engine('postgresql+psycopg2://gluk:iwt@10.10.0.170:5432/gpsdb', echo = True) #Соединение с базой данных
    Session = sessionmaker(bind = engine) #Создание класса сессии
    session = Session()
    add_data(header, session)

def add_data(header,session):
    for every in header:
        print(every)
        file = File(every['filename'],
                    #every['DATE'],every['CRINEX VERS'], every['CRINEX PROG'], 
                    every['MARKER NAME'], every['MARKER NUMBER'], every['OBSERVER'], every['AGENCY'], every['REC'], every['REC # / TYPE'], 
                    every['REC # / TYPE / VERS'], every['ANT'], every['ANT # / TYPE'], every['DOME'], every['X'], 
                    every['Y'], every['Z'], every['H'], every['E'], every['N'],every['INTERVAL'], every['TIME OF FIRST OBS'])
        session.add(file)
        session.commit()













