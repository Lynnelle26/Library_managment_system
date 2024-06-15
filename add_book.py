from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from database import Base
from database import session

class Addbook(Base):
    __tablename__ = 'addbook'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    publisher = Column(String(250), nullable=False)
    year = Column(String(250), nullable=False)

    borrowed_books = relationship("BorrowedBook", back_populates="book")

    def __init__(self, name, author, publisher, year):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
        session.add(self)
        session.commit()
    
    @staticmethod
    def get_book_by_id(id):
        return session.query(Addbook).filter_by(id=id).first()
    
    @staticmethod
    def delete_book(book_id):
        book = session.query(Addbook).filter_by(id=book_id).first()
        session.delete(book)
        session.commit()
        return True
