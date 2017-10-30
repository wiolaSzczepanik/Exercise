class HapaxLegomenon:

    def __init__(self):
        self.filename = input('Enter filename: ')
        self.hapaksy = {}

    def read_file(self):
        file = open(self.filename)
        data = file.readlines()
        data = [elem.strip().split(' ') for elem in data]
        data = [item for elem in data for item in elem]
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
