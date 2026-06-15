# Our accounts storage - starts empty
accounts = {
    "test_user":{
        "name": "Test User",
        "balance": 1000.0,
        "transactions": []
    }
}

def create_account():
    print("---- Create Account ----")
    
    # ask user for details
    name = input("Enter your name: ")
    
    # convert to account ID - lowercase, no spaces
    # example: "Prinsi Shah" becomes "prinsi_shah"
    account_id = name.lower().replace(" ", "_")
    
    # check if account already exists
    if account_id in accounts:
        print("Account already exists!")
        return        # stop the function here
    
    # ask for opening balance
    balance = float(input("Enter opening balance: "))
    
    # store in accounts dictionary
    accounts[account_id] = {
        "name"        : name,
        "balance"     : balance,
        "transactions": []
    }
    
    print("Account created successfully!")
    print("Your account ID is:", account_id)

def  deposit():
    print("---- Deposit----")
    account_id = input("enter your account ID: ")
    if account_id not in accounts:
        print("Account Not Found")
        return
    amount =float(input("Enter The Amount :"))
    accounts[account_id]["balance"]+= amount
    print("Deposit Succesfully")
    print("New Balance is :",accounts[account_id]["balance"])

def withdraw():
    print("----Withdraw----")
    account_id = input("enter your account ID: ")
    if account_id not in accounts:
        print("Accounts not Found")
        return
    amount = float(input("Enter The Amount :"))
    if amount > accounts[account_id]["balance"]:
        print("Insufficient Balance")
        return
    accounts[account_id]["balance"]-= amount
    print("Withdraw Succesfully")
    print("New Balance is:",accounts[account_id]["balance"])

def transfer():
    print("----Transfer----")

    from_id = input("enter your account id:")
    to_id = input("enter the recipient account id:")
    if from_id not in accounts:
        print("your account is not found!")
        return
    if to_id not in accounts:
        print("recipient account not found!")
        return
    if from_id == to_id:
        print("Cannot transfer to the same account!")
        return
    amount =float(input("Enter the amount to transfer:"))
    if amount > accounts[from_id]["balance"]:
        print("Insufficient balance!")
        return
    accounts[from_id]["balance"]-= amount
    accounts[to_id]["balance"]+= amount
    print("transfer succesfully!")
    print("your new balance is:",accounts[from_id]["balance"])

create_account()
deposit()
withdraw()
transfer()



    



