import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.parse import RegexpParser
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import requests

# prepare the sentence for comparison
def prepare_sentence(sentence_array, nouns_and_verbs):
    # split sentence into individual words first
    split_sentence = sentence_array.split()

    # tokenise question into its words
    text = f"""{split_sentence}"""
    print(text)
    tokenised_sentence = word_tokenize(text)

    # filter the question into its key words
    stop_words = set(stopwords.words("english"))
    for words in stop_words:
        if words not in stop_words:
            tokenised_sentence.append(words)

    # use parts-of-speech tagging to define what type of word it is
    tagged_words = nltk.pos_tag(tokenised_sentence)

    # filters out everything but nouns and verbs
    nouns_verbs_chunked = """chunky:{<NN.?>*<NNS.?>*<NNP.?>*<NNPS.?>*<VB.?>*<VBG.?>*<VBD.?>*<VBN>?}"""
    chunker = RegexpParser(nouns_verbs_chunked)
    output = chunker.parse(tagged_words)

    # for every word, put into the nouns_and_verbs array
    for word in output:
        word.append(nouns_and_verbs)

# function to run all the code
def run_algorithm(question, final_quote):

    # define array to store the prepared question and run the function to prepare it
    final_question = []
    prepare_sentence(question, final_question)

    # define the array for keeping the final quote, along with a boolean to check whether
    # it should continue to look for a quote that fits well
    final_quote = [], continue_looking = True

    # while loop to interate finding the best quote to send
    while continue_looking == True:

        # advice quotes api to feed into the machine learning algorithm
        # the api that will be used is the ZenQuotes api here: https://zenquotes.io/
        api_call = requests.get("https://zenquotes.io/api/quotes")
        api_quotes = api_call.json()["api_call"]

        # if it matches a word in the quesiton, append it to final_quote and break the while loop
        for quote in api_quotes:

            # get the quote from the JSON file and run function to prepare the quote for comparison
            single_quote = quote["q"]
            final_single_quote = []
            prepare_sentence(single_quote, final_single_quote)

            for word in final_single_quote:
                if word in final_question:
                    print(final_question)
                    print(final_single_quote)
                    final_quote.append(final_single_quote)
                    continue_looking = False
                    break
                else:
                    continue
