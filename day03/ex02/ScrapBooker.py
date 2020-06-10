import numpy as np 

class ScrapBooker:
    def crop(self, array, dim, pos=(0, 0)):
        '''crops the image as a rectangle with the given dimensions
        (meaning, the new height and width for the image), whose top left corner is given by the position
        argument. The position should be (0,0) by default'''
        for i, j, k in zip(dim, pos, array.shape):
            if (i + j > k):
                print("ERROR")
                return
        c = array[pos[0]:dim[0]+ pos[0], pos[1]:dim[1] + pos[1]]
        return np.copy(c)

    def thin(self, array, n, axis):
        '''deletes every n-th pixel row along the specified axis (0 vertical, 1 horizontal)'''
        a = axis
        if (axis == 0):
            a = 1
        elif(axis == 1):
            a = 0
        res = np.delete(array, np.s_[n - 1::n], a)
        return (res)

    def juxtapose(self, array, n, axis):
        '''uxtaposes n copies of the image along the specified axis (0 vertical, 1 horizontal).'''
        a = axis
        if (axis == 0):
            a = 1
        elif(axis == 1):
            a = 0
        for i in range(n):
            res = np.append(array, array, a)
        return (res)
    def mosaic(array, dimensions):
        '''makes a grid with multiple copies of the array. The dimensions argument
        specifies the dimensions (meaning the height and width) of the grid'''
        res = np.resize(array, dimensions)
        return res


