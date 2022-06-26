from utils import *

image_path = 'input/P1040059-s.JPG'
# image_path = 'input/img_0_400_800.png'
new_size = (1500, 1125)
img = load_image(image_path)

edges = canny_edge_detection(img)

# Morphological Closing Operator
closing = morf_closing(edges)

contours = find_contours(closing, min_contour_area=200)

contours_on_image = draw_contours(img, contours, empty_img=True)
show_image(contours_on_image)

# # Image processing ( smoothing )
# # Averaging
# blur = cv2.blur(contours_on_image,(10, 10))
#
# # Image smoothing: bilateral filter
# bilateral = cv2.bilateralFilter(blur, 5, 75, 75)


edges = canny_edge_detection(contours_on_image)

create_featured_image(edges, img)


