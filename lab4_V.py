import sys
import numpy as np
import cv2 as cv
from tkinter import *


def Ball():
    hsv_min = np.array((0, 77, 17), np.uint8)
    hsv_max = np.array((208, 255, 255), np.uint8)

    fn = 'ball4.jpg'
    img = cv.imread(fn)

    hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV )
    thresh = cv.inRange( hsv, hsv_min, hsv_max )
    contours0, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours0:
        if len(cnt)>4:
            ellipse = cv.fitEllipse(cnt)
            cv.ellipse(img,ellipse,(0,0,255),2)

    cv.imshow('contours', img)

    cv.waitKey()
    cv.destroyAllWindows()

def Kv():
    
    hsv_min = np.array((0, 54, 5), np.uint8)
    hsv_max = np.array((187, 255, 253), np.uint8)

    fn = 'kn.png' # имя файла, который будем анализировать
    img = cv.imread(fn)

    hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    contours0, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
        box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
        box = np.int0(box) # округление координат
        cv.drawContours(img,[box],0,(0,0,255),2) # рисуем прямоугольник

    cv.imshow('contours', img) # вывод обработанного кадра в окно

    cv.waitKey()
    cv.destroyAllWindows()



def Menu():
    window = Tk()

    
    window.title("Menu")

    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200
    window.geometry('600x300+{}+{}'.format(w, h))
    window.configure(bg='#D0FBFF')

    btn = Button(window, text="Распознавание окружностей", padx=10, pady=7, command =Ball, bg='#7CFFA8', font="Arial")  
    btn.pack(anchor="center", padx=50, pady=20)

    btn = Button(window, text="Распознавание прямоугольника", padx=10, pady=7, command =Kv, bg='#7CFFA8', font="Arial")  
    btn.pack(anchor="center", padx=50, pady=20)

    btn1 = Button(window, text="Выход", padx=10, pady=7, command =exit, bg='#7CFFA8', font="Arial")  
    btn1.pack(anchor="center", padx=50, pady=20)
    


    window.mainloop()

Menu()

