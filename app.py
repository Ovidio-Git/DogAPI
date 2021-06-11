import datetime
import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# configuration sqlalchemy for mysql
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:1989@db/pets"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# key used to encrypt your cookies and save send them to the browser 
app.config['SECRET_KEY'] = 'T800' 
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



# CREATE ITEM PER NAME
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
    return '200 OK CREATE'


# READ ALL ITEMS
@app.route('/api/dogs/')
def read_all():
    response = []
    for Query in Dogs.query.all():
        Data = {
            'id_dog': Query.id_dog, 
            'name': Query.name, 
            'picture': Query.picture, 
            'is_adopted':Query.is_adopted, 
            'create_date':Query.created_date
            }
        response.append(Data)
    return jsonify(response)   


# READ ITEMS PER NAMES
@app.route('/api/dogs/<dname>',)
def read_names(dname):
    Query = Dogs.query.filter_by(name=dname).first_or_404()
    Data = {
        'id_dog': Query.id_dog, 
        'name': Query.name, 
        'picture': Query.picture, 
        'is_adopted':Query.is_adopted, 
        'create_date':Query.created_date
        }
    return jsonify(Data)


# READ ITEMS PER IS_ADOPTED
@app.route('/api/dogs/is_adopted',)
def read_is_adopted():
    response = []
    for Query in Dogs.query.filter_by(is_adopted=True).all():
        Data = {
            'id_dog': Query.id_dog, 
            'name': Query.name, 
            'picture': Query.picture, 
            'is_adopted':Query.is_adopted, 
            'create_date':Query.created_date
            }
        response.append(Data)
    return jsonify(response)  


# UPDATE ITEM PER NAME   
@app.route('/api/dogs/<dname>', methods=['PUT'])
def update_dog(dname):
    data   = request.get_json()
    id_dog = data['id_dog']
    name   = data['name']
    is_adopted = data['is_adopted']
    # Query picture from external API
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    things  = response.json()
    picture = things['message']


    Query = Dogs.query.filter_by(name=dname).first_or_404()
    Query.id_dog = id_dog
    Query.name = name
    Query.picture = picture
    Query.is_adopted = is_adopted
    Query.create_date = datetime.datetime.now()
    db.session.commit()
    
    return "200 OK UPDATE"


# DELETE ITEM PER NAME
@app.route('/api/dogs/<dname>', methods=['DELETE'])
def delete_dog(dname):
    Query = Dogs.query.filter_by(name=dname).first()
    db.session.delete(Query)
    db.session.commit()
    return '200 OK DELETE'



if __name__ == '__main__':
    app.run()
    
