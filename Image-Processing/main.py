import cv2
import numpy as np

flag = False
ix = -1
iy = -1

def draw(event, x, y, flags, param):
    global flag, ix, iy
    if event == 1:
        flag = True
        ix = x
        iy = y
    elif event == 0:

        if flag == True:
            cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y), color=(255,0,0), thickness=-1)

    elif event == 4:
        pass
    # print(event)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", draw)

img = cv2.imread("img/fruits.jpg")
# img = np.zeros((512, 512, 3))

while True:

    cv2.imshow('window', img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()






















# #Rectangle
# cv2.rectangle(img, pt1=(100, 100), pt2=(300,300), color=(255,0,0), thickness=-1)
# #Circle
# cv2.circle(img,center=(100,400), radius=50, color=(0,255,0), thickness=-1)
# #Line
# cv2.line(img,pt1=(0,0), pt2=(512,512), color=(0,255,255), thickness=2)
# #Text
# cv2.putText(img, org=(100,100), fontFace=cv2.FONT_ITALIC, fontScale=45, color=(0,255,255), thickness=2, lineType=cv2.LINE_AA,text="hello")
#
# cv2.imshow("Original", img)
# cv2.waitKey(0)


















# # Read an Image
# img = cv2.imread('img/fruits.jpg')
#
# # img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# # print(img_gray.shape)
#
#
# # img[:, :, 0] = 0
#
# imgBlue = img[:, :, 0]
# imgGreen = img[:, :, 1]
# imgRed = img[:, :, 2]
# # new_img = np.hstack((img1, img2, img3))
# new_img = np.hstack((imgBlue, imgGreen,imgRed))
#
# cv2.imshow('window', new_img)
# cv2.waitKey(0)