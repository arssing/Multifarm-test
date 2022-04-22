from flask import Flask
from utils import get_APR

app = Flask(__name__)

@app.route("/")
def index():
    try:
        apr = get_APR()
        return {"apr":apr}
    except:
        return {"apr":"something went wrong"}

if __name__ == "__main__":
    app.run()