from flask import Flask
from DB import db_wrapper

app = Flask(__name__)
app.config["DEBUG"] = True

db_wrap = db_wrapper.DBWrapper()
db_wrap.connect_to(app)


@app.route("/")
def hello():
    return "OMG!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)
