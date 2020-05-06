import os
import numpy

import tensorflow as tf

from tensorflow_gan.examples.mnist import util
from keras.models import load_model
from keras.datasets import mnist

from model import get_generator_model, LATENT_DIM

NUM_PICS_TO_CALCULATE_FID = 2048


def calculate_fid(opts):
    model_path = opts['--model-path']

    model = get_generator_model()
    model = load_model(model_path)

    (_, _), (x_test, _) = mnist.load_data()

    x_test = (x_test.astype(numpy.float32)) / 255.0
    x_test = numpy.expand_dims(x_test, axis=3)

    random_code = numpy.random.normal(size=(NUM_PICS_TO_CALCULATE_FID, LATENT_DIM))

    predicted_imgs = model.predict(random_code)
    numpy.random.shuffle(x_test)
    real_imgs = x_test[:NUM_PICS_TO_CALCULATE_FID]

    predicted_imgs = tf.convert_to_tensor(predicted_imgs, dtype=tf.float32)
    real_imgs = tf.convert_to_tensor(real_imgs, dtype=tf.float32)

    fid = util.mnist_frechet_distance(real_imgs, predicted_imgs)
    print("CALCULATED FID: %f" % fid)

    if opts.get('--output', None):
        path = opts['--output']
        if os.path.exists(path):
            os.remove(path)

        with open(path, "w") as f:
            f.write("CALCULATED FID: %f" % fid)
