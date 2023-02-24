import tensorflow as tf
import importlib

# import the Tensorflow algorithm into the main script
masteroogway = input('masteroogway')
importlib.import_module(masteroogway)

# model that will be trained on advice quotes
class masteroogwayAdviceModel(tf.keras.Model):
    def __init__(self) -> None:
        super(masteroogwayAdviceModel).__init__()
        # model parameters


# language processing model that will be trained on Master Oogway quotes
class masteroogwayModel(tf.keras.Model):
    def __init__(self) -> None:
        super(masteroogwayModel).__init__()
        # model parameters
