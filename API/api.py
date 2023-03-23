from flask import *
from algorithm import run_algorithm

# initialise Flask as app
app = Flask(__name__)

@app.route('/', methods=["GET"])
def _input():
    # initialise the question input and where the final quote is going
    _input_question = str(request.args.get("/"))
    final_quote = ""

    # run the algorithm.py file
    run_algorithm(_input_question, final_quote)

    # here is what is going to be in the JSON file that can requested via the API
    input_data_set = {
        "qu": _input_question,
        "an": final_quote,
    }
    # turn input_data_set into JSON
    json_dump = json.dumps(input_data_set)

    # return the JSON file
    return json_dump

if __name__ == "__main__":
    app.run(port=7777)
