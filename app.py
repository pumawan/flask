from config.koneksi import *
from controller.UserControllers import *

api.add_resource(UserController, '/user')

if __name__ == '__main__':
    app.run(debug=True,port=9000,host="localhost")

