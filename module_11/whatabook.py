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
    print("Welcome to Whatabook menu options!")
    print("Press '1 to view Books.")
    print("Press '2 to view Store Locations.")
    print("Press '3 to view My Account.")
    print("Press '4 to view Exit Whatabook menu options.")

def show_books(cursor):
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    print("-- DISPLAYING BOOK RECORDS --")
    for book in books:
        print("Book Name: {}".format(book[1]))
        print("Author Name: {}".format(book[3]))
        print()
    
def show_locations(cursor):
    cursor.execute("SELECT * FROM store")
    locations = cursor.fetchall()
    print("-- DISPLAYING LOCATION RECORDS --")
    for location in locations:       
        print("Locale: {}".format(location[1]))

def validate_user(cursor, user_id):
    cursor.execute("SELECT * FROM user WHERE user_id = " + user_id.strip())
    userlist = cursor.fetchall()
    return len(userlist) == 1

def run_my_account():
    user_id=input("Please enter your user_id:")
    if validate_user(cursor, user_id):
        user_choice = 5
        while user_choice !="3":
            show_account_menu()            
            user_choice=input("Please enter your choice:")
            if user_choice == "1":
                show_wishlist(cursor, user_id)                       
            if user_choice == "2":
                        show_books_to_add(cursor, user_id)
                        book_id=input("Please enter the Book ID:")
                        add_book_to_wishlist(cursor, user_id, book_id)

            if user_choice not in ("1","2","3"):
                        print("Please enter '1,'2,'3")
            if user_choice == "3":
                        print("Going back to Main Menu.")
    else:
        print("User Id is invalid.")

def show_account_menu():
    print("Here is the Account Menu:")
    print("Enter 1 for Wishlist")
    print("Enter 2 to add a Book")
    print("Enter 3 to return to Main Menu")

def show_wishlist(cursor, user_id):
    cursor.execute("SELECT * FROM wishlist INNER JOIN book on wishlist.book_id = book.book_id WHERE user_id = " + user_id.strip())
    wishlist = cursor.fetchall()
    for row in wishlist:
        print("")
        print(row[4])


def show_books_to_add(cursor, user_id):
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    print("-- DISPLAYING WISHLIST RECORDS --")
    for book in books:
        print("Book Name: {}".format(book[1]))
        print("Author Name: {}".format(book[3]))
        print("Book ID: {}".format(book[0]))

def add_book_to_wishlist(cursor, user_id, book_id):
    cursor.execute(f"INSERT INTO wishlist (user_id,book_id) VALUES ({user_id},{book_id})")



try:
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