from flask import Flask
from flask_restful import Api

import api_resources

app = Flask(__name__)
api = Api(app)

api.add_resource(api_resources.Account, "/account/<string:account_number>")
api.add_resource(api_resources.Transaction, "/transaction/<int:transaction_id>")

if __name__ =="__main__":
    app.run(debug=True)
