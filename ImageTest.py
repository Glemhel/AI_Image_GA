import numpy as np
from projectConstants import *
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import cv2

from numba import jit, cuda


def generateRandomImageData(k):
    data = np.array([])
    for i in range(k):
        triangle = [np.random.randint(0, HEIGHT) for _ in range(6)]
        #c = list(np.random.randint(0, 255, 3))
        c = [255, 255, 255]
        #o = np.random.randint(OPACITY_MIN, OPACITY_MAX + 1)
        o = 50
        data1 = triangle + c + [o]
        data1 = np.array(data1)
        data = np.concatenate((data, data1))
    return data.astype(int)


# @jit(nopython=True)
def dataToImage(data):
    data = data.astype(int)
    image = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image, 'RGBA')
    for i in range(len(data) // 10):
        p1 = (data[i], data[i + 1])
        p2 = (data[i + 2], data[i + 3])
        p3 = (data[i + 4], data[i + 5])
        c = (data[i + 6], data[i + 7], data[i + 8], data[i + 9])
        draw.polygon([p1, p2, p3], c)
    return image


def showImage(data):
    image = dataToImage(data)
    image.show()


def imagesComparison(data, iteration=np.random.randint(0, 100000)):
    image2 = dataToImage(data)
    f, axarr = plt.subplots(1, 2)
    plt.suptitle(
        str(iteration) + ' iterations. Fitness = ' + str(int(fitness_function(data)))
    )
    axarr[0].imshow(sample_image)
    axarr[1].imshow(image2)
    plt.savefig('iteration' + str(iteration) + '.png')
    plt.show()


def imagesDifference(image1, image2):
    npimage1 = np.array(image1)
    cvimage1 = cv2.cvtColor(npimage1, cv2.COLOR_RGB2BGR)
    npimage2 = np.array(image2)
    cvimage2 = cv2.cvtColor(npimage2, cv2.COLOR_RGB2BGR)
    return arrays_mse(cvimage1, cvimage2)


# @jit
def arrays_mse(v1, v2):
    return np.sum((v1.astype("float") - v2.astype("float")) ** 2) / float(len(v1))


def saveImage(image):
    image.save("result.jpg")


def fitness_function(data):
    return imagesDifference(sample_image, dataToImage(data))


def save_best_individual(population, iteration):
    x = min(population, key=lambda y: y.fitness())
    imagesComparison(x.data, iteration)
