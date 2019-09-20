import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from config.koneksi import *
from flask_restful import Resource
from models.UserModels import User,UserSchema

class UserController(Resource):

    def __init__(self):
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    def get(self):
        users =  User.query.all()
        results = self.users_schema.dump(users)
        return results

    def post(self):
        username = request.form.get('username')
        email = request.form.get('email')
        user_baru = User(username,email)
        db.session.add(user_baru)
        db.session.commit()
        return self.user_schema.dump(user_baru)

    def put(self):
        id = request.form.get('id')
        username = request.form.get('username')
        email = request.form.get('email')
        userupdate = User.query.filter_by(id=int(id)).first()
        if userid is not None:
            if username:
                userid.username = username
            if email:
                userid.email = email
            db.session.commit()
            return self.user_schema.dump(userupdate)

    def delete(self):
        id = request.form.get('id')
        userhapus = User.query.filter_by(id=int(id)).first()    
        if userhapus is not None:
            db.session.delete(userhapus)
            db.session.commit()
            return self.user_schema.dump(userhapus)