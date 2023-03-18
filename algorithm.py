from masteroogway import question
import tensorflow as tf
from tensorflow.python.keras.layers import Embedding, Dense, LSTM
from tensorflow.python.keras.models import Sequencial
from tensorflow.python.keras.losses import MeanSquaredError
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import requests

# tokenise question into its words
text = f"""{question}"""
tok = tokenised_text = word_tokenize(text)


# filter the question into its key words
def filter_sentence(filtered_sentence_array):
    stop_words = set(stopwords.words("english"))
    for words in stop_words:
        if words not in stop_words:
            filtered_sentence_array.append(words)

# stem and lemmonise the words to get them prepared for model building
def stem_sentence(filtered_sentence_array, stemmed_words_array):
    ps = PorterStemmer()
    for word in filtered_sentence_array:
        stemmed_words_array.append(ps.stem(word))

# lemmonise stemmed words
def lem_sentence(stemmed_words_array, lemmonised_words_array):
    lem = WordNetLemmatizer()
    for word in stemmed_words_array:
        lemmonised_words_array.append(lem.lemmatize(word))

# define the arrays for filtering, stemming, and lemmonising the question
filtered_question = [], stemmed_question = [], lemmonised_question = []

# run each function for each stage of the word preperation
filter_sentence(filtered_question)
stem_sentence(filtered_question, stemmed_question)
lem_sentence(stemmed_question, lemmonised_question)

# advice quotes api to feed into the machine learning algorithm
# the api that will be used is the ZenQuotes api here: https://zenquotes.io/
api_call = requests.get("https://zenquotes.io/api/quotes")
api_quotes = api_call.json()["api_call"]

# define the arrays for filtering, stemming, and lemmonising the quote
filtered_quote = [], stemmed_quote = [], lemmonised_quote = [], final_quote = []

# append every quote to single_api_quotes
for quote in api_quotes:
    quotes = quote["q"]
    # run functions to prepare quote
    filter_sentence(filtered_quote)
    stem_sentence(filtered_quote, stemmed_quote)
    lem_sentence(stemmed_quote, lemmonised_quote)
    if(lemmonised_quote.__contains__(lemmonised_question) == True):
        final_quote.append(lemmonised_quote)
    else:
        break


# model that will be trained on advice quotes api
class masteroogwayAdviceModel(tf.keras.Model):
    def __init__(self) -> None:
        super(masteroogwayAdviceModel).__init__()
        # model parameters
