

class CsvReader():
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        for _ in range(self.skip_top):
            next(self.file)
        line = self.file.readline()
        lst = line.split(self.sep)
        cols = len(lst)
        count = 0
        while True:
            count += 1
            line = self.file.readline()
            if not line:
                break
            lst = line.split(self.sep)
            if (cols != len(lst)):
                print(line)
                return None
            print(lst, end='')
            print("\tsize: {}".format(len(lst)))
        print(count)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def getheader(self):
        if self.header is False:
            return None
        for _ in range(self.skip_top):
            next(self.file)
        s = self.file.readline()
        return s

    def getdata(self):
        pass

    # def read_data():
