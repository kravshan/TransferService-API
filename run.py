import requests

BASE_URL = "http://127.0.0.1:5000/"

acc_no_1 = 123456788
response = requests.put(BASE_URL + "account/" + str(acc_no_1), {"account_number": str(acc_no_1), "balance": 12000})
print(response.json())

acc_no_2 = 987654321
response = requests.put(BASE_URL + "account/" + str(acc_no_2), {"account_number": str(acc_no_2), "balance": 10500})
print(response.json())

acc_no_3 = 543216789
response = requests.put(BASE_URL + "account/" + str(acc_no_3), {"account_number": str(acc_no_3), "balance": 15200})
print(response.json())

def run_transaction(transaction_id, src_account_number, dest_account_number, amount):
    src = requests.get(BASE_URL + "account/" + str(src_account_number)).json()
    print(src)
    dest = requests.get(BASE_URL + "account/" + str(dest_account_number)).json()
    print(dest)

    src_balance = float(src['balance']) - amount
    dest_balance = float(dest['balance']) + amount

    src_response =  requests.patch(BASE_URL + "account/" + str(src_account_number), {"balance": src_balance})
    print(src_response.json())

    dest_response = requests.patch(BASE_URL + "account/" + str(dest_account_number), {"balance": dest_balance})
    print(dest_response.json())

    response = requests.put(BASE_URL + "transaction/" + str(transaction_id), {"src_account_number": src_account_number, "dest_account_number": dest_account_number, "amount": amount})
    print(response.json())

#remember to change the transaction id each time you run the run_transaction method
#otherwise previous transactions will get overridden
run_transaction(3, acc_no_3, acc_no_1, 500.0)
