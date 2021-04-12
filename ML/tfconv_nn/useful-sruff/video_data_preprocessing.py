from tensorflow import keras
import glob 
import os

from keras_video import VideoFrameGenerator

classes = ['back', 'forward', 'left', 'right']

#some global params
SIZE = (640, 360)
CHANNELS = 3
NBFRAME = 5
BS = 8

#directory pattern 
glob_pattern = 'data\\vids\\' + classname + '_resized.mp4'


#augmentation
data_aug = keras.preprocessing.image.ImageDataGenerator(
    zoom_range=.1,
    horizontal_flip=True,
    rotation_range=8, 
    width_shift_range=.2,
    height_shift_range=.2
)

#create video frame generator
train = VideoFrameGenerator(
    classes=classes,
    glob_pattern=glob_pattern,SS
    nb_frames=NBFRAME,
    split=.33,
    shuffle=True,
    batch_size=BS,
    target_shape=SIZE,
    nb_channel=CHANNELS,
    transformation=data_aug,
    use_frame_cache=True 
)
