from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    #parser.add_argument()

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Store with name '{}' already exists".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occured when creating the store"}, 400

        return store.json(), 200

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'store': store.json()}, 200

        return {"message": "Store with name '{}' doesn't exists".format(name)}, 404

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}, 200

    def put(self):
        pass




class StoreList(Resource):

    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}, 200