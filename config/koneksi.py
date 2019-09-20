from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:cahyaneramawisnu@localhost/cobadb'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)