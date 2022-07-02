"""
Uses UI, because of same issues with the shared counter
"""

# Required Libraries
import uuid
from multiprocessing import Pool, cpu_count

import cv2
from os import listdir
from os.path import isfile, join
import argparse
import numpy
import threading


def handle_images(files):

    images = numpy.empty(len(files), dtype=object)
    # Iterate through every image
    # and resize all the images.
    input_path = args["input"]
    for n in range(0, len(files)):
        path = join(input_path, files[n])
        images[n] = cv2.imread(join(input_path, files[n]),
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
            f'{output_path}/{resize_width}x{resize_height}_{uuid.uuid1()}.jpg', resized_image)


# Argument parsing variable declared
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--input",
                required=True,
                help="Path to input folder")

ap.add_argument("-o", "--output",
                required=True,
                help="Path to output folder")

args = vars(ap.parse_args())

if __name__ == '__main__':
    # Find all the images in the provided images folder
    input_path = args["input"]
    files = [f for f in listdir(input_path) if isfile(join(input_path, f))]
    print(files)
    number_of_process = cpu_count()
    p = Pool(processes=number_of_process)
    p.map(handle_images, files)
    print("Images resized Successfully")



