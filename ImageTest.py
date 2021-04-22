# Mikhail Rudakov BS19-02

from projectConstants import *
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import cv2


# file for image processing

# convert data in known format to image
def dataToImage(data):
    image = Image.new('RGB', (HEIGHT, WIDTH))  # create initial image to draw on
    draw = ImageDraw.Draw(image, 'RGBA')
    for i in range(0, len(data), ENTRY_SIZE):  # for each chunck of data
        x, y = int(data[i] * HEIGHT), int(data[i + 1] * WIDTH)  # coordinates of emoji
        font_color = (int(255 * data[i + 2]), int(255 * data[i + 3]), int(255 * data[i + 4]), int(255 * data[i + 5]))
        # font color of the image
        unicode_text = emojis_for_drawing[i // (ENTRY_SIZE * EMOJI_REPETITIONS)]  # the emoji itself - determined by
        # index in array
        draw.text((x, y), unicode_text, font=unicode_font, fill=font_color)  # draw that emoji
    return image


# show image generated from some data
def showImage(data):
    image = dataToImage(data)
    image.show()


# compare image with reference image, display and save it
def imagesComparison(data, iteration=-1):
    image2 = dataToImage(data)
    f, axarr = plt.subplots(1, 2)
    # proper title, including number of iteration and fitness value
    plt.suptitle(
        str(iteration) + ' iterations. Fitness = ' + str(int(imageDifferenceFromSample(data)))
    )
    # side-by-side comparison of images
    axarr[0].imshow(sample_image)
    axarr[1].imshow(image2)
    path_to_save = path_results + '/s2s_iteration' + str(iteration) + '.png'
    plt.savefig(path_to_save)
    plt.show()


# calculate difference between given image and reference image
def imageDifferenceFromSample(data):
    npimage = np.array(dataToImage(data))
    cv2image = cv2.cvtColor(npimage, cv2.COLOR_RGB2BGR)
    return arrays_mse(cv2image, cv2_sample_image)


# metrics for difference of two images - L2 (mean squared error)
def arrays_mse(v1, v2):
    return np.sum((v1.astype("float") - v2.astype("float")) ** 2) / float(HEIGHT * WIDTH)


# save image for testing purposes
def saveImage(data, iteration=-1):
    image = dataToImage(data)
    path_to_save = path_results + '/iteration' + str(iteration) + '.png'
    image.save(path_to_save)


# save best individual from the population based on fitness value and display it
def save_best_individual(population, iteration):
    x = min(population, key=lambda y: y.fitness_value)
    imagesComparison(x.data, iteration)
    saveImage(x.data, iteration)


# save current population into file for further needs
def save_population(population):
    np.save(path_results + './population', population)


# load population from file
def load_population(path=None):
    if path is None:
        return np.load(path_results + './population.npy', allow_pickle=True)
    return np.load(path, allow_pickle=True)
