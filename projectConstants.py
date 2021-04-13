from PIL import Image
import cv2
import numpy as np

image_name = 'mona_lisa.png'
sample_image = Image.open('./reference_images/' + image_name)
np_sample_image = np.array(sample_image)
cv2_sample_image = cv2.cvtColor(np_sample_image, cv2.COLOR_RGB2BGR)
run_name = 'smallPopulation'
path_results = './results/' + image_name[:-4] + run_name

HEIGHT, WIDTH = sample_image.size
POLYGONS_NUMBER = 100
HOF_NUMBER = 3
POPULATION_SIZE = 100
EPOCHS = 500
P_CROSSOVER = 0.9
P_MUTATION = 0.5
TOURNAMENT_SIZE = 2
SBX_ETA = 15
MUTATION_VARIANCE = 0.25
