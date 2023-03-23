import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import requests


def prepare_sentence(sentence_array, stemmed_words_array, lemmonised_words_array):
    # tokenise question into its words
    text = f"""{sentence_array}"""
    tokenised_sentence = word_tokenize(text)

    # filter the question into its key words
    stop_words = set(stopwords.words("english"))
    for words in stop_words:
        if words not in stop_words:
            tokenised_sentence.append(words)

    # stem the words to cut any prefixes
    ps = PorterStemmer(tokenised_sentence, stemmed_words_array)
    for word in tokenised_sentence:
        stemmed_words_array.append(ps.stem(word))

    # lemmonise the stemmed words
    lem = WordNetLemmatizer(stemmed_words_array, lemmonised_words_array)
    for word in stemmed_words_array:
        lemmonised_words_array.append(lem.lemmatize(word))


# function to run all the code
def run_algorithm(question, final_quote):
    # define the arrays for stemming and lemmonising the question
    stemmed_question = [], lemmonised_question = []

    # run the function to prepare the sentence for model building
    prepare_sentence(question, stemmed_question, lemmonised_question)

    # define the arrays for stemming and lemmonising the quote, along with a variable to check whether
    # it should continue to look for a quote that fits in well
    stemmed_quote = [], lemmonised_quote = [], final_quote = [], continue_looking = True

    # while loop to interate finding the best quote to send
    while continue_looking == True:
        # advice quotes api to feed into the machine learning algorithm
        # the api that will be used is the ZenQuotes api here: https://zenquotes.io/
        api_call = requests.get("https://zenquotes.io/api/quotes")
        api_quotes = api_call.json()["api_call"]

        # if it matches a word in the lemmonised question, append it to final_quote and break the while loop
        for quote in api_quotes:
            # get the quote and tokenise it
            single_quote = quote["q"]

            # run function to prepare quote
            prepare_sentence(single_quote, stemmed_quote, lemmonised_quote)

            if(lemmonised_quote.__contains__(lemmonised_question) == True):
                final_quote.append(lemmonised_quote)
                continue_looking = False
                break
            else:
                return
