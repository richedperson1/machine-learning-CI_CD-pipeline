from flask import *
from housing.logger import logging
from housing.exception import housingExeption

import sys
app = Flask(__name__)

@app.route("/")
def home():
    try:
        raise Exception("hello word")
        logging.info("we are under testing phase")
        return "Hello world"
    except  Exception as e:
        housing = housingExeption(e,sys)
        logging.info(housing.errorMessage)
    return "Server not responding"

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
    # app.run(debug=True)

