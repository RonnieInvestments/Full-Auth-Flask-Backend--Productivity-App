from flask import Flask, jsonify, request, make_response
from flask_bcrypt import bcrypt
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

    #entries = JournalEntry.query.all()

    #entries_dict = journal_schema.dump(entries, many=True)

    #Pagination
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    pagination = JournalEntry.query.paginate(
        page=page, 
        per_page=per_page, 
        error_out=False
    )

    entries = pagination.items
    
    return make_response({
        "page": pagination.page,
        "per_page": pagination.per_page,
        "total": pagination.total,
        "total_pages": pagination.pages,
        "items": [JournalEntrySchema().dump(r) for r in entries]
    }), 200


    #return make_response(entries_dict, 200)


@app.route("/entries", methods=["POST"])
def add_journal_entry():

    try:
        incoming_data = journal_schema.load(request.get_json(), many=True)

        db.session.add_all(incoming_data)
        db.session.commit()

        #Serializing
        incoming_data_dict = journal_schema.dump(request.get_json(), many=True)
        return make_response(incoming_data_dict, 201)
    
    except ValidationError as e:
        return make_response({"message":"Could not load the data"})


@app.route("/entry/<int:id>", methods=["PATCH"])
def update_journal_entry(id):

    try:
        #Deserialize
        incoming_data = journal_schema.load(request.get_json(), many=False)

        entry = journal_schema.query.filter_by(id).first()

        if not entry:
            return make_response({"message":f"Entry {id} not found in the database."}, 404)
        
        entry.title = incoming_data["title"]
        entry.content = incoming_data["content"]

        db.session.commit()

        return make_response({"message":"Entry updated successfully"}, 201)
    
    except Exception as e:
        return make_response({"error":f"Could not update data {e}"}, 404)
    

@app.route("/entry/<int:id>", methods=["GET"])
def delete_journal_entry(id):
    
    try:
        entry = journal_schema.query.filter_by(id).first()

        if not entry:
            return make_response({"message":f"Entry {id} not found in the database."}, 404)
        
        #Delete if found
        db.session.delete(id)
        db.session.commit()

        return make_response({}, 201)
    
    except Exception as e:
        return make_response({"error":f"Could not delete entry {e}"}, 404)

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
    

if __name__=="__main__":
    app.run(debug=True)
