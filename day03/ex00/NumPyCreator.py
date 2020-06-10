import numpy as np

class NumpyCreator:
    def from_list(self, lst, dtype=None):
        try:
            nparr = np.asarray(lst, dtype=dtype)
        except TypeError:
            print("Argument must be of type list and dtype must be a valid python type")
            return None
        return nparr

    def from_tuple(self, tpl, dtype=None):
        try:
            nparr = np.asarray(tpl, dtype=dtype)
        except TypeError:
            print("Argument must be of type tuple and dtype must be a valid python type")
            return None
        return nparr
    
    def from_iterable(self, iter, dtype=None):
        try:
            nparr = np.asarray(iter, dtype=dtype)
        except TypeError:
            print("Argument must be of type iterable and dtype must be a valid python type")
            return None
        return nparr

    def from_shape(self, shape, value=0, dtype=None):
        try:
            nparr = np.full(shape, value, dtype)
        except TypeError:
            print("ERROR")
            return None
        return nparr

    def random(self, shape, dtype=None):
        try:
            nparr = np.random.random(shape)
        except TypeError:
            print("ERROR")
            return None
        return nparr

    def identity(self, shape, dtype=None):
        try:
            nparr = np.eye(shape, dtype)
        except TypeError:
            print("ERROR")
            return None
        return nparr
