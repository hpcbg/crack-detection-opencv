# Required Libraries
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy

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
onlyfiles = [f for f in listdir(input_path) if isfile(join(input_path, f))]
images = numpy.empty(len(onlyfiles), dtype=object)

# Iterate through every image
# and resize all the images.
for n in range(0, len(onlyfiles)):
    path = join(input_path, onlyfiles[n])
    images[n] = cv2.imread(join(input_path, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)

    # Load the image in img variable
    img = cv2.imread(path, 1)

    # Define a resizing Scale
    # To declare how much to resize
    resize_scaling = 50
    resize_width = int(img.shape[1] * resize_scaling / 100)
    resize_height = int(img.shape[0] * resize_scaling / 100)
    resized_dimensions = (resize_width, resize_height)

    # Create resized image using the calculated dimensions
    resized_image = cv2.resize(img, resized_dimensions,
                               interpolation=cv2.INTER_AREA)

    # Save the image in Output Folder
    output_path = args["output"]
    cv2.imwrite(
        f'{output_path}/{resize_width}x{resize_height}_{n}_resized.jpg', resized_image)

print("Images resized Successfully")
