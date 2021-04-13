from PIL import Image
import cv2
import numpy as np

image_name = 'house.jpg'
sample_image = Image.open('./reference_images/' + image_name)
np_sample_image = np.array(sample_image)
cv2_sample_image = cv2.cvtColor(np_sample_image, cv2.COLOR_RGB2BGR)
run_name = 'run3'
path_results = './results/' + image_name[:-4] + run_name

HEIGHT, WIDTH = sample_image.size
POLYGONS_NUMBER = 100
HOF_NUMBER = 5
POPULATION_SIZE = 100
EPOCHS = 2500
P_CROSSOVER = 0.8
P_MUTATION = 0.5
TOURNAMENT_SIZE = 2
SBX_ETA = 20
MUTATION_VARIANCE = 0.2
