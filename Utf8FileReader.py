class Utf8FileReader:
    
    def __init__(self, source):
        self.source = source

    # reads the file and applies f to each line
    # if a is defined as a list, it appends the result of f to the list
    # if a is null, it only runs f on each line
    def read(self, f, a = None):
        if (a is None):
            # there is no accumulator
            file = open(self.source, 'r', encoding="utf-8")
            for line in file:
                f(line)
            file.close()
        else:
            # there is an accumulator
            file = open(self.source, 'r', encoding="utf-8")
            for line in file:
                a.append(f(line))
            file.close()
