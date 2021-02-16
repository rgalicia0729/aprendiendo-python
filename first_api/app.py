from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'id': 1,
        'name': 'My wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 9.99
            }
        ]
    }
]


@app.route('/store')
def get_stores():
    # GET /store
    return jsonify({'stores': stores})


@app.route('/store/<string:storeId>')
def get_store_by_id(storeId):
    # GET /store/<string:storeId>
    for store in stores:
        if store['id'] == int(storeId):
            return jsonify(store)

    return jsonify({'ok': False, 'message': 'Store not found'})


@app.route('/store', methods=['POST'])
def create_store():
    # POST /store
    body = request.get_json()

    new_store = {
        'id': body['id'],
        'name': body['name'],
        'items': body['items']
    }

    stores.append(new_store)

    return jsonify(new_store)


app.run(port=5000)
