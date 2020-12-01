import cv2
import numpy as np
import sys
import glob
import os
from pathlib import Path

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('/home/CAP5627-5/FaceClassifier/haarcascade_frontalface_default.xml')

#files=glob.glob('*.jpg')
datapath='/home/CAP5627-5/affective3/pain_classification/Testing/Pain/'
image1=''
c=0
for file3 in os.scandir(datapath):

    # Read the image
            image = cv2.imread(file3.path)
            #image = np.full((100, 80, 3), 12, np.uint8)


            #image = np.array(image, dtype=np.uint8)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
                )

            print ("Found {0} faces!".format(len(faces)))

    # calculating face location verticies
            for x,y,w,h in faces:
                r = max(w, h) / 2
                centerx = x + w / 2
                centery = y + h / 2
                nx = int(centerx - r)
                ny = int(centery - r)
                nr = int(r * 2)

                image1 = gray[ny:ny + nr, nx:nx + nr]
                #image1 = gray[x:x+180, y:y+180]
                image1 = cv2.resize(image1, (180, 180))
            print ("cropped_{1}{0}".format(str(file3),str(x)))
            asdff  = "/home/CAP5627-5/affective5/pain_classification/Testing/Pain/"
            asdff+= file3.name
            cv2.imwrite(asdff, image1)
            c=c+1

print('Total Images Cropped:',c)
