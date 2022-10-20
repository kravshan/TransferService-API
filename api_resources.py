from flask_restful import Resource

import data
import failsafe

class Account(Resource):
    def get(self, account_number):
        failsafe.abort_if_account_id_does_not_exist(account_number)
        return data.accounts[account_number]

    def put(self, account_number):
        failsafe.abort_if_account_id_already_exists(account_number)
        args = data.account_put_args.parse_args()
        data.accounts[account_number] = args
        return data.accounts[account_number], 201

    def patch(self, account_number):
        args = data.account_update_args.parse_args()
        failsafe.abort_if_account_id_does_not_exist(account_number)
        data.accounts[account_number]['balance'] = args['balance']
        return data.accounts[account_number]

class Transaction(Resource):
    def get(self, transaction_id):
        failsafe.abort_if_transaction_id_does_not_exist(transaction_id)
        return data.transactions[transaction_id]

    def put(self, transaction_id):
        failsafe.abort_if_transaction_id_already_exists(transaction_id)
        args = data.transaction_put_args.parse_args()
        data.transactions[transaction_id] = args
        return data.transactions[transaction_id], 201