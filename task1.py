import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image1 = cv.imread('img1.jpg', 0)
image1 = cv.resize(image1,(400,400))
print(image1)
image4 = cv.imread('img2.jpg', 0)
image4 = cv.resize(image4,(400,400))
print(image4)
image3 = cv.imread('img3.jfif', 0)
image3 = cv.resize(image3,(400,400))
print(image3)
image2 = cv.imread('img4.jfif', 0)
image2 = cv.resize(image2,(400,400))
print(image2)
image5 = cv.imread('R.jpg', 0)
image6 = cv.imread('debo.jpeg', 0)
image7 = cv.imread('kernel.png',0)
def displayImage(img):
    plt.imshow(img, cmap='gray')
    plt.show()

def task1(img1, img2, img3, img4):

    imageA = np.concatenate((img1, img2), axis=1)
    imageB = np.concatenate((img3, img4), axis=1)
    imageC = np.concatenate((imageA, imageB), axis=0)
    displayImage(imageC)


task1(image1, image2, image3, image4)

def task3(img5):
    pixel = int(input("Enter The Required Pixel: "))
    img5[img5 < pixel] = 0
    plt.imshow(img5,cmap='gray')
    plt.show()


task3(image5)

ret,thresh1 = cv.threshold(image5,100,255,cv.THRESH_TOZERO)
def displayImage(img):
    plt.imshow(img, cmap='gray')
    plt.show()
#displayImage(thresh1)

def task4(img6):
    blurred_debo = cv.GaussianBlur(img6, (5, 5), 0)    #low pass
    displayImage(blurred_debo)
    sharpen_debo= img6-blurred_debo   #high pass
    displayImage(sharpen_debo)
    canny_edges = cv.Canny(image=blurred_debo, threshold1=100, threshold2=200)  #high pass
    displayImage(canny_edges)
task4(image6)


def task5(img7):
     blured = cv.GaussianBlur(img7, (5, 5), 0)
     sharpened =  img7  - blured
     cv.imshow("img",sharpened)
     cv.waitKey(0)

task5(image7)
def task6(img8):
    img8 = cv.GaussianBlur(img8, (5, 5), 0)
    canny_edges = cv.Canny(image=img8, threshold1=100, threshold2=200)  # high pass
    displayImage(canny_edges)
    kernel = (2, 2)
    image = canny_edges
    for i in range(5):
        image = cv.dilate(image, kernel)
    displayImage(image)
task6(image6)