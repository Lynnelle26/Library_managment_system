from database import session, Base, engine
from add_book import Addbook
from loan import Loan, BorrowedBook

def main():
    print("Welcome to the Library Managment System")
    print("1. Add a book")
    print("2. Search for a book")
    print("3. List all books")
    print("4. Loaned book")
    print("5. Delete a book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        search_book()
    elif choice == 3:
        list_books()
    elif choice == 4:
        list_borrowed_books_by_student()
    elif choice == 5:        
        delete_book()
    elif choice == 6:
        exit()
    else:
        print("Invalid choice")
        main()

Base.metadata.create_all(engine)
def add_book():
    name = input("Enter the name of the book: ")
    author = input("Enter the author of the book: ")
    publisher = input("Enter the publisher of the book: ")
    year = input("Enter the year of publication: ")
    book = Addbook(name, author, publisher, year)
    session.add(book)
    session.commit()

def list_books():
    books = session.query(Addbook).all()
    if books:
        print("List of available books:")
        for book in books:
            print(f"ID: {book.id}, Name: {book.name}, Author: {book.author}, Publisher: {book.publisher}, Year: {book.year}")
    else:
        print("No books available in the library.")    

def delete_book():
    book_id = input("Enter the ID of the book to delete: ")
    book = session.query(Addbook).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print("Book deleted successfully!")
    else:
        print("Book not found.")


def list_borrowed_books_by_student():
    student_name = input("Enter the student's name: ")
    student_age = input("Enter student's age: ")
    student_email = input("Enter student's email: ")
    student_phone = input("Enter student's phone number: ")
    book_name = input("Enter the name of the book to borrow: ")

    # Create a new student record without checking if it exists
    new_student = Loan(name=student_name, age=student_age, email=student_email, phone=student_phone)
    session.add(new_student)
    session.commit()
    print(f"New student '{student_name}' added to the database.")

    # Now proceed to borrow the book
    book = session.query(Addbook).filter_by(name=book_name).first()
    if book:
        borrowed_book = BorrowedBook(loan_id=new_student.id, book_id=book.id)
        session.add(borrowed_book)
        session.commit()
        print(f"Book '{book.name}' borrowed by {new_student.name}")
    else:
        print(f"Book '{book_name}' not found.")  


def search_book():
    book_name = input("Enter the name of the book to search: ")
    book = session.query(Addbook).filter_by(name=book_name).first()
    if book:
        print(f"Book found - Name: {book.name}, Author: {book.author}, Publisher: {book.publisher}, Year: {book.year}")
    else:
        print("Book not found.")        



if __name__ == "__main__":
    main()   