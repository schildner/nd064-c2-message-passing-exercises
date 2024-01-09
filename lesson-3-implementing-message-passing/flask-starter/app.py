import json
from flask import Flask, jsonify, request

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computers():
    if request.method == 'GET':
        return Response(json.dumps(retrieve_orders()),
                        200,
                        {'Content-Type': 'application/json'})
    elif request.method == 'POST':
        request_body = request.json
        return Response(json.dumps(create_order(request_body)))
    else:
        raise Exception('Unsupported HTTP request type.')

if __name__ == '__main__':
    app.run()
