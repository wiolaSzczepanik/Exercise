class PalindromRecognizer:

    def __init__(self):
        self.filename = input('Enter the filename: ')

    def read_file(self):
        file = open(self.filename)
        data = file.readlines()
        data = [elem.strip() for elem in data]
        return data

    def display_line_which_is_palindrom(self, data):
        for sentence in data:
            if self.check_if_is_palindrom(sentence):
                print(sentence)

    def check_if_is_palindrom(self, sentence):
        sentence = sentence.split(' ')
        for elem in sentence:
            if elem.lower() == elem[::-1].lower():
                return True
