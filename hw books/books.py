import json
file_name = 'book.json'

# load the book 
def load_book():
    try:
        with open(file_name, 'r') as bookf:
            all_books = json.load(bookf)
    except FileNotFoundError:
        all_books = {}
    return all_books

# Save the book 
def save_book(books):
    with open(file_name, 'w') as bookf:
        json.dump(books, bookf, indent=4)

# Add a new book
def add_book(books):
    book_name = input("Enter the book name: ")
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    edition = input("Edition: ")
    books[book_name] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "edition": edition
    }
    print(f"Book '{book_name}' successfully added!")

# Search a book
def search_book(books):
    user_input = input("Enter the book name: ").lower()
    found = False
    for book_name, info in books.items():
        if user_input in book_name.lower():
            print(f"-------{book_name}-----")
            print(f"Title: {info['title']}")
            print(f"Author: {info['author']}")
            print(f"ISBN: {info['isbn']}")
            print(f"Edition: {info['edition']}")
            print("--------------------")
            found = True
    if not found:
        print(f"No book found with name containing '{user_input}'.")

# Delete a book
def delete_book(books):
    delete_name = input("Enter book name to delete: ")
    if delete_name in books:
        del books[delete_name]
        save_book(books)
        print(f"Book '{delete_name}' successfully deleted!")
    else:
        print(f"No book found with the name '{delete_name}'.")

# View all books
def view_all_book(books):
    if not books:
        print("No books available.")
    for book_name, info in books.items():
        print(f"\nBook Name: {book_name}")
        print(f"  Title: {info['title']}")
        print(f"  Author: {info['author']}")
        print(f"  ISBN: {info['isbn']}")
        print(f"  Edition: {info['edition']}")

# Main menu loop
def imake_funk():
    book = load_book()
    while True:
        print("---------- Book Choice List ----------")
        print("1. View All Books")
        print("2. Add New Book")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        print("--------------------------------------")
        choice = int(input("Enter the Choice Number: "))
        if choice == 1:
            print('--- View All Books ---')
            view_all_book(book)
        elif choice == 2:
            print('--- Add New Book ---')
            add_book(book)
            save_book(book)
        elif choice == 3:
            print('--- Search Book ---')
            search_book(book)
        elif choice == 4:
            print('--- Delete Book ---')
            delete_book(book)
        elif choice == 5:
            print('chla jaa Exit kiya tho')
            break
        else:
            print("Invalid choice plese valid nimber")

if __name__ == '__main__':
    imake_funk()
