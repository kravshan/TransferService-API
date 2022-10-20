from flask_restful import abort
from data import accounts, transactions

def abort_if_account_id_does_not_exist(id):
    if id not in accounts:
        abort(404, message="Account ID is not available")
    
def abort_if_transaction_id_does_not_exist(id):
    if id not in transactions:
        abort(404, message="Transaction ID is not available")

def abort_if_account_id_already_exists(id):
    if id in accounts:
        abort(404, message="Account is already available with that ID")

def abort_if_transaction_id_already_exists(id):
    if id in transactions:
        abort(404, message="Transaction is already available with that ID")