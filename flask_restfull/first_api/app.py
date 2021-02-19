from flask import Flask
from flask_restful import Resource, Api, reqparse, request

products = []

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('name', type=str)


class Product(Resource):
    def get(self, productId):
        # Recurso para obtener los datos de un producto
        product = next(
            filter(lambda x: x['id'] == productId, products), None)

        return product, 200 if product is not None else 400

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


class Products(Resource):
    def get(self):
        # Recurso util para consultar todos los productos
        return products

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
