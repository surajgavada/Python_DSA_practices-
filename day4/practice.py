def bank():
    psd = (2110)
    pwd = int(input("enter your password:"))
    if (pwd == psd):
        print ("choice your option:")
        print("1.balance")
        print("2.debit")
        print("3.credit")
    else:
        print("password is wrong!, pls enter correct pwd")
bank()