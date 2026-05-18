balance = 10000
withdraw = 10001

if balance > 0:
    if withdraw <= balance:
        print("Transaction Successful")

    else: 
        print("Transaction Failed")