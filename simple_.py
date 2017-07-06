from hyperlpr import pipline


import cv2

# image1 = cv2.imread("./dataset/0.jpg")
# image2 = cv2.imread("./dataset/1.jpg")
# image3 = cv2.imread("./dataset/5.jpg")
# image4 = cv2.imread("./dataset/6.jpg")

image5 = cv2.imread("./dataset/3144391.png")
#
# pipline.SimpleRecognizePlate(image4)
# pipline.SimpleRecognizePlate(image3)
pipline.SimpleRecognizePlate(image5)