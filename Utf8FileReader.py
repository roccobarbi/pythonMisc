class Utf8FileReader:
    
    def __init__(self, source):
        self.source = source

    # reads the file and applies the function fun to each line
    # if acc is defined as a list, it appends the result of fun to the list
    # if acc is null, it only runs fun on each line
    def read(self, fun, acc = None):
        if (acc is None):
            # there is no accumulator
            file = open(self.source, 'r', encoding="utf-8")
            for line in file:
                fun(line)
            file.close()
        else:
            # there is an accumulator
            file = open(self.source, 'r', encoding="utf-8")
            for line in file:
                acc.append(fun(line))
            file.close()
