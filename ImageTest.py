import numpy as np
from projectConstants import *
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import cv2


def generateRandomImageData(k):
    return np.random.random(size=k * 10)


def dataToImage(data):
    image = Image.new('RGB', (HEIGHT, WIDTH))
    draw = ImageDraw.Draw(image, 'RGBA')
    for i in range(len(data) // 10):
        p1 = (int(HEIGHT * data[i]), int(WIDTH * data[i + 1]))
        p2 = (int(HEIGHT * data[i + 2]), int(WIDTH * data[i + 3]))
        p3 = (int(HEIGHT * data[i + 4]), int(WIDTH * data[i + 5]))
        c = (int(255 * data[i + 6]), int(255 * data[i + 7]), int(255 * data[i + 8]), int(255 * data[i + 9]))
        draw.polygon([p1, p2, p3], c)
    return image


def showImage(data):
    image = dataToImage(data)
    image.show()


def imagesComparison(data, iteration=-1):
    image2 = dataToImage(data)
    f, axarr = plt.subplots(1, 2)
    plt.suptitle(
        str(iteration) + ' iterations. Fitness = ' + str(int(fitness_function(data)))
    )
    axarr[0].imshow(sample_image)
    axarr[1].imshow(image2)
    path_to_save = path_results + '/iteration' + str(iteration) + '.png'
    plt.savefig(path_to_save)
    plt.show()


def imageDifferenceFromSample(image):
    npimage = np.array(image)
    cv2image = cv2.cvtColor(npimage, cv2.COLOR_RGB2BGR)
    return arrays_mse(cv2image, cv2_sample_image)


# @jit
def arrays_mse(v1, v2):
    return np.sum((v1.astype("float") - v2.astype("float")) ** 2) / float(HEIGHT * WIDTH)


def saveImage(image):
    image.save("tempresult.jpg")


def fitness_function(data):
    return imageDifferenceFromSample(dataToImage(data))


def save_best_individual(population, iteration):
    x = min(population, key=lambda y: y.fitness_value)
    imagesComparison(x.data, iteration)


def save_population(population):
    np.save(path_results + './population', population)


def load_population(path=None):
    if path is None:
        return np.load(path_results + './population.npy', allow_pickle=True)
    return np.load(path, allow_pickle=True)
