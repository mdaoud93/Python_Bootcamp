from PIL import Image
import numpy as np

class ColorFilter:
    def invert(self, array):
        '''invert(array) : Takes a NumPy array of an image as an argument and returns an array with inverted color.'''
        return (255 - array)
    def to_blue(self, array):
        ''''Takes a NumPy array of an image as an argument and returns an array with a blue filter.'''
        res = np.zeros(array.shape, dtype=np.uint8)
        res[:, :, 2] = array[:, :, 2]
        return res

    def to_green(self, array):
        ''''Takes a NumPy array of an image as an argument and returns an array with a green filter.'''
        res = np.array(array * [0, 1, 0], dtype=np.uint8)
        return res
    def to_red(self, array):
        ''''Takes a NumPy array of an image as an argument and returns an array with a red filter.'''
        res = array - self.to_blue(array) - self.to_green(array)
        return res

    def celluloid(self, array, shades):
        th_range = np.linspace(0, 255, shades, endpoint=True)
        print(th_range)
        height = array.shape[0]
        width = array.shape[1]
        channel = array.shape[2]
        res = array.copy()
        for i in range (height):
            for j in range (width):
                for k in range (channel):
                    t = 0
                    while (t < shades and array[i][j][k] > th_range[t]):
                        t += 1
                    res[i][j][k] = th_range[t]
        return res

    def to_grayscale(self, array, filter="w"):
        if (filter == "m" or filter == "mean"):
            gray_value = np.sum(array, 2) / 3
            return gray_value
        if (filter == "w" or filter == "weighted"):
            weights = [0.299, 0.587, 0.114]
            tile = np.tile(weights, reps=(array.shape[0],array.shape[1],1))
            return (np.sum(tile * array, axis=2))