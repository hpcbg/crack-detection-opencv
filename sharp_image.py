import cv2
import numpy as np

# read image as grayscale
# img = cv2.imread('input/k.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('input/P1040059-s.JPG', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (1500, 1125))

# threshold to binary
thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]

# apply morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
morph = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# find contours - write black over all small contours
letter = morph.copy()
cntrs = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(cntrs))
cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]
for c in cntrs:
    area = cv2.contourArea(c)
    if area < 100:
        cv2.drawContours(letter,[c],0,(0,0,0),-1)

# do canny edge detection
edges = cv2.Canny(letter, 200, 200)

# # write results
# cv2.imwrite("K_thresh.png", thresh)
# cv2.imwrite("K_morph.png", morph)
# cv2.imwrite("K_letter.png", letter)
# cv2.imwrite("K_edges.png", edges)

# show results
cv2.imshow("K_thresh", thresh)
cv2.imshow("K_morph", morph)
cv2.imshow("K_letter", letter)
cv2.imshow("K_edges", edges)
cv2.waitKey(0)
