import cv2
import glob
import os
import numpy as np
import csv

def calcRGB(img_array):
    average_color_per_row = np.average(img_array, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    return average_color

def main():
    files = glob.glob("./images/*")

    f = open('./output/RGB.csv', 'w')
    csvWriter = csv.writer(f)

    for fname in files:
        bgr = cv2.imread(fname, -1)
        average_color = calcRGB(bgr)
        listData = []
        listData.append(os.path.basename(fname))
        for element in average_color :
            listData.append(element)
        print(listData)

        csvWriter.writerow(listData)

if __name__ == '__main__':
    main()
