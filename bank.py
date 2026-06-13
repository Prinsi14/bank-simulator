accounts = {}

def create_account():
    name = input("Enter your name: ")

    account_id = name.lower().replace(" ", "_")

    if account_id in accounts:
        print("Account already exists!")
        return 

    balance = float(input("Enter initial deposit amount: "))

    accounts[account_id] = { 
        "name": name,
        "balance": balance,
        "transactions": []
    }  

    print("Account created successfully!")
    print("Your account id is:", account_id)


create_account()



