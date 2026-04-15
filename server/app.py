from flask import Flask, jsonify, request, bcrypt
from models import *
from flask_jwt_extended import create_access_token,  JWTManager, jwt_required
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///entries.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app=app)

migrate = Migrate(app, db)

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

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print('Received data:', username , password)

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'Login Success', 'access_token': access_token})
    else:
        return jsonify({'message': 'Login Failed'}), 401