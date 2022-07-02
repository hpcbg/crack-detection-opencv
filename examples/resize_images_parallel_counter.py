"""
Issues with the shared counter
Useful links
https://stackoverflow.com/questions/35088139/how-to-make-a-thread-safe-global-counter-in-python
https://docs.python.org/3/library/multiprocessing.html
https://stackoverflow.com/questions/2080660/how-to-increment-a-shared-counter-from-multiple-processes
"""

# Required Libraries
import multiprocessing

import cv2
from os import listdir
from os.path import isfile, join
import argparse
import numpy
import threading
from multiprocessing import Pool, Value, RawValue, Lock


# class Counter:
#     def __init__(self, value=0):
#         # RawValue because we don't need it to create a Lock:
#         self.val = RawValue('i', value)
#         self.lock = Lock()
#
#     def increment(self):
#         with self.lock:
#             self.val.value += 1
#
#     def value(self):
#         with self.lock:
#             return self.val.value
#
#
# thread_safe_counter = Counter(0)
# lock = Lock()
counter = Value('i', 0)


def handle_images(image_file):
    global counter
    with counter.get_lock():
        counter.value += 1
    print("counter.value:", counter.value)

    # with lock:
    #     print(f'{image_file}_{thread_safe_counter.value()}')
    #     thread_safe_counter.increment()
    #     print(f"Hello from thread {threading.current_thread().name}")
    # images = numpy.empty(len(onlyfiles), dtype=object)
    # # Iterate through every image
    # # and resize all the images.
    # for n in range(0, len(onlyfiles)):
    #     path = join(input_path, onlyfiles[n])
    #     images[n] = cv2.imread(join(input_path, onlyfiles[n]),
    #                            cv2.IMREAD_UNCHANGED)
    #
    #     # Load the image in img variable
    #     img = cv2.imread(path, 1)
    #
    #     # Define a resizing Scale
    #     # To declare how much to resize
    #     resize_scaling = 50
    #     resize_width = int(img.shape[1] * resize_scaling / 100)
    #     resize_height = int(img.shape[0] * resize_scaling / 100)
    #     resized_dimensions = (resize_width, resize_height)
    #
    #     # Create resized image using the calculated dimensions
    #     resized_image = cv2.resize(img, resized_dimensions,
    #                                interpolation=cv2.INTER_AREA)
    #
    #     # Save the image in Output Folder
    #     output_path = args["output"]
    #     cv2.imwrite(
    #         f'{output_path}/{resize_width}x{resize_height}_{n}_resized.jpg', resized_image)


if __name__ == '__main__':
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
    # onlyfiles = [f for f in listdir(input_path) if isfile(join(input_path, f))]
    onlyfiles = [i for i in range(23)]
    # thread_safe_counter = Counter(0)
    number_of_process = multiprocessing.cpu_count()
    p = Pool(processes=number_of_process)
    p.map(handle_images, onlyfiles)
    print("Images resized Successfully")



