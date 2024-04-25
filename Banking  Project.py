
def login(username, password):
    data1 = {"username": "ziyad@123", "password": "5555"}
    if data1["username"] == username:
        if data1["password"] == password:
            print("logined sucessfully")

            class Bankaccount:
                def __init__(self, balance=0):
                    self.balance = balance
                    print("Hello!")

                def deposite(self, deposite_amount):
                    print("deposited amount is", deposite_amount)
                    self.balance = self.balance + deposite_amount
                    print("your current account balance = ", self.balance)

                def withdrawal(self, withdrawal_amount):
                    if withdrawal_amount > self.balance:
                        print("insufficient fund")
                    else:
                        print("withdrawal amount is", withdrawal_amount)
                        self.balance = self.balance - withdrawal_amount
                        print("your current account balance = ", self.balance)

                def balance_enquiry(self):
                    print("Your Account Balance=", self.balance)

            obj1 = Bankaccount()
            userinput = int(input("Press 1 For Balance enquiry \nPress 2 For Deposit  \nPress 3 For Withdrawal\n"))
            if userinput == 1:
                obj1.balance_enquiry()
            elif userinput == 2:
                obj1.deposite(int(input("Enter the amount for deposite=")))
            elif userinput == 3:
                obj1.withdrawal(int(input("Enter the amount for withdrawal")))
            else:
                print("Please enter a valid number")


        else:
            print("Please enter correct password")
    else:
        print("invalid username")


username = input("Enter the username =")
password = input("Enter the password =")
login(username, password)


