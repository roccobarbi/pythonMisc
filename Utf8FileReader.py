class Utf8FileReader:
    
    def __init__(self, source):
        self._source = source

    # reads the file and applies the function fun to each line
    # if acc is defined as a list, it appends the result of fun to the list
    # if acc is null, it only runs fun on each line
    def map(self, fun, acc = None):
        file = open(self._source, 'r', encoding="utf-8")
        if (acc is None):
            # there is no accumulator
            for line in file:
                fun(line)
            file.close()
        else:
            # there is an accumulator
            for line in file:
                acc.append(fun(line))
            file.close()

    # reads the file and returns it as a list, line by line
    # newline characters at the end of each line, if present, are kept
    def read(self):
        acc = []
        self.map(lambda line: line, acc)
        return acc

    # reads the file and returns it as a list, line by line
    # newline characters are removed from the end of each line
    def readNoNL(self):
        acc = []
        self.map(lambda line: line.rstrip("\n"), acc)
        return acc
