from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sql_database = 'sqlite:///./blog.db'

engine = create_engine(sql_database,connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoFlush=False)
Base= declarative_base()


# to setup dtabaase connection 
#1 setup the engine
#2 create a base class that is mapping
#3 create a sessionmaker