from PIL import Image

HEIGHT = 512
WIDTH = 512
sample_image = Image.open('./images/white_triangle.jpg')
POLYGONS_NUMBER = 100
OPACITY_MIN = 20
OPACITY_MAX = 80
POPULATION_SIZE = 76
EPOCHS = 500
P_CROSSOVER = 0.8
P_MUTATION = 0.2
P_INSERTION = 0.4
P_DELETION = 0.1
P_EDITION = 1 - P_DELETION - P_INSERTION
TOURNAMENT_SIZE = 3
