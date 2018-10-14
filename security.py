from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt import JWT

def authenticate(username, password):
	user = UserModel.find_by_username(username)
	if user and safe_str_cmp(user.password,password): 
		return user

def identity(payload):
	user_id = payload['identity']
	return UserModel.find_by_id(user_id)

# @jwt.auth_response_handler
# def customized_response_handler(access_token, identity):
#  return jsonify({'access_token':access_token.decode('utf-8'),'user_id': identity.id})