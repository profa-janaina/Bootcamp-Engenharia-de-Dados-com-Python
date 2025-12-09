from skimage.io import imread, imwrite

def read_image(path, is_gray = False):
    image = imread(path, as_gray = is_gray)
    return image

def save_image(image, path):
    imwrite(path, image) 