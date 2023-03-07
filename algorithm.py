import tensorflow as tf
from tensorflow.python.keras.layers import Embedding, Dense, LSTM
from tensorflow.python.keras.models import Sequencial
from tensorflow.python.keras.losses import MeanSquaredError
import masteroogway
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# advice quotes api to feed into the machine learning algorithm


# process language to put into ml algorithm


# get question input
    # make question input readable (put all letters to lowercase etc.)

# tokenise question into its words
main_question = masteroogway.question
text = f"""{main_question}"""
tokenised_text = word_tokenize(text)

# filter the question into its key words
filtered_sentence = []
stop_words = set(stopwords.words("english"))
for words in stop_words:
    if words not in stop_words:
        filtered_sentence.append(words)

# stem and lemmonise the words to get them prepared for model building





# use dictionary to get only the nouns, verbs, and adjectives (ready to feed into algorithm)


# model that will be trained on advice quotes api
class masteroogwayAdviceModel(tf.keras.Model):
    def __init__(self) -> None:
        super(masteroogwayAdviceModel).__init__()
        # model parameters
