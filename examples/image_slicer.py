# https://pypi.org/project/image-slicer/
# https://stackoverflow.com/questions/63798231/slice-images-in-directory-using-glob-image-slicer-based-on-pixel-sizes-instead

import glob
import image_slicer

for file in glob.glob('~\\test_folder\\*.jpg'):
    image_slicer.slice(file, row=3, col=4)