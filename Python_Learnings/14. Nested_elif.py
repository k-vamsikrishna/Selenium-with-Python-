salary = 45000
credit_score = 720

if salary >= 100000:
    print("Premium Loan")

elif salary >= 40000:

    if credit_score >= 750:
        print("Loan Approved")

    elif credit_score >= 650:
        print("Loan Under Verification")

    else:
        print("Loan Rejected")

else:
    print("Salary Not Eligible")