# TransferService-API
Simple and to the point implementation of a Transfer Service API.

How to use:
First, run the api.py file in order to activate the local  host server on http://127.0.0.1:5000/. 
Then, edit the run_transaction() method in the run.py file giving a suitable transfer_id value, source account number, destination account number and the amount to transfer.
Finally, run  the run.py file to get the expected rsults.

Requirements are completed as follows:
1. The implementation of a TransferService API is given here.
2. No user interface is created.
3. API accepts source account number, destination account number and the amount to transfer. It does return an appropriate response.
4. Data is saved in-memory in two python dictionaries called "accounts" and "transactions". No database is used.
5. The framework of choice is Flask for creating the API.
6. Authentication is not done.
7. The run.py file can run as many tests are necessary by giving different source account numbers, destination account numbers and the amounts to transfer.
8. The failsafe.py file has necessary methods to avoid the server from crashing at all times.

The data models are in the data.py file. It contains a simple model for creating and updating an account, and a simple implementation for only creating a transaction.

The api_resources.py file contains the reorce files that are required to run the API in Flask framework.

The system does have the capability to create an account, update an account and read an account. Deleting an account is not a requirement.
The system also has the capability to create a transaction and read a transaction. Updating and deleting a transaction are not requirements.
