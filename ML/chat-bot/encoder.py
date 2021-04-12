import tensorflow as tf
class EncoderRNN(object):
    def __init__(self, num_units=150):
        self.num_units = num_units
        self.encoder_cell = tf.nn.rnn_cell.BasicLSTMCell(num_units)
    def forward(num_words):
