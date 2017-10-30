def open_file_palindrome():
    filename = input("Enter the file: ")
    with open(filename) as word_file:
        for line in word_file.readlines():
            

