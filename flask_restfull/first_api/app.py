from flask import Flask
from flask_restful import Resource, Api, reqparse

products = []

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('name', type=str)


class Product(Resource):
    def get(self, productId):
        # Recurso para obtener los datos de un producto
        for product in products:
            if product['id'] == productId:
                return product

        return {'ok': False, 'message': 'No se encontró el producto'}, 404

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
        args = parser.parse_args()

        new_product = {
            'id': args.get('id'),
            'name': args.get('name')
        }

        products.append(new_product)

        return new_product, 201


# Resources
api.add_resource(Product, '/api/product/<int:productId>')
api.add_resource(Products, '/api/products')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
