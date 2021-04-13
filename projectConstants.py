from PIL import Image, ImageFont
import cv2
import numpy as np
from emoji_translate.emoji_translate import Translator

image_name = 'flower.JPEG'
sample_image = Image.open('./reference_images/' + image_name)
np_sample_image = np.array(sample_image)
cv2_sample_image = cv2.cvtColor(np_sample_image, cv2.COLOR_RGB2BGR)
run_name = '0'
path_results = './results/' + image_name[:-5] + run_name

HEIGHT, WIDTH = sample_image.size
POLYGONS_NUMBER = 100
ENTRY_SIZE = 6
HOF_NUMBER = 5
POPULATION_SIZE = 100
EPOCHS = 2500
P_CROSSOVER = 0.8
P_MUTATION = 0.5
TOURNAMENT_SIZE = 2
SBX_ETA = 20
MUTATION_VARIANCE = 0.2

# drawing with emojis
# each entry is emoji (0) at
# some position (1, 2) with some color (3,4,5)

# preprocessing should be done here
unicode_font = ImageFont.truetype("Symbola.otf", 36)

emo = Translator(exact_match_only=False, randomize=True)
words_for_emojifying = ['flower', 'rain', 'soup', 'happy']
emojis_for_drawing = [emo.emojify(x) for x in words_for_emojifying]
EMOJIS_NUMBER = len(emojis_for_drawing)
