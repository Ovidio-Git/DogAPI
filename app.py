import datetime
import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:1989@localhost/pets"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)

class Dogs(db.Model):
    __tablename__ = 'dogs'
    id_dog =db.Column(db.Integer,primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    picture = db.Column(db.String(100))
    is_adopted = db.Column(db.Boolean,default=1,nullable=False )
    created_date = db.Column(db.DateTime,default=datetime.datetime.now, nullable=False)

    def __repr__(self):
        return '<Dog %r>' % self.name #show data value not id value



@app.route("/")
def home():

    print("Listo1")
    return "hola prro"


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
    add = Dogs(id_dog=id_dog, name=name,picture=picture, is_adopted=is_adopted)
    db.session.add(add)
    db.session.commit()
    return 'OK 200 [Information receive]'


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
if __name__=='__main__':
    db.create_all()
    print("****Listo*****")
    app.run()