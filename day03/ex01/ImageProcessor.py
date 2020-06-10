# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot

class ImageProcessor:
    def load(self, path):
        try:
            self.img = image.imread(path)
            print("Loading image of dimensions {} {}".format(self.img.shape[0], self.img.shape[1]))
            return self.img
        except Exception:
            print ("ERROR")

    def display(self, array):
        try:
            pyplot.imshow(array)
            pyplot.show()
        except Exception:
            print ("ERROR")

imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")
print(arr)
imp.display(arr)
