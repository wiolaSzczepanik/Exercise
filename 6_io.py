import string


class HapaxLegomenon:

    def __init__(self):
        self.hapaksy = {}

    def read_file(self):
        filename = input('Enter filename: ')
        file = open(filename)
        data = file.readlines()
        data = [elem.strip().split(' ') for elem in data]
        data = [item.strip(string.punctuation).lower() for elem in data for item in elem]
        return data

    def counter_words(self, data):
        for elem in data:
            if elem in self.hapaksy.keys():
                self.hapaksy[elem] += 1
            else:
                self.hapaksy[elem] = 1

    def dispaly_hapax(self):
        for elem in self.hapaksy:
            if self.hapaksy[elem] == 1:
                print(elem)
