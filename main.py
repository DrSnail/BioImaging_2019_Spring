# -*- coding: utf-8 -*-
import numpy as np
import cv2

def draw(event, x, y, flags, param):
    r = 25
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x, y), int(r*1.3), (0,0,255), 2)
        cv2.line(image,(x-r, y-r),(x+r, y+r),(255,0,0), 5)
        cv2.line(image,(x-r, y+r),(x+r, y-r),(255,0,0), 5)


# start
image = cv2.imread("Images/Processing oocyte/img10.tif")

cv2.namedWindow('image', cv2.WINDOW_FREERATIO)
#cv2.imshow('image', image)

cv2.setMouseCallback('image', draw)

while(1):
    cv2.imshow('image', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("Result/gray.jpg", gray)

# распознавание границ и закрытие
edged = cv2.Canny(gray, 10, 250)
cv2.imwrite("Result/edged.jpg", edged)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("Result/closed.jpg", closed)

# поиск контуров
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
total = 0

# цикл по контурам
for c in cnts:
    # аппроксимируем контур
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # если у контура 4 вершины, предполагаем, что это четырехугольник
    if len(approx) == 4:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
        total += 1

# показываем результирующее изображение
print("Найдено {0} прямоугольников на этой картинке".format(total))
cv2.imwrite("output.jpg", image)

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyWindow('image')







# бинаризация
#ret,thresh1 = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
#cv2.imwrite("threshold.jpg", thresh1)

#cv2.destroyAllWindows()
