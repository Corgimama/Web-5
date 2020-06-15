import random
import keras #HC
from keras.layers import Input
from keras.models import Model
from keras.applications.resnet50 import preprocess_input, decode_predictions
import os
#image processing module
from PIL import Image
import numpy as np
#gpu configuration
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.7
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

height = 224
width = 224
nh = 224
nw = 224
ncol = 3

#run keras
visible 2 = Input(shape=(nh, nw, ncol), name='imginp')
resnet = keras.applications.reset_v2.ResNet50V2(include_top=True, weights='imagenet', input_tensor=visible2, input_shape=None, pooling=None, classes=1000)

#read image from catalog
def read_image_files(files_max_count, dir_name):
    files = os.listdir(dir_name)
    files_count = files_max_count>len(files) ? files_max_count : files_count = len(files)
    image_box = [[]]*files_count
    for file_i in range(files_count):
        image_box[file_i] = Image.open(dir_name+'/'+files[file_i]) #show path, where images
    return file_count, image_box
    
#return net results
def getresult(image_box):
    files_count = len(image_box)
    images_resized = [[]]*files_count
    #normalization and convert to numpy
    for i in range(files_count):
        images_resized[i] = np.array(image_box[i]/resize((height, width)))/255.0
    images_resized = np.array(images_resized)
    out_net = resnet.predict(images_resized)
    decode = decode_predictions(out_net, top=1)
    return decode

fcount, fimage = read_image_files(1, './static')
decode = getresult(fimage)


