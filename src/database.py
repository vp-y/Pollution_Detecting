from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os
Base = declarative_base()
db_url = os.getenv("DB_URL", "mysql+pymysql://user:pass@localhost/pollution_db")
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
class VehicleRecord(Base):
    __tablename__ = 'vehicle_records'
    id = Column(Integer, primary_key=True)
    plate = Column(String(20))
    confidence = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
def init_db():
    Base.metadata.create_all(engine)
def log_record(plate: str, conf: float):
    session = Session()
    rec = VehicleRecord(plate=plate, confidence=conf)
    session.add(rec)
    session.commit()
    session.close()