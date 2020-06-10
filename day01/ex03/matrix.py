def check_data(data):
    if (not isinstance(data, list)):
        # print("Error, the data must be of type list")
        return False
    list_size = len(data[0])
    for row in data:
        if (len(row) != list_size):
            # print("Error, Matrix rows are not of the same size")
            return False
        for i in row:
            if (not isinstance(i, float) and not isinstance(i, int)):
                # print("Error, Matrix elements must be of type 'float' or 'int'")
                return False
    return True

class Matrix:
    
    def __init__(self, *args):
        if (len(args) == 0):
            self.data=[[]]
            self.shape=(0,0)
            return
        if (len(args) == 1):
            if (isinstance(args[0], tuple)):
                self.shape = args[0]
                if (len(self.shape) != 2):
                    raise ValueError("Error, shape must be of the form '(rows, colomns)'")
                self.data = []
                col = [0.0] * self.shape[1]
                for i in range (self.shape[0]):
                    self.data.append(col)
            elif (isinstance(args[0], list)):
                if (check_data(args[0]) == False):
                    raise ValueError("Error, invalid matrix")
                self.data = args[0]
                r = len(self.data)
                c = len(self.data[0])
                self.shape = (r, c)
            else:
                raise TypeError("Error, invalid matrix")
        if (len(args) == 2):
            if (not isinstance(args[0], list) or not isinstance(args[1], tuple)):
                raise TypeError("Error, invalid matrix")
            if (len(args[1] != 2)):
                raise (ValueError("Error, shape must be of the form '(rows, colomns)'"))


    def __str__(self):
        data = self.data
        shape = self.shape
        s = "\033[0;32m(" + str(shape[0]) + ", " + str(shape[1]) + ")\n"
        for r in range (shape[0]):
            for c in range(shape[1]):
                s = s + str(data[r][c])
                s = s + "  "
            s = s + "\n"
        s = s + "\033[0;0m"
        return s
