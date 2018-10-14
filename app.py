from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.secret_key = 'rufa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
api = Api(app)
jwt = JWT(app, authenticate, identity)


# @jwt.auth_response_handler
# def customized_response_handler(access_token, identity):
#  return {'access_token':access_token.decode('utf-8'),'user_id': identity.id}

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)