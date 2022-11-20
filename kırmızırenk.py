import cv2 as cv

image = cv.imread("kirmizisekil.jpg")

gri = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

ai, thresh = cv.threshold(gri,100,200,cv.THRESH_BINARY)
m = cv.moments(thresh)
print(m)
x = int(m["m10"]/m["m00"])
y = int(m["m01"]/m["m00"])

cv.circle(image, (x, y), 10, (255, 0, 0), -1)
cv.imshow("s", image)
cv.waitKey(0)
cv.destroyAllWindows()

