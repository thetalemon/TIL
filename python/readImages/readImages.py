import cv2
import glob
import os

files = glob.glob("./images/*")

print(files)

for fname in files:
    bgr = cv2.imread(fname, -1)
    img = cv2.Canny(bgr, 100, 200)
    outputPath ="./output/"  +  os.path.basename(fname)
    print(outputPath)
    cv2.imwrite(outputPath, img)
