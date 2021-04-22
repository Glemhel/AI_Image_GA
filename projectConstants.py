# Mikhail Rudakov BS19-02

from PIL import Image, ImageFont
import cv2
import numpy as np
from emoji_translate.emoji_translate import Translator

# file for setting the algorithm's hyper parameters and other necessary constants

# PUT YOUR PARAMETER HERE
# 1 - anime man
# 2 - stones scultpure
# 3 - rabbit
# 4 - Dr. Brown on hockey
# 5 - head of sculpture
# if you want to test custom image, put image name into this variable, like 'rabbit.jpg'
option = '5'

# name of the image to reconstruct
images_for_drawing = {'1': 'dr_stone.jpg', '2': 'rocks_sculpture.jpg', '3': 'rabbit.jpg', '4': 'hockey.jpg',
                      '5': 'head.jpg'}
image_name = images_for_drawing[option] if option in images_for_drawing else option
# path to that image
sample_image = Image.open('./reference_images/' + image_name)
# this image in other formats
np_sample_image = np.array(sample_image)
cv2_sample_image = cv2.cvtColor(np_sample_image, cv2.COLOR_RGB2BGR)

# identifier of algorithm run
run_name = '_manual_testing' + str(np.random.randint(10, 100))
# where to save results to
path_results = './results/' + image_name[:-4] + run_name

HEIGHT, WIDTH = sample_image.size  # size of the image
HOF_NUMBER = 2  # hall of fame size
POPULATION_SIZE = 20  # number of individuals in the population
EPOCHS = 10000  # number of epochs of the algorithm
P_CROSSOVER = 0.8  # probability of making a crossover
P_MUTATION = 0.5  # probability of mutation
TOURNAMENT_SIZE = 2  # size of selection tournament
SBX_ETA = 20  # value for crossover diversity
MUTATION_VARIANCE = 0.2  # value for mutation diversity

ENTRY_SIZE = 6  # amount of number each emoji is represented with
# drawing with emojis
# each entry is emoji at some position (0, 1) with some color (2,3,4,5)

# preprocessing should be done here
unicode_font = ImageFont.truetype("Symbola.otf", 36)

# translator from words to emoji
emo = Translator(exact_match_only=False, randomize=False)
pic_emojis = {'1': ['rock', 'doctor', 'man', 'arm', 'chemistry', 'strong',
                    'eye', 'green', 'fire'],
              '2': ['stone', 'tree', 'sun', 'water', 'ocean',
                    'light', 'happy', 'sea', 'relieved'],
              '3': ['rabbit', 'cute', 'flower', 'eye', 'nose',
                    'sunflower', 'grass', 'animal'],
              '4': ['ice hockey', 'ice', 'man', 'eyeglasses',
                    'joy', 'woohoo', 'ice skate', 'tshirt'],
              '5': ['man', 'cloud', 'eye', 'stone', 'ancient', 'pensive', 'cloud',
                    'hair', 'brain', 'nose'],
              'custom': ['happy', 'eye', 'sun', 'fire', 'water',
                         'woohoo', 'light', 'relieved']
              }
words_for_emojifying = pic_emojis[option] if option in pic_emojis else pic_emojis['custom']
# convert words to emojis
emojis_for_drawing = [emo.get_emoji(x) for x in words_for_emojifying]
EMOJIS_NUMBER = len(emojis_for_drawing)  # number of emojis generated
EMOJI_REPETITIONS = 50  # each emoji is represented this amount of times
print(emojis_for_drawing)
