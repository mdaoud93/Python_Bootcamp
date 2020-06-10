from PIL import Image
import numpy as np
from ColorFilter import ColorFilter

def invert_test():
    im = np.array(Image.open('woman.png'))
    cf = ColorFilter()
    im_i = cf.invert(im)
    img = Image.fromarray(im_i)
    img.show()

def to_blue_test():
    im = np.array(Image.open('woman.png'))
    cf = ColorFilter()
    im_blue = cf.to_blue(im)
    img = Image.fromarray(im_blue)
    img.show()

def to_green_test():
    im = np.array(Image.open('woman.png'))
    cf = ColorFilter()
    im_green = cf.to_green(im)
    # print(im_green)
    img = Image.fromarray(im_green)
    img.show()

def to_red_test():
    im = np.array(Image.open('woman.png'))
    cf = ColorFilter()
    im_red = cf.to_red(im)
    img = Image.fromarray(im_red)
    img.show()

def celluloid_test():
    im = np.array(Image.open('img.png'))
    cf = ColorFilter()
    im_th = cf.celluloid(im, 5)
    img = Image.fromarray(im_th)
    img.show()

def grayscale_test_m():
    im = np.array(Image.open('woman.png'))
    cf = ColorFilter()
    im_th = cf.to_grayscale(im, "m")
    img = Image.fromarray(im_th)
    img.show()

def grayscale_test_w():
    im = np.array(Image.open('woman.png'))
    cf = ColorFilter()
    im_th = cf.to_grayscale(im)
    img = Image.fromarray(im_th)
    img.show()

# invert_test()
# to_blue_test()
# to_green_test()
# to_red_test()
# celluloid_test()
# grayscale_test_m()
# grayscale_test_w()