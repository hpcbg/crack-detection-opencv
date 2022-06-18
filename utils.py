import numpy as np
import cv2
from matplotlib import pyplot as plt


def load_image(path, size=(1500, 1125)):
    img = cv2.imread(path, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, size)
    return img


def canny_edge_detection(img):
    return cv2.Canny(img, 45, 200)


def find_contours(closing, min_contour_area=None):
    contours = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    if min_contour_area is None:
        return contours
    else:
        return [contour for contour in contours if cv2.contourArea(contour) > min_contour_area]


def morf_closing(edges):
    kernel = np.ones((10, 10), np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    return closing


def draw_contours(img, contours, empty_img=False):
    if empty_img:
        img = np.zeros(img.shape, dtype='uint8')
    cv2.drawContours(img, contours=contours, contourIdx=-1, color=(255, 255, 255), thickness=8)
    return img


def show_image(img):
    cv2.imshow('im', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def create_featured_image(closing, original_img=None):
    # Create feature detecting method
    # sift = cv2.xfeatures2d.SIFT_create()
    # surf = cv2.xfeatures2d.SURF_create()
    orb = cv2.ORB_create(nfeatures=50)

    # Make featured Image
    keypoints, descriptors = orb.detectAndCompute(closing, None)
    featuredImg = cv2.drawKeypoints(closing, keypoints, None)

    # Create an output image
    cv2.imwrite('output/CrackDetected-7.jpg', featuredImg)

    if original_img.any():
        plot_featured_image(featuredImg, original_img)


def plot_featured_image(featuredImg, original_img):
    plt.subplot(121), plt.imshow(original_img)
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(featuredImg, cmap='gray')
    plt.title('Output Image'), plt.xticks([]), plt.yticks([])
    plt.show()
