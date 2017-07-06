#coding=utf-8
import detect
import  finemapping  as  fm

import segmentation

import cv2


import time

def SimpleRecognizePlate(image):
    t0 = time.time()
    images = detect.detectPlateRough(image)
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        image  =cv2.resize(image,(136,36))

        image_gray = fm.findContoursAndDrawBoundingBox(image)
        cv2.imshow("image,",image_gray)
        cv2.waitKey(0)
        blocks,res,confidence = segmentation.slidingWindowsEval(image_gray)
        if confidence>4.5:
            print "车牌:",res,"置信度:",confidence
        else:
            print "不确定的车牌:", res, "置信度:", confidence

    print time.time() - t0,"s"




