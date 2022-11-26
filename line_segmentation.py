import numpy as np
import cv2
from math import fabs
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def average(image, lines):
    left = []
    right = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        y_int = parameters[1]
        if slope < 0:
            left.append((slope, y_int))
        else:
            right.append((slope, y_int))

    right_avg = np.average(right, axis=0)
    left_avg = np.average(left, axis=0)
    # left_line = make_points(image, left_avg)
    # right_line = make_points(image, right_avg)
    # return np.array([left_line, right_line])


def draw_lines(img, lines, color=[255, 0, 0], thickness=3):
    if lines is None:
        return
    img = np.copy(img)
    line_img = np.zeros(
        (
            img.shape[0],
            img.shape[1],
            3
        ),
        dtype=np.uint8,
    )
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)

    cv2.imshow('im', line_img)
    cv2.waitKey()

    # img = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
    return img


def pipeline(image):
    """
    An image processing pipeline which will output
    an image with the lane lines annotated.
    """
    height = image.shape[0]
    width = image.shape[1]

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    kernel_size = 3
    blur_gray = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)

    cannyed_image = cv2.Canny(gray_image, 50, 200)

    lines = cv2.HoughLinesP(
        cannyed_image,
        rho=8,
        theta=np.pi / 60,
        threshold=160,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=25,
    )
    # print(lines)
    img = draw_lines(gray_image, lines)
    plt.imshow(img)
    plt.show()

    average(None, lines)

    left_line_x = []
    left_line_y = []
    right_line_x = []
    right_line_y = []

    for line in lines:
        for x1, y1, x2, y2 in line:
            slope = (y2 - y1) / (x2 - x1)
            if fabs(slope) < 0.5:
                continue
            if slope <= 0:
                left_line_x.extend([x1, x2])
                left_line_y.extend([y1, y2])
            else:
                right_line_x.extend([x1, x2])
                right_line_y.extend([y1, y2])
    min_y = int(image.shape[0] * (3 / 5))
    max_y = int(image.shape[0])
    poly_left = np.poly1d(np.polyfit(
        left_line_y,
        left_line_x,
        deg=1
    ))

    left_x_start = int(poly_left(max_y))
    left_x_end = int(poly_left(min_y))

    poly_right = np.poly1d(np.polyfit(
        right_line_y,
        right_line_x,
        deg=1
    ))
    right_x_start = int(poly_right(max_y))
    right_x_end = int(poly_right(min_y))

    line_image = draw_lines(
        image,
        [[
            [left_x_start, max_y, left_x_end, min_y],
            [right_x_start, max_y, right_x_end, min_y],
        ]],
        thickness=5,
    )
    pts = np.array([[left_x_start, max_y], [left_x_end, min_y], [right_x_start, max_y],
                    [right_x_end, min_y]], np.int32)
    return line_image, pts


img_path = 'input/2000x1500_16_resized.jpg'
# img_path = 'input/P1040047-s.JPG'
# img_path = 'brockerLine.png'
# img = cv2.imread(img_path)
img = mpimg.imread(img_path)
q, pts = pipeline(img)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(q, [pts], (0, 0, 255))
plt.imshow(q)
plt.show()
