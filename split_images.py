# Required Libraries
from multiprocessing import Pool, cpu_count
import cv2
from os import listdir, mkdir
from os.path import isfile, join
import argparse
from utils import find_cracks


def split_image(input_file):
    print(f'Processing image: {input_file}')

    input_path = args["input"]
    split_size = int(args["size"])
    output_path = args["output"]

    path = join(input_path, input_file)


    # Load the image in img variable
    img = cv2.imread(path, 1)

    # Save the tiles in Output Folder
    for r in range(0, img.shape[0], split_size):
        for c in range(0, img.shape[1], split_size):
            split_img = img[r:r + split_size, c:c + split_size, :]
            # If crack found in the tile, save in Positive.
            # Else, save in Rest, since this case is much more frequent.
            if find_cracks(split_img):
                cv2.imwrite(f"{output_path}/Positive/{input_file}_{r}_{c}.png", split_img)
            else:
                cv2.imwrite(f"{output_path}/Rest/{input_file}_{r}_{c}.png", split_img)


# Argument parsing variable declared
ap = argparse.ArgumentParser()

ap.add_argument("-s", "--size",
                required=True,
                help="Split size in pixels")

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
    output_path = args["output"]
    mkdir(f'{output_path}/Positive')
    mkdir(f'{output_path}/Rest')
    mkdir(f'{output_path}/Negative')

    # Get file names from the input folder
    files = [f for f in listdir(input_path) if isfile(join(input_path, f))]

    # If the number of CPUs is not set by the user, use all CPUs
    number_of_process = args.get('cpun')
    if number_of_process is None:
        number_of_process = cpu_count()

    # Create pool and map the file names to the threads
    p = Pool(processes=number_of_process)
    p.map(split_image, files)
    print("Images resized Successfully")



