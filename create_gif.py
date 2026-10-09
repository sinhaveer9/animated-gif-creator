import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['Neon1.jpg', 'Neon2.jpg']
target_size = (500, 500)  # width, height — change to whatever you want
images = []

for filename in filenames:
    img = Image.open(filename).convert('RGB')
    img = img.resize(target_size)
    images.append(np.array(img))

iio.imwrite('neon.gif', images, duration=500, loop=0)
#to create the gif- python3 create_gif.py