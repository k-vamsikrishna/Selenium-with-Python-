temp = int(input("What is the temperature outside ?"))

if not (temp > 30 or temp == 30):
    print("Summer is started!")

elif not (temp < 30 or temp == 30):
    print("Winter is started")

else:
    print("Raining")

