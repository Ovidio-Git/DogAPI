import datetime
import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:1989@db/pets"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)

class Dogs(db.Model):
    
    id_dog =db.Column(db.Integer,primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    picture = db.Column(db.String(100))
    is_adopted = db.Column(db.Boolean,default=1,nullable=False )
    created_date = db.Column(db.DateTime,nullable=False)


    def __init__(self, id_dog, name, picture, is_adopted, created_date):
        self.id_dog  = id_dog
        self.name    = name
        self.picture = picture
        self.is_adopted   = is_adopted
        self.created_date = created_date

db.create_all()


@app.route("/")
def home():
    return "Bienvenido al inicio amigo mio"


@app.route("/api/dogs/", methods=['POST'])
def create_dog():
    data   = request.get_json()
    id_dog = data['id_dog']
    name   = data['name']
    is_adopted = data['is_adopted']
    # Query picture from external API
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    if response.status_code == 200:
        things  = response.json()
        picture = things['message']
    else:
        print("Query to external API Error")
    add = Dogs(
        id_dog=id_dog, 
        name=name,
        picture=picture, 
        is_adopted=is_adopted,
        created_date=datetime.datetime.now())
    db.session.add(add)
    db.session.commit()
    return '200 OK [Information receive]'


# @app.route("/api/dogs")
# def index():
#     return jsonify(Dogs)

# @app.route("/api/dogs")
# def index():
#     response = []
#     for dog in Dogs.select():
#         response.append( UserResponseModel(
#         id = dog.id,
#         name = dog.name,
#         picture = dog.picture,
#         is_adopted=dog.is_adopted,
#         created_date=dog.created_date))
#     return response

# 
if __name__ == '__main__':
    print("****Listo*****")
    app.run()
    
