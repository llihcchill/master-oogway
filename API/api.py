from flask import *
from algorithm import run_algorithm

# initialise Flask as app
app = Flask(__name__)

@app.route('/', method=["GET"])
def _input():
    _input_question = str(request.args.get("/"))

    # run the algorithm.py file
    run_algorithm()

    # here is what is going to be in the JSON file that can requested via the API
    input_data_set = {
        "qu": _input_question,
        "an": "",
    }
    # turn input_data_set into JSON
    json_dump = json.dump(input_data_set)

    # return the JSON file
    return json_dump
