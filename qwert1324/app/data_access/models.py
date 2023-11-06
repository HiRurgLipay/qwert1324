from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, JSON


Base = declarative_base()

class FormData(Base):
    __tablename__ = 'form_data'

    id = Column(Integer, primary_key=True)
    data = Column(JSON)

    def save(self):
        from qwert1324.app import Session
        session = Session()
        session.add(self)
        session.commit()
        session.close()
