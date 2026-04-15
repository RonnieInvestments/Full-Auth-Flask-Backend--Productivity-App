from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return{
        "message":"Welcome to our journal entry platform"
    }

@app.route("/entries", methods=["GET"])
def get_journal_entries():
    pass

@app.route("/entries", methods=["POST"])
def add_journal_entry():
    pass

@app.route("/entry/<int:id>", methods=["PATCH"])
def update_journal_entry():
    pass

@app.route("/entry/<int:id>", methods=["GET"])
def delete_journal_entry():
    pass