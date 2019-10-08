"""
	NQueens Model
	@author: Andrés Hernández
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URI = 'postgres+psycopg2://user:pass@db:5432/solutions'

Base = declarative_base()
engine = create_engine(DATABASE_URI, echo=True)

def create_session():
	Session = sessionmaker(bind=engine)
	return Session()

def create_db():
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)

def delete_db():
	Base.metadata.drop_all(engine)


class Solution(Base):
    __tablename__ = 'solutions'
    id = Column(Integer, primary_key=True)
    nqueen = Column(Integer)
    solution = Column(String)

    def __str__(self):
    	return "<ID: {}, NQueen: {}, Solution: {}>".format(self.id,self.nqueen,self.solution)