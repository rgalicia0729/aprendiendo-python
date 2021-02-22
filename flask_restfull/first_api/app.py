from flask import Flask
from flask_restful import Resource, Api, reqparse, request
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

products = []

app = Flask(__name__)
app.secret_key = 'RUBYhn10vjFXO94T5GbsqSkelzoDHZfQ'
api = Api(app)

jwt = JWT(app, authenticate, identity)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('name', type=str)


class Product(Resource):
    @jwt_required()
    def get(self, productId):
        # Recurso para obtener los datos de un producto
        product = next(
            filter(lambda x: x['id'] == productId, products), None)

        return product, 200 if product is not None else 400

    @jwt_required()
    def put(self, productId):
        # Recurso para actualizar los dato de un producto
        args = parser.parse_args()

        for i in range(len(products)):
            if products[i]['id'] == productId:
                new_product = {
                    'id': products[i]['id'],
                    'name': args.get('name')
                }
                products[i] = new_product

                return new_product, 201

        return {'ok': False, 'message': 'No se encontró el producto'}, 404

    @jwt_required()
    def delete(self, productId):
        # Recurso para eliminar un registro de un producto
        global products

        products = list(filter(lambda x: x['id'] != productId, products))
        return {'ok': True, 'message': 'Product deleted'}


class Products(Resource):
    @jwt_required()
    def get(self):
        # Recurso util para consultar todos los productos
        return products

    @jwt_required()
    def post(self):
        # Recurso para agregar un nuevo producto
        body = request.get_json()

        if next(filter(lambda x: x['id'] == int(body['id']), products), None):
            return {'ok': False, 'message': f"An product with id {body['id']} already exists"}, 400

        new_product = {
            'id': int(body['id']),
            'name': body['name']
        }

        products.append(new_product)

        return new_product, 201


# Resources
api.add_resource(Product, '/api/product/<int:productId>')
api.add_resource(Products, '/api/products')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
