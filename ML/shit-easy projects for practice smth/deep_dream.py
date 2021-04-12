import numpy as np
from functools import partial
from PIL import Image
import tensorflow.compat.v2 as tf
import tensorflow.compat.v1 as tfc
import urllib.request
import os
import zipfile


def main():
    #download google pre-trained neural network
    local_zip_file = 'inception5h.zip'
    if not os.path.exists(local_zip_file):
        #download
        model_url = urllib.request.urlopen(url)
        with open(local_zip_file, 'wb') as output:
            output.write(model_url.read())

        #extract
        with zipfile.ZipFile(local_zip_file, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
    model_fn = 'tensorflow_inseption_graph.pb'

    #Creating tf session and loading the model
    graph = tf.Graph()
    sess = tfc.InteractiveSession(graph=graph)
    with tfc.gfile.FastGFile((local_zip_file), 'rb') as f:
        graph_def = tf.io.gfile.GFile()
        graph_def.ParseFromString(f.read())
    t_input = tf.placeholder(np.float32, name='input') #define input tensor
    imagenet_mean = 117.0
    t_preprocessed = tf.expand_dims(t_input-imagenet_mean, 0)
    tf.import_graph_def(graph_def, {'input': t_preprocessed})

    layers = [op.name for op in graph.get_operations() if op.type=='Cony2D' and 'import/' in op.name]
    feature_nums = [int(graph.get_tensor_by_name(model_name+':0').get_shape()[-1]) for name in layers]

    print('Number of layers: ', len(layers))
    print('Total numbers of feature channels:', sum(feature_nums))


    def render_deepdream(t_obj, img0=img_noise, iter_n=10, step=1.5, octave_n=4, octave_scale=1.4):
        t_score = tf.reduce_mean(t_obj) #defining optimization objective
        t_grad  = tf.gradients(t_score, t_input)[0]

        #split the image into a number of octaves
        img = img0
        octaves = []
        for _ in range(octave_n-1):
            hw = img.shape[:2]
            lo = resize(img, np.int32(np.float32(hw)/octave_scale))
            hi = img-resize(low, hw)
            img = lo
            octaves.append(hi)

        #generate details octave by octave
        for octave in range(octave_n):
            if octave > 0:
                hi = octaves[-octave]
                img = resize(img, hi.shape[:2]) + hi
            for _ in range(iter_n):
                g = calc_grad_tiled(img, t_grad)
                img += g*(step / (np.abs(g).mean()+1e-7))
            #output deep dreamed image
            showarray(img/255.0)


    #Pick a layer to enchance my image
    layer = 'mixed4d_3x3_bottleneck_pre_relu'
    channel = 139

    img0 = PIL.Image.open('image.jpg')
    img0 = np.float32(img0)

    #Apply gradient ascent to the layer
    render_deepdream(tf.square(T('mixed4c')), img0)

if __name__ == '__main__':
    main()
