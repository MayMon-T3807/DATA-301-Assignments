# Before this semester started, I worked as an intern at Inya Institiue for 6 months.
# I love to immerse myself in the book so I enjoyed working at Inya Institute.
# Inya Institute has both public library and digital library.
# So, let's look at the system of Inya Library how they manage their valuable books.
# this assignment is written to the reference of Inya Library

# First we define classes
class Book:
    def __init__(self, title, author, isbn, available=True):
        # includes information about the class
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"
    
    def borrow(self):
        if self.available:
            self.available = False
        else:
            raise Exception(f"'{self.title}' is already borrowed.")
    
    def return_book(self):
        self.available = True

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"
    
    def borrow_book(self, book):
        try:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name} has successfully borrowed '{book.title}'")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has successfully returned '{book.title}'")
        else:
            print(f"Error: {self.name} did not borrow '{book.title}'")

class Library:
    def __init__(self, name="Inya Institute Library"):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")
    
    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name}")
    
    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def lend_book(self, member_id, isbn):
        try:
            member = self.find_member_by_id(member_id)
            if not member:
                raise Exception(f"Member ID {member_id} not found")
            
            book = self.find_book_by_isbn(isbn)
            if not book:
                raise Exception(f"Book with ISBN {isbn} not found")
            
            member.borrow_book(book)
            
        except Exception as e:
            print(f"Error in lending book: {str(e)}")
    
    def return_book(self, member_id, isbn):
        try:
            member = self.find_member_by_id(member_id)
            if not member:
                raise Exception(f"Member ID {member_id} not found")
            
            book = self.find_book_by_isbn(isbn)
            if not book:
                raise Exception(f"Book with ISBN {isbn} not found")
            
            member.return_book(book)
            
        except Exception as e:
            print(f"Error in returning book: {str(e)}")
    
    def display_available_books(self):
        print(f"\nAvailable Books at {self.name}:")
        available_books = [book for book in self.books if book.available]
        if available_books:
            for book in available_books:
                print(str(book))
        else:
            print("No books available")
    
    def display_borrowed_books(self):
        print(f"\nBorrowed Books at {self.name}:")
        borrowed_books = [book for book in self.books if not book.available]
        if borrowed_books:
            for book in borrowed_books:
                print(str(book))
        else:
            print("No books currently borrowed")

def main():
    
    library = Library()
    # add my favourite books
    
    books = [
        Book("ကျောက်တိုင်ပေါ်က အင်္ကျီ", "ဒဂုန်တာရာ", "9991-1"),
        Book("နေပြည်တော်မှ စာများ", "လူထုဒေါ်အမာ", "9991-2"),
        Book("ပန်းနုလမ်း", "မြသန်းတင့်", "9991-3"),
        Book("မြန်မာ့ယဉ်ကျေးမှု", "ဦးသိန်းဟန်", "9991-4"),
        Book("အသက် ၂၈ နှစ်ရှိပြီဖြစ်သော မိန်းမတစ်ယောက်","နုနုရည်အင်း၀", "9991-5"),
        Book("ပန်းကြာ၀တ်မှုန်","ခင်ခင်ထူး","9991-6"),
        Book("အမှတ်တရ","ဂျူး","9991-7"),
        Book("ဖွင့်ဆောင်းမရတဲ့ထီး","ချိုပိန်းနောင်","9991-8"),
        Book("ကျန်ရစ်မြစ်", "သော်တာအေးလဲ့","9991-9")
        
    ]
    
    for book in books:
        library.add_book(book)
    
    # Add some members
    members = [
        Member(1001, "စုစုလှိုင်"),
        Member(1002, "သွေးသစ်"),
        Member(1003, "မမလေး"),
        Member(1004, "မေမွန်"),
        Member(1005, "နွေးနွေး")
    ]
    
    for member in members:
        library.add_member(member)
    
    # Demonstrate library operations
    print("\n=== Library Operations Demo ===")
    
    # Display initial available books
    library.display_available_books()
    
    # Lend some books
    print("\nLending books:")
    library.lend_book(1001, "9991-1")  
    library.lend_book(1002, "9991-2")  
    
    # Display available and borrowed books
    library.display_available_books()
    library.display_borrowed_books()
    
    # Return a book
    print("\nReturning books:")
    library.return_book(1001, "9991-1")  # မောင်မောင် returns ကျောက်တိုင်ပေါ်က အင်္ကျီ
    
    # Final display of available and borrowed books
    library.display_available_books()
    library.display_borrowed_books()

if __name__ == "__main__":
    main()

