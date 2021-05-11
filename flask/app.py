from flask import Flask

app = Flask(__name__)

# POST - used to receive data
# GET - used to send back data

# We are going to create below endpoints for the app.

    # POST /store data: {name:}
    # GET /store/<string:name>
    # GET /store
    # POST /store/<string:name>/item {name:, price:}
    # GET /store/<string:name>/item


# POST /store data: {name:}
@app.route('/store', methods:['POST'])
def create_store():
    pass
# GET /store/<string:name>
# GET /store
# POST /store/<string:name>/item {name:, price:}
# GET /store/<string:name>/item
@app.route('/', methods=['GET'])
def home():
    return 'Hello world'

@app.route('/', methods=['POST'])

app.run(port=1000, debug=True)