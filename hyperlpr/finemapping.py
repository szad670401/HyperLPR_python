
import cv2
import numpy as np

from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)


def fitLine_ransac(pts,zero_add = 0 ):
    if len(pts)>=2:
        [vx, vy, x, y] = cv2.fitLine(pts, cv2.DIST_HUBER, 0, 0.01, 0.01)
        lefty = int((-x * vy / vx) + y)
        righty = int(((136- x) * vy / vx) + y)
        return lefty+30+zero_add,righty+30+zero_add
    return 0,0


def findContoursAndDrawBoundingBox(gray_image):


    line_upper  = [];
    line_lower = [];

    line_experiment = []

    grouped_rects = []
    for k in np.linspace(-1.8, -0.2,5):
        thresh_niblack = threshold_niblack(gray_image, window_size=25, k=k)
        binary_niblack = gray_image > thresh_niblack
        binary_niblack = binary_niblack.astype(np.uint8) * 255
        imagex, contours, hierarchy = cv2.findContours(binary_niblack.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            bdbox = cv2.boundingRect(contour)
            if (bdbox[3]/float(bdbox[2])>0.5 and bdbox[3]*bdbox[2]>100 and bdbox[3]*bdbox[2]<1300) or (bdbox[3]/float(bdbox[2])>3 and bdbox[3]*bdbox[2]<100):
                # cv2.rectangle(rgb,(bdbox[0],bdbox[1]),(bdbox[0]+bdbox[2],bdbox[1]+bdbox[3]),(255,0,0),1)
                line_upper.append([bdbox[0],bdbox[1]])
                line_lower.append([bdbox[0]+bdbox[2],bdbox[1]+bdbox[3]])
                line_experiment.append([bdbox[0],bdbox[1]])
                line_experiment.append([bdbox[0]+bdbox[2],bdbox[1]+bdbox[3]])
                # grouped_rects.append(bdbox)

    rgb = cv2.copyMakeBorder(gray_image,30,30,0,0,cv2.BORDER_REPLICATE)
    leftyA, rightyA = fitLine_ransac(np.array(line_lower),2)
    rows,cols = rgb.shape[:2]

    # rgb = cv2.line(rgb, (cols - 1, rightyA), (0, leftyA), (0, 0, 255), 1,cv2.LINE_AA)

    leftyB, rightyB = fitLine_ransac(np.array(line_upper),-2)

    rows,cols = rgb.shape[:2]

    # rgb = cv2.line(rgb, (cols - 1, rightyB), (0, leftyB), (0,255, 0), 1,cv2.LINE_AA)
    pts_map1  = np.float32([[cols - 1, rightyA], [0, leftyA],[cols - 1, rightyB], [0, leftyB]])
    pts_map2 = np.float32([[136,36],[0,36],[136,0],[0,0]])

    mat = cv2.getPerspectiveTransform(pts_map1,pts_map2)
    image = cv2.warpPerspective(rgb,mat,(136,36))
    return image