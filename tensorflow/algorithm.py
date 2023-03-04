import tensorflow as tf
import numpy
import importlib

# import the Tensorflow algorithm into the main script
masteroogway = input('masteroogway')
importlib.import_module(masteroogway)

# advice quotes api to feed into the machine learning algorithm


# dictionary of every noun, verb, and adjective to comprehend questions (maybe another api?)


# get question input
    # make question input readable (put all letters to lowercase etc.)


# use dictionary to get only the nouns, verbs, and adjectives (ready to feed into algorithm)


# model that will be trained on advice quotes api
class masteroogwayAdviceModel(tf.keras.Model):
    def __init__(self) -> None:
        super(masteroogwayAdviceModel).__init__()
        # model parameters
