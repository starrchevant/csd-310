import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    """
    This function prints the menu options for WhatABook.
    """    
    print("Welcome to Whatabook menu options!")
    print("Press '1 to view Books.")
    print("Press '2 to view Store Locations.")
    print("Press '3 to view My Account.")
    print("Press '4 to view Exit Whatabook menu options.")

def show_books(cursor):
    """
    This function prints out all the books in the database for WhatABook.
    """
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    print("-- DISPLAYING BOOK RECORDS --")
    for book in books:
        print("Book Name: {}".format(book[1]))
        print("Author Name: {}".format(book[3]))
        print()
    
def show_locations(cursor):
    """
    This function prints all locations for WhatABook.
    In the store table hours are stored in the locale field.
    """
    cursor.execute("SELECT * FROM store")
    locations = cursor.fetchall()
    print("-- DISPLAYING LOCATION RECORDS --")
    for location in locations:       
        print("Locale: {}".format(location[1]))

def validate_user(cursor, user_id):
    """
    This function checks for valid user_id's.
    """
    if len (user_id) == 0:
        return False
    try:
        cursor.execute(f"SELECT * FROM user WHERE user_id=\"{int(user_id)}\"")
        userlist = cursor.fetchall()
        return len(userlist) == 1
    except ValueError:
        return False

def validate_book(cursor,book_id):
    """
    This function checks for valid book_id's.
    """
    if len (book_id) == 0:
        return False
    try:
        cursor.execute(f"SELECT * FROM book WHERE book_id=\"{int(book_id)}\"")
        booklist = cursor.fetchall()
        return len(booklist) == 1
    except ValueError:
        return False

def run_my_account():
    """
    This function is to allow the user to access their personal accounts.
    """
    user_id=input("Please enter your user_id:")
    if validate_user(cursor, user_id):
        #The number 5 is just an arbitrary number that is not equal to 3 to enter the while loop.
        user_choice = 5
        while user_choice !="3":
            show_account_menu()            
            user_choice=input("Please enter your choice:")
            if user_choice == "1":
                show_wishlist(cursor, user_id)                       
            if user_choice == "2":
                        show_books_to_add(cursor, user_id)
                        book_id=input("Please enter the Book ID:")
                        if validate_book(cursor, book_id):
                            add_book_to_wishlist(cursor, user_id, book_id)
                        else: 
                           print("That is not a valid Book ID:")
                           print()                        
            if user_choice not in ("1","2","3"):
                        print("Please enter '1,'2,'3")
            if user_choice == "3":
                        print("Going back to Main Menu.")
    else:
        print("User Id is invalid.")

def show_account_menu():
    """
    This function prints out the Account Menu.
    """
    print("Here is the Account Menu:")
    print("Enter 1 for Wishlist")
    print("Enter 2 to add a Book")
    print("Enter 3 to return to Main Menu")

def show_wishlist(cursor, user_id):
    """
    This prints a user's wishlist.
    """
    #This where wishlist table is joined to book table to able to get book name out of book table and the out of the wishlist table.
    cursor.execute("SELECT * FROM wishlist INNER JOIN book on wishlist.book_id = book.book_id WHERE user_id = " + user_id.strip())
    wishlist = cursor.fetchall()
    for row in wishlist:
        print("")
        print(row[4])


def show_books_to_add(cursor, user_id):
    """
    This prints out the list of books for user to add.
    """
    cursor.execute("SELECT book_name, author, book_id FROM book")
    books = cursor.fetchall()
    print("-- DISPLAYING WISHLIST RECORDS --")
    for book in books:
        print("Book Name: {}".format(book[0]))
        print("Author Name: {}".format(book[1]))
        print("Book ID: {}".format(book[2]))

def add_book_to_wishlist(cursor, user_id, book_id):
    """
    This is where user add book(s) to the wishlist.
    """
    cursor.execute(f"INSERT INTO wishlist (user_id,book_id) VALUES ({user_id},{book_id})")
    #This is to finalize changes to the database.
    db.commit()


try:
    #Standard initialization to the database.
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor = db.cursor()

    user_choice=5
    while user_choice !="4":
        show_menu()       
        user_choice=input("Please enter your choice:")
        if user_choice == "1":
            show_books(cursor)
        if user_choice == "2":
            show_locations(cursor)
        if user_choice == "3":
            run_my_account()
        if user_choice == "4":
            print("Goodbye")
        if user_choice not in ("1","2","3","4"):
            print("Please enter '1,'2,'3,'4")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)
finally:
    db.close()