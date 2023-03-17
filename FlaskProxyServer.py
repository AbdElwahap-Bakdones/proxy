from flask import Flask, request, jsonify
# import requests

app = Flask(__name__)
app.config['SERVER_NAME'] = 'proxyMessage.com'


@app.route('/', methods=['POST', 'GET'])
def process_request():
    print(request.headers)
    # Check if the request is coming from a specific domain
    # if request.headers.get('Origin') != 'http://example.com':
    #     return jsonify({'error': 'Invalid request origin'}), 403

    # url = 'http://example.com/api'
    # headers = {'Content-Type': 'application/json'}
    # data = request.get_json()
    # response = requests.post(url, headers=headers, json=data)
    # return jsonify(response.json())

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    print('start')
    app.run()
