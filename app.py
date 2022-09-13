from flask import *
from housing.logger import logging
app = Flask(__name__)

@app.route("/")
def home():
    try:
        logging.info("we are under testing phase")
        return "Hello world"
    except:
        return "Server not responding"

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
    # app.run(debug=True)

