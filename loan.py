from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Loan(Base):
    __tablename__ = 'loan'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)

    borrowed_books = relationship("BorrowedBook", back_populates="student", foreign_keys="[BorrowedBook.loan_id]") 
    def __init__(self,name,age,email,phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'
    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey('loan.id'))
    book_id = Column(Integer, ForeignKey('addbook.id'))

    # student_id = Column(Integer, ForeignKey('loan.id'))
    # book_id = Column(Integer, ForeignKey('addbook.id'))

    student = relationship("Loan", back_populates="borrowed_books", foreign_keys=[loan_id])  
    book = relationship("Addbook", back_populates="borrowed_books")

    def __init__(self, loan_id, book_id):
        self.loan_id = loan_id
        self.book_id = book_id