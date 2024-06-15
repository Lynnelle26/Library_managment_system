from sqlalchemy import Column,Integer,String
from database import Base

class Deletebook(Base):
    __tablename__ = 'deletebook'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    publisher = Column(String(250), nullable=False)
    year = Column(String(250), nullable=False)

    def __init__(self, name, author, publisher, year):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
        