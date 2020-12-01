import numpy as np
import sys
import os
#opencv
import glob
import cv2
#import keras
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.models import Sequential
from keras.optimizers import Adam
#from keras.layers.core import Dense,Flatten
from keras.layers import Activation,Flatten,Dense, Dropout
from keras.metrics import categorical_crossentropy
from keras.layers.normalization import BatchNormalization
from keras.layers import Conv2D,MaxPooling2D
from keras.callbacks import ModelCheckpoint, EarlyStopping
#from Python.display import display, Image
from keras.models import load_model
#from Python.display import display
from PIL import Image
import tensorflow as tf
#from sklearn.metric import confusion_matrix
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#directories for train,test,validation data
trainpath ="/home/CAP5627-5/affective4/pain_classification/Training/"
testpath = '/home/CAP5627-5/affective4/pain_classification/Testing/'
validpath = '/home/CAP5627-5/affective4/pain_classification/Validation/'

#Data Augmentation
x=image.ImageDataGenerator(rescale=1./255,horizontal_flip=True,shear_range=0.2,zoom_range=0.2)
y=image.ImageDataGenerator()
Z=image.ImageDataGenerator()
trainbatch = x.flow_from_directory(trainpath, target_size = (180,180), batch_size = 200,color_mode='grayscale', class_mode='categorical',shuffle=True, seed = 42)
#print('TrainB:',len(trainbatch))
validbatch = y.flow_from_directory(validpath, target_size = (180,180), batch_size = 200,color_mode='grayscale', class_mode='categorical', seed = 42)
#print(len(validbatch))
testgen = Z.flow_from_directory(testpath ,target_size = (180,180),color_mode='grayscale', class_mode='categorical')
y_test=testgen.classes

#CNN
model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape=(180, 180,1)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Conv2D(64, (3, 3)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(2))
model.add(Activation('softmax'))
model.compile(Adam(lr=.0001,decay=0.001), loss='binary_crossentropy', metrics=['accuracy'])

checkpoint = ModelCheckpoint('Best.h5', monitor= 'val_acc', verbose=5,save_best_only=True, save_weights_only = False, mode='auto',period=1)

early_stop = EarlyStopping(monitor='val_acc',min_delta=0,patience=20, verbose=5, mode = 'auto')

model.fit_generator(trainbatch, steps_per_epoch=100, validation_data=validbatch, validation_steps=40, epochs=1000, callbacks=[checkpoint, early_stop])
#model = load_model('Best.h5')
model.summary()

#Testing the model
#test_acc = model.evaluate_generator(testgen,steps=)
#print('Test evaluate:', test_acc)
y_pred = model.predict_generator(testgen,steps=126)
y_pred = np.round(y_pred)
print('Test predict:',len( y_pred))

print('Confusion Matrix:',confusion_matrix(y_test,y_pred[:,0]))
print('Classification Report:',classification_report(y_test,y_pred[:,0]))
print('Accuracy Score:',accuracy_score(y_test, y_pred[:,0]))
