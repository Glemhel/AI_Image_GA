import numpy as np
from projectConstants import *
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import cv2


def generateRandomImageData(k):
    data = []
    for _ in range(k):
        idx = np.random.randint(0, EMOJIS_NUMBER)
        x, y, r, g, b = np.random.random(5)
        data.append([idx, x, y, r, g, b])
    return np.array(data)


def dataToImage(data):
    image = Image.new('RGB', (HEIGHT, WIDTH))
    draw = ImageDraw.Draw(image, 'RGBA')
    for i in range(len(data) // ENTRY_SIZE):
        unicode_emoji = emojis_for_drawing[data[i]]
        x, y = int(HEIGHT * data[i + 1]), int(WIDTH * data[i + 2])
        c = (int(255 * data[i + 3]), int(255 * data[i + 4]), int(255 * data[i + 5]))
        # draw image
        draw.text((x, y), unicode_emoji, font=unicode_font, fill=c)
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
