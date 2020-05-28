def menu():
    print("1. Balance Enquiry")
    print("2.Cash Withdrawal")
    print("3.Deposit")
    print("4. change your pin")
    print("5.Transfer money")
    print("6. quit")


print("Welcome")
# input("Select your language (English/Hindi)")
print("swipe your card")
transaction = [1, 2, 3, 4, 5, 6]

atm_pin = 1510
curr_balance = 2000
pin = int(input("Enter your 4-digit pin"))
if pin == atm_pin:
    while True:
        menu()
        choice = int(input("Choose your transaction"))
        if choice in transaction:
            if choice == 1:
                print("current balance:{}".format(curr_balance))
            elif choice == 2:
                required = int(input("Enter amount"))
                if required <= curr_balance:
                    x = input("Confirm your withdrawal(Yes/No):")
                    if x == "Yes":
                        print("Transaction is being processed")
                        print("Collect your cash")
                    else:
                        print("Transaction is cancelled")
                else:
                    print("Current balance is insufficient to meet your requirement")
            elif choice == 3:
                a = int(input("Enter amount:"))
                if a >= 0:
                    curr_balance += a
                    if input("Do you want to know your current balance (Yes/No):") == "Yes":
                        print("current balance:{}".format(curr_balance))
                    else:
                        pass
                else:
                    print("Invalid amount")
            elif choice == 4:
                if int(input("Enter current pin:")) == atm_pin:
                    new_atm_pin = int(input("Enter your new pin:"))
                    if new_atm_pin == int(input("confirm new pin")):
                        atm_pin = new_atm_pin
                        print("Your pin has been changed")
                    else:
                        print("not matched")
                else:
                    print("Invalid pin")
            elif choice == 5:
                b = int(input("Enter amount:"))
                if b < curr_balance:
                    print("Transaction successful")
                    curr_balance = curr_balance - b
                    if input("Do you want to know your current balance (Yes/No):") == "Yes":
                        print("current balance:{}".format(curr_balance))
                    else:
                        pass
                else:
                    print("Current balance is insufficient to meet your requirement")
            elif choice == 6:
                exit()
