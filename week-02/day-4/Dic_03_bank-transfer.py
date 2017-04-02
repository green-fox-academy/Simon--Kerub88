# Create function that returns the name and balance of cash on an account

# Create function that transfers an balance of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - balance
#
# Print "404 - account not found" if any of the account numbers don't exist

accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

def bank_user_database(accounts):
    clients = ""
    for i in accounts:
        clients += i["client_name"] + " " + str(i["balance"]) + " " "\n"
    return clients



print(bank_user_database(accounts))

# /////////////////////////////////////////////////////////////////////////////

def bank_transfer(from_acc,to_acc, transfer):
    accounts_rewrite = []

    for bank_user in accounts:
        # if bank_user["client_name"] != accounts[0]["client_name"] or bank_user["client_name"] != accounts[1]["client_name"] or bank_user["client_name"] != accounts[2]["client_name"]:
        #     print("404 - account not found")
        if bank_user["client_name"] == from_acc:
            bank_user["balance"] = bank_user["balance"] - transfer
            accounts_rewrite.append(bank_user)
        elif bank_user["client_name"] == to_acc:
            bank_user["balance"] = bank_user["balance"] + transfer
            accounts_rewrite.append(bank_user)
        else:
            accounts_rewrite.append(bank_user)

    return accounts_rewrite

print(bank_transfer(accounts[1]["client_name"], accounts[2]["client_name"], 1000000000))
