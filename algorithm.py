import masteroogway
import tensorflow as tf
from tensorflow.python.keras.layers import Embedding, Dense, LSTM
from tensorflow.python.keras.models import Sequencial
from tensorflow.python.keras.losses import MeanSquaredError
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# advice quotes api to feed into the machine learning algorithm


# get question input
main_question = masteroogway.question

# tokenise question into its words
text = f"""{main_question}"""
tokenised_text = word_tokenize(text)

# filter the question into its key words
filtered_sentence = []
stop_words = set(stopwords.words("english"))
for words in stop_words:
    if words not in stop_words:
        filtered_sentence.append(words)

# stem and lemmonise the words to get them prepared for model building
ps = PorterStemmer()
stemmed_words = []
for word in filtered_sentence:
    stemmed_words.append(ps.stem(word))

# use dictionary to get only the nouns, verbs, and adjectives (ready to feed into algorithm)


# model that will be trained on advice quotes api
class masteroogwayAdviceModel(tf.keras.Model):
    def __init__(self) -> None:
        super(masteroogwayAdviceModel).__init__()
        # model parameters
