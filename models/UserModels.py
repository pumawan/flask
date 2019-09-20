import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from config.koneksi import db,ma


class User(db.Model):
    __table_args__ = {"schema":"public"}
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username,email):
        self.username = username
        self.email = email

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','username','email')


