# Required Libraries
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import argparse

split_size = 100

# Argument parsing variable declared
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--input",
                required=True,
                help="Path to input folder")

ap.add_argument("-o", "--output",
                required=True,
                help="Path to output folder")

args = vars(ap.parse_args())

# Find all the images in the provided images folder
input_path = args["input"]
output_path = args["output"]
file_names = [f for f in listdir(input_path) if isfile(join(input_path, f))]
images = np.empty(len(file_names), dtype=object)

# Iterate through every image
# and resize all the images.
for n, file_name in enumerate(file_names):
    path = join(input_path, file_name)
    images[n] = cv2.imread(join(input_path, file_name),
                           cv2.IMREAD_UNCHANGED)

    # Load the image in img variable
    img = cv2.imread(path, 1)

    print(f'Processing image: {n}')
    # Save the image in Output Folder
    for r in range(0, img.shape[0], split_size):
        for c in range(0, img.shape[1], split_size):
            cv2.imwrite(f"{output_path}/img_{n}_{r}_{c}.png", img[r:r + split_size, c:c + split_size, :])


