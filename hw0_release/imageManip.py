import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
from skimage import color
from skimage import io


def load(image_path):
    """ Loads an image from a file path

    Args:
        image_path: file path to the image

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """
    out = None

    ### YOUR CODE HERE
    # Use skimage io.imread
    out = io.imread(image_path)
    ### END YOUR CODE

    return out


def change_value(image):
    """ Change the value of every pixel by following x_n = 0.5*x_p^2
        where x_n is the new value and x_p is the original value

    Args:
        image: numpy array of shape(image_height, image_width, 3)

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """

    out = None

    ### YOUR CODE HERE
    out = 0.5 * image**2
    ### END YOUR CODE

    return out


def convert_to_grey_scale(image):
    """ Change image to gray scale

    Args:
        image: numpy array of shape(image_height, image_width, 3)

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """
    out = None

    ### YOUR CODE HERE
    out = color.rgb2gray(image)
    ### END YOUR CODE

    return out


def rgb_decomposition(image, channel):
    """ Return image **excluding** the rgb channel specified

    Args:
        image: numpy array of shape(image_height, image_width, 3)
        channel: str specifying the channel

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """

    out = None

    ### YOUR CODE HERE
    if channel == 'R':
        out = image[:, :, 0]
    if channel == 'G':
        out = image[:, :, 1]
    if channel == 'B':
        out = image[:, :, 2]
    ### END YOUR CODE

    return out


def lab_decomposition(image, channel):
    """ Return image decomposed to just the lab channel specified

    Args:
        image: numpy array of shape(image_height, image_width, 3)
        channel: str specifying the channel

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """

    lab = color.rgb2lab(image)
    out = None

    ### YOUR CODE HERE
    if channel == 'L':
        out = lab[:, :, 0]
    if channel == 'A':
        out = lab[:, :, 1]
    if channel == 'B':
        out = lab[:, :, 2]
    ### END YOUR CODE

    return out


def hsv_decomposition(image, channel):
    """ Return image decomposed to just the hsv channel specified

    Args:
        image: numpy array of shape(image_height, image_width, 3)
        channel: str specifying the channel

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """

    hsv = color.rgb2hsv(image)
    out = None

    ### YOUR CODE HERE
    if channel == 'H':
        out = hsv[:, :, 0]
    if channel == 'S':
        out = hsv[:, :, 1]
    if channel == 'V':
        out = hsv[:, :, 2]
    ### END YOUR CODE

    return out


def mix_images(image1, image2, channel1, channel2):
    """ Return image which is the left of image1 and right of image 2 excluding
    the specified channels for each image

    Args:
        image1: numpy array of shape(image_height, image_width, 3)
        image2: numpy array of shape(image_height, image_width, 3)
        channel1: str specifying channel used for image1
        channel2: str specifying channel used for image2

    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """

    ### YOUR CODE HERE
    y, x, z = image1.shape
    out = np.zeros(image1.shape)

    out[:, 0:x//2, 0] = image1[:, 0:x//2, 0]
    out[:, (x//2+1):-1, 0] = image2[:, (x//2+1):-1, 0]

    out[:, 0:x//2, 1] = image1[:, 0:x//2, 1]
    out[:, (x//2+1):-1, 1] = image2[:, (x//2+1):-1, 1]

    out[:, 0:x//2, 2] = image1[:, 0:x//2, 2] 
    out[:, (x//2+1):-1, 2] = image2[:, (x//2+1):-1, 2]
    ### END YOUR CODE

    return out
