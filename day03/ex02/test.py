from ScrapBooker import ScrapBooker
import numpy as np

def thin_test():
    x = np.arange(11*12).reshape(11, 12)
    print("X:")
    print(x)
    sp = ScrapBooker()
    a = sp.thin(x, 3, 1)
    print("a")
    print(a)

def juxtapose_test():
    x = np.arange(3*4).reshape(3, 4)

    print("x:")
    print(x)
    sp = ScrapBooker()
    b = sp.juxtapose(x, 1, 1)
    c = sp.juxtapose(x, 1, 0)
    print("b:")
    print(b)
    print("c:")
    print(c)

def mosaic_test():
    x = np.arange(4) + 1
    x.shape = (2,2)
    print("x:")
    print(x)
    y = np.resize(x, (3, 2))
    print("y:")
    print(y)

    
mosaic_test()