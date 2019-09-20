import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from config.koneksi import db
from models import UserModels

if __name__ == '__main__':
    db.create_all()
    db.session.close()
    db.session.commit()
    db.session.remove()  