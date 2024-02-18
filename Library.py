import os


class Library:
    def __init__(self):
        self.file = open("book.txt", "a+")
    def __del__(self):
        self.file.close()
        print("Library closed")


    def __ListBooks(self) -> int:
        """
        Display the list of books in the library.

        Returns:
            int: 0 if successful, -1 if an error occurs.
        """
        try:
            # Go to the start of the file
            self.file.seek(0)

            # Read the file
            books_list:list = self.file.read().splitlines()

            # Check if there are no books in the library
            if len(books_list) == 0:
                print("No books in library")
                return 0
            
            # Display the books
            print("Books in library:")
            for n,book in enumerate(books_list):
                self.__DisplayBook(book, n)
            print("-"*20)
            return 0
        except:
            # If an error occurs, return -1
            return -1
        
    def __AddBook(self) -> int:
        """
        Adds a new book to the library.

        Returns:
            int: 0 if the book is successfully added, -1 otherwise.
        """
        try:
            # Get the book details from the user
            user_inp_title:str = input("Enter book title: ")
            user_inp_author:str = input("Enter author name: ")
            user_inp_first_relase_year:str = input("Enter first release year: ")
            user_inp_num_of_pages:str = input("Enter number of pages: ")
            print()

            # Convert the book details to a desired format
            book_info:str = f"{user_inp_title},{user_inp_author},{user_inp_first_relase_year},{user_inp_num_of_pages}\n"

            # Go to the end of the file
            self.file.seek(0,2)

            # Write the book details to the file
            self.file.write(book_info)

            # Flush the file to ensure the data is written to the file
            self.file.flush()
            return 0
        except:
            # If an error occurs, return -1
            return -1
        

    def __RemoveBook(self) -> int:
        """
        Removes a book from the library.

        Returns:
            int: 0 if the book is successfully removed, -1 otherwise.
        """
        try:
            # Get the book title from the user
            user_inp_title:str = input("Enter book title: ")
            print()

            # Go to the start of the file
            self.file.seek(0)

            # Read the file
            books_list:list = self.file.read().splitlines()
        
            # Iterate through the books to find the book to remove
            found_books:dict = self.__FindBook(books_list, user_inp_title)

            # Check if the book is not found
            if len(found_books) == 0:
                print("Book not found")
                return 0
            
            # Check if more than one book with the same title is found
            elif len(found_books) > 1:
                # Display the found books
                print("Multiple books found\n")
                for n,book in found_books.items():
                    self.__DisplayBook(book, n)
                print("-"*20)
                print()

                try:
                    # Get the displayed book number from the user
                    user_inp_number:int = int(input("Enter book number to remove: "))
                except:
                    # If input from user can not be converted to int, return -1
                    print("Invalid input")
                    return -1
                
                # Remove the found book from the list with given book number
                books_list.pop(user_inp_number-1)

            # Remove the found book from the list
            else:
                # Remove the found book from the list
                books_list.pop(list(found_books.keys())[0])

            # Truncate the file to remove all the data
            self.file.truncate(0)
            # Go to the start of the file
            self.file.seek(0)

            # Write the updated list of books to the file
            for book in books_list:
                self.file.write(f"{book}\n")

            # Flush the file to ensure the data is written to the file
            self.file.flush()

            print("Book removed")
            return 0
        except:
            return -1
    
    def __FindBook(self, books_list:list, user_inp_title:str, user_inp_author:str = None, user_inp_first_relase_year:str = None, user_inp_num_of_pages:str = None) -> dict:
        """
        Finds books in the library based on the given criterias.

        Args:
            books_list (list): A list of books in the library.
            user_inp_title (str): The title of the book to search for.
            user_inp_author (str, optional): The author of the book to search for. Defaults to None.
            user_inp_first_relase_year (str, optional): The first release year of the book to search for. Defaults to None.
            user_inp_num_of_pages (str, optional): The number of pages of the book to search for. Defaults to None.

        Returns:
            dict: A dictionary containing the order number in list as keys and details of the found books as values.
        """
        try:
            # Create a dictionary to store the found books
            book_exist_dict:dict = dict()
            # Iterate through the books to find the book
            for n,book in enumerate(books_list):
                # Split the book details
                book_title:str = book.split(',')[0]
                book_author:str = book.split(',')[1]
                book_first_relase_year:str = book.split(',')[2]
                book_num_of_pages:str = book.split(',')[3]

                # Check if the book is found
                if book_title == user_inp_title:
                    # Check if the other criterias are given and if they match the book details
                    if user_inp_author and user_inp_author != book_author:
                        continue
                    if user_inp_first_relase_year and user_inp_first_relase_year != book_first_relase_year:
                        continue
                    if user_inp_num_of_pages and user_inp_num_of_pages != book_num_of_pages:
                        continue
                    # Add the found book to the dictionary
                    book_exist_dict[n] = book
            # Return the found books
            return book_exist_dict
        except:
            # If an error occurs, return an empty dictionary
            return list()
    

    def __DisplayBook(self, book_info_str:str, book_number:int) -> None:
        """
        Display the information of a book.

        Args:
            book_info_str (str): A string containing book information separated by commas.
            book_number (int): The of the book in the list.

        Returns:
            None
        """
        # Split the book details
        book_info:str = book_info_str.split(',')
        # Display the book details
        print("-"*20)
        print(f"Book {book_number+1}:")
        print(f"Book Title: {book_info[0]}")
        print(f"Author: {book_info[1]}")
        print(f"First Release Year: {book_info[2]}")
        print(f"Number of Pages: {book_info[3]}")

    def lib(self) -> None:
        """
        Displays a menu for the library operations and performs the selected operation.

        The menu options are:
        1. List Books
        2. Add Book
        3. Remove Book
        4. Exit

        Returns:
        None
        """
        # Loop to display the menu
        while True:
            # Display the menu and get the user input
            user_input:str = input("""\n*** MENU ***
1. List Books
2. Add Book
3. Remove Book
4. Exit
Enter your choice: """)
            print()
            # Perform the selected operation
            if user_input == "1":
                if (self.__ListBooks()):
                    print("Error listing books")
            elif user_input == "2":
                if (self.__AddBook()):
                    print("Error adding book")
            elif user_input == "3":
                if (self.__RemoveBook()):
                    print("Error removing book")
            elif user_input == "4":
                break
            else:
                print("Invalid input")
            
            # Clear the console
            # input("Press Enter to continue...")
            # os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    lib = Library()
    lib.lib()
            
        
        