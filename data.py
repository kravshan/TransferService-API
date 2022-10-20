from flask_restful import reqparse

#Accounts model
accounts = {}
account_put_args = reqparse.RequestParser()
account_put_args.add_argument("account_number", type=str, help="Account number is required", nullable=False)
account_put_args.add_argument("balance", type=float, help="Balance is required", nullable=False)

account_update_args = reqparse.RequestParser()
account_update_args.add_argument("balance", type=float, help="Balance is required")

#Transactions model
transactions = {}
transaction_put_args = reqparse.RequestParser()
transaction_put_args.add_argument("src_account_number", type=str, help="Source account number is required", nullable=False)
transaction_put_args.add_argument("dest_account_number", type=str, help="Destination account number is required", nullable=False)
transaction_put_args.add_argument("amount", type=float, help="Amount is required", nullable=False)