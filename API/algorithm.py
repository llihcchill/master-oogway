import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import requests

# function to run all the code
def run_algorithm(question, final_quote):

    # tokenise question into its words
    text = f"""{question}"""
    tok = tokenised_text = word_tokenize(text)

    # define the arrays for filtering, stemming, and lemmonising the question
    filtered_question = [], stemmed_question = [], lemmonised_question = []

    def prepare_sentence(filtered_sentence_array, stemmed_words_array, lemmonised_words_array):
        # filter the question into its key words
        stop_words = set(stopwords.words("english"))
        for words in stop_words:
            if words not in stop_words:
                filtered_sentence_array.append(words)

        # stem the words to cut any prefixes
        ps = PorterStemmer(filtered_sentence_array, stemmed_words_array)
        for word in filtered_sentence_array:
            stemmed_words_array.append(ps.stem(word))

        # lemmonise the stemmed words
        lem = WordNetLemmatizer(stemmed_words_array, lemmonised_words_array)
        for word in stemmed_words_array:
            lemmonised_words_array.append(lem.lemmatize(word))

    # run the function to prepare the sentence for model building
    prepare_sentence(filtered_question, stemmed_question, lemmonised_question)

    # advice quotes api to feed into the machine learning algorithm
    # the api that will be used is the ZenQuotes api here: https://zenquotes.io/
    api_call = requests.get("https://zenquotes.io/api/quotes")
    api_quotes = api_call.json()["api_call"]

    # define the arrays for filtering, stemming, and lemmonising the quote
    filtered_quote = [], stemmed_quote = [], lemmonised_quote = [], final_quote = []

    # append every quote (if it matches a word in the lemmonised question) to final_quote
    for quote in api_quotes:
        quotes = quote["q"]
        # run function to prepare quote
        prepare_sentence(filtered_quote, stemmed_quote, lemmonised_quote)
        if(lemmonised_quote.__contains__(lemmonised_question) == True):
            final_quote.append(lemmonised_quote)
            break
        else:
            return
