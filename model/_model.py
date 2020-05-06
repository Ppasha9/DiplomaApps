from keras.models import Sequential, Model
from keras.layers import Input, Dense, Conv2DTranspose, Reshape, BatchNormalization, Activation
from keras.layers.advanced_activations import LeakyReLU

DECODER_NUM_LAYERS = 3
DECODER_NUM_FILTERS = 1024

BATCH_NORM_EPSILON = 1e-05
BATCH_NORM_DECAY = 0.9

LATENT_DIM = 100


def get_generator_model():
    num_layers = DECODER_NUM_LAYERS
    num_units = DECODER_NUM_FILTERS
    z_dim = LATENT_DIM
    b_n_epsilon = BATCH_NORM_EPSILON
    b_n_decay = BATCH_NORM_DECAY

    height = 28 // 2 ** (num_layers - 1)
    width = 28 // 2 ** (num_layers - 1)

    input_decoder = Input(shape=(z_dim,))

    model = Sequential()
    model.add(Dense(num_units * height * width, input_dim=z_dim))
    model.add(Reshape(target_shape=(height, width, num_units)))
    model.add(LeakyReLU())

    for i in range(num_layers - 1):
        scale = 2 ** (i + 1)
        model.add(Conv2DTranspose(filters=num_units // scale, kernel_size=(4, 4), strides=(2, 2), padding="SAME"))
        model.add(BatchNormalization(momentum=b_n_decay, epsilon=b_n_epsilon))
        model.add(LeakyReLU())

    model.add(Conv2DTranspose(filters=1, kernel_size=(4, 4), strides=(1, 1), padding="SAME"))
    model.add(Activation("sigmoid"))
    model.summary()

    output_decoder = model(input_decoder)
    dec_model = Model(input_decoder, output_decoder)

    return dec_model
