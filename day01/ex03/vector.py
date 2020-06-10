import sys

class Vector:
    '''A class representing a vector and its methods'''
    def __init__(self, param):
        if (isinstance(param, list)):
            self.values = []
            for i in param:
                if (not isinstance (i, float) and not isinstance(i, int)):
                    print("Error, values must be of type \'float\'")
                    return
                self.values.append(float(i))
            self.size = len(param)
        elif (isinstance(param, int)):
            self.values = []
            if (param < 0):
                self.size = 0
            else:
                self.size = param
            for i in range (self.size):
                self.values.append(float(i))
        elif (isinstance(param, range)):
            if (len(param) < 0):
                self.values = []
                self.size = 0
            else:
                self.values = []
                self.size = len(param)
                for i in param:
                    self.values.append(float(i))
        else:
            print("Input error, input must be of type 'list', 'integer' or 'range'")
    def __add__(self, other):
        if (isinstance(other, Vector)):
            if (self.size != other.size):
                print("\033[1;31mERROR, vectors must be of the same size\033[1;0m")
                return None
            new_lst = []
            for i in range(self.size):
                new_lst.append(self.values[i] + other.values[i])
            new_v = Vector(new_lst)
            return (new_v)
        elif (isinstance(other, int) or isinstance(other, float)):
            new_lst = []
            for i in range(self.size):
                new_lst.append(self.values[i] + other)
            new_v = Vector(new_lst)
            return (new_v)
        else:
            print("\033[1;31mERROR, must be of type int or foat\033[1;0m")
            return None
    
    __radd__ = __add__

    def __sub__(self, other):
        if (isinstance(other, Vector)):
            if (self.size != other.size):
                print("\033[1;31mERROR, vectors must be of the same size\033[1;0m")
                return None
            new_lst = []
            for i in range(self.size):
                new_lst.append(self.values[i] - other.values[i])
            new_v = Vector(new_lst)
            return (new_v)
        elif (isinstance(other, int) or isinstance(other, float)):
            new_lst = []
            for i in range(self.size):
                new_lst.append(self.values[i] - other)
            new_v = Vector(new_lst)
            return (new_v)
        else:
            print("\033[1;31mERROR, must be of type int or foat\033[1;0m")
            return None

    def __rsub__(self, other):
        print("\033[1;31mERROR, cannot substract a vector from a number\033[1;0m")
        return None

    def __mul__(self, other):
        if (isinstance(other, Vector)):
            if (self.size != other.size):
                print("\033[1;31mERROR, vectors must be of the same size\033[1;0m")
                return None
            sum = 0
            for i in range(self.size):
                sum = sum + self.values[i] * other.values[i]
            return (sum)
        elif (isinstance(other, int) or isinstance(other, float)):
            new_lst = []
            for i in range(self.size):
                new_lst.append(self.values[i] * other)
            new_v = Vector(new_lst)
            return (new_v)
        else:
            print("\033[1;31mERROR, must be of type int or foat\033[1;0m")
            return None

    __rmul__ = __mul__

    def __str__(self):
        s = "Size: " + str(self.size) + "\n"
        s = s + str(self.values)
        return s

    __repr__ = __str__
