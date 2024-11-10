class Book:  #ye book bnayega jo bh user bolega wo, alag is liye likha taki previous book nd next book se link hojaye
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_book(self, title, isbn): #book add karna
        new_Book = Book(title, isbn)
        new_Book.next = self.head  # type: ignore
        self.head = new_Book

    def remove_book(self, isbn): 
        prev = None
        current = self.head
        # current variable ko baar baar check kiya jayega while loop use karke and uske hisab se prev variable ko change krenge 

        while current:
            if current.isbn == isbn:
                if prev: # agar prev ki val none nahi h to current ke next value prev ke next mtlb current m daldo
                    prev.next = current.next
                else: # agar prev ki value none h matlab current wala head hi h, to head ko current ke next wala element dedo 
                    self.head = current.next
                return True
            prev = current  # agar value match nh ki to agle term search kro
            current = current.next
        return False

    def search_book(self, query):
        current = self.head
        while current:
            if query in current.title or query in current.isbn:
                print("Book Found")
                return
            current = current.next
        print("Book not found.")


def main():
    library = LinkedList()

    while True:
        print("--------------------------------------Library Management System--------------------------------------")
        print('''
      1: Add Book
      2: Remove Book
      3: Search Book
      4: Exit
      ''')

        ch = int(input("Enter your choice: ")) 
# isse konsa option choose kar rha user wo input le rhe

        if(ch!=1 and ch!=2 and ch!=3 and ch!=4):
            print("Invalid input. Program Exited.") 
    # agar 1,2,3,4 ke alawa aur koi number diya to program end hojayega 

# agar 1st option liya h to
        elif(ch == 1):
            title = input("Enter book title: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, isbn)

# 2nd option
        elif(ch == 2):
            isbn = input("Enter ISBN of the book to remove: ")
            if library.remove_book(isbn):
                print("Book removed successfully.")
            else:
                print("Book not found.")


        elif(ch == 3):
            query = input("Enter title or ISBN to search: ")
            library.search_book(query)
    
        print("--------------------THANK YOU--------------------")

main()