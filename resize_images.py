# Required Libraries
from multiprocessing import Pool, cpu_count
import cv2
from os import listdir
from os.path import isfile, join
import argparse


def resize_image(input_file):
    print(f'Processing image: {input_file}')

    input_path = args["input"]

    path = join(input_path, input_file)

    # Load the image in img variable
    img = cv2.imread(path, 1)

    # Define a resizing Scale to declare how much to resize
    resize_scaling = int(args['scale'])
    resize_width = int(img.shape[1] * resize_scaling / 100)
    resize_height = int(img.shape[0] * resize_scaling / 100)
    resized_dimensions = (resize_width, resize_height)

    # Create resized image using the calculated dimensions
    resized_image = cv2.resize(img, resized_dimensions,
                               interpolation=cv2.INTER_AREA)

    # Save the image in Output Folder
    output_path = args["output"]
    cv2.imwrite(f'{output_path}/{input_file}_{resize_width}x{resize_height}.jpg', resized_image)


# Argument parsing variable declared
ap = argparse.ArgumentParser()

ap.add_argument("-s", "--scale",
                required=True,
                help="Resize scaling in percents")

ap.add_argument("-n", "--cpun",
                required=False,
                help="CPU count")

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

    # Get file names from the input folder
    files = [f for f in listdir(input_path) if isfile(join(input_path, f))]

    # If the number of CPUs is not set by the user, use all CPUs
    number_of_process = args.get('cpun')
    if number_of_process is None:
        number_of_process = cpu_count()

    # Create pool and map the files to the threads
    p = Pool(processes=number_of_process)
    p.map(resize_image, files)
    print("Images resized Successfully")



