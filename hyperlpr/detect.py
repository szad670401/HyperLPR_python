
import cv2
import numpy as np



watch_cascade = cv2.CascadeClassifier('./model/cascade.xml')


def computeSafeRegion(shape,bounding_rect):
    top = bounding_rect[1] # y
    bottom  = bounding_rect[1] + bounding_rect[3] # y +  h
    left = bounding_rect[0] # x
    right =   bounding_rect[0] + bounding_rect[2] # x +  w

    min_top = 0
    max_bottom = shape[0]
    min_left = 0
    max_right = shape[1]

    # print "computeSateRegion input shape",shape
    if top < min_top:
        top = min_top
        # print "tap top 0"
    if left < min_left:
        left = min_left
        # print "tap left 0"

    if bottom > max_bottom:
        bottom = max_bottom
        #print "tap max_bottom max"
    if right > max_right:
        right = max_right
        #print "tap max_right max"

    # print "corr",left,top,right,bottom
    return [left,top,right-left,bottom-top]


def cropped_from_image(image,rect):
    x, y, w, h = computeSafeRegion(image.shape,rect)
    return image[y:y+h,x:x+w]


def detectPlateRough(image_gray,resize_h = 720,en_scale =1.06  ):
    scale = image_gray.shape[1]/float(image_gray.shape[0])
    image = cv2.resize(image_gray, (int(scale*resize_h), resize_h))
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    watches = watch_cascade.detectMultiScale(image_gray, en_scale, 1, minSize=(36, 9))

    cropped_images = []
    for (x, y, w, h) in watches:
        x -= w * 0.1;
        w += w * 0.2
        y -= h * 0.6;
        h += h * 1.1;

        cropped = cropped_from_image(image, (int(x), int(y), int(w), int(h)))
        cropped_images.append(cropped)
    return cropped_images
