
class Bank:
    def __init__(self) -> None:
        self.total_balance=0
        self.total_loan_balance=0
        self.accounts={}
        self.admin={}
        self.loan_enable=True
        self.account_num_count=10000

    def create_account(self,name,email,address,account_type):
        self.account_num_count +=1
        account_num=self.account_num_count
        self.accounts[account_num]={
            'name' : name,
            'email': email,
            'address': address,
            'account_type':account_type,
            'balance': 0,
            'loan_count': 0,
            'transactions':[]
        }

        print(f'Account created successfuly and Account Number {account_num}')

    def delete_account(self,account_num):
        if account_num in self.accounts:
            del self.accounts[account_num]
            print(f'Account deleted successfully and account number was {account_num}')

        else:
            print("Account number is Invalid.And Number does not exists..!")


    def show_all_accounts(self):
        print("<------------------------------ALL ACCOUNT LIST------------------------------>")
        for value ,key in self.accounts.items():
            print(f" Name: {key['name']}, Email: {key['email']}, Address: {key['address']}, Account Number: {value}")

        
    def total_available_balance(self):
        print(f'Total balance in the Bank : {self.total_balance} Taka')

    def total_loan(self):
        print(f'Total loan in the bank : {self.total_loan_balance} Taka')


    def create_admin_account(self,userName,password):
        self.admin[userName]=password
        print("Admin login successfully...")

    def loan_features(self):
        self.loan_enable = not self.loan_enable
        
        if self.loan_enable:
            status = 'Enable'
        else:
            status = 'Disabled' 
        print(f'Loan features has been {status}')




class User:
    def __init__(self,bank,account_num) -> None:
        self.bank=bank
        self.account_num=account_num

    def deposit(self,amount):
        if amount > 0:
            self.bank.accounts[self.account_num]['balance'] +=amount
            self.bank.total_balance +=amount
            self.bank.accounts[self.account_num]['transactions'].append(f'Deposited -> {amount}') 
            print(f'Deposit {amount} taka successfully..')

        else:
            print("Deposit amount greater then zero..!")      
        
    def withdraw(self,amount):
        if self.bank.accounts[self.account_num]['balance'] >= amount:
            self.bank.accounts[self.account_num]['balance'] -=amount
            self.bank.total_balance -=amount
            self.bank.accounts[self.account_num]['transactions'].append(f'Withdraw -> {amount}')
            print(f'Withdraw amount {amount} taka successfully..')

        else:
            print("Withdrawal amount exceeded")

    def check_balance(self):
        print(f'Your account balance :{self.bank.accounts[self.account_num]['balance']} Taka')


    def check_transactions(self):
        print("<----------------------All TRANSACTIONS HISTORY-------------------------->")
        for transaction in self.bank.accounts[self.account_num]['transactions']:
            print(transaction)

    
    def take_loan(self,amount):
        if self.bank.loan_enable and self.bank.accounts[self.account_num]['loan_count'] < 2:
            self.bank.accounts[self.account_num]['balance'] +=amount  
            self.bank.total_loan_balance +=amount
            self.bank.accounts[self.account_num]['loan_count'] += 1
            self.bank.accounts[self.account_num]['transactions'].append(f'Loan taken -> {amount}')
            print(f'Loan granted successfully {amount} taka')

        else:
            print("Sorry your account not elligible for loan")

    
    def transfer(self, recipient_account_number, amount):
        if recipient_account_number in self.bank.accounts:
            if self.bank.accounts[self.account_num]['balance'] >= amount:
                self.bank.accounts[self.account_num]['balance'] -= amount
                self.bank.accounts[self.account_num]['transactions'].append(f"Transferred: {amount} taka to Account {recipient_account_number}")
                self.bank.accounts[recipient_account_number]['balance'] += amount
                self.bank.accounts[recipient_account_number]['transactions'].append(f"Received: {amount} taka from Account {self.account_num}")
                print("Balance transferred successfully")
            else:
                print("Insufficient balance to transfer")
        else:
            print("account number does not exist")



class Admin:
    def __init__(self,bank,userName,password) -> None:
        self.bank=bank
        self.userName=userName
        self.password=password


    def create_user_account(self,name,email,address,account_type):
        self.bank.create_account(name,email,address,account_type)

    def delete_user_account(self,account_num):
        self.bank.delete_account(account_num)


    def show_user_account(self):
        self.bank.show_all_accounts()

    def total_bank_balance(self):
        self.bank.total_available_balance()

    def total_bank_loan(self):
        self.bank.total_loan()

    def loan_feature(self):
        self.bank.loan_features()



    
        
bank = Bank()
admin=Admin(bank,"admin","password")

def Admin_menu():
    userName = input('Enter Your userName : ')
    password =input("Enter Your password: ")
    if userName =="admin" and password =="password":
         while True:
                print("\n..........Admin Menu..........")
                print("1. Create User Account")
                print("2. Delete User Account")
                print("3. Show All User Accounts")
                print("4. Total Available Balance")
                print("5. Total Loan Amount")
                print("6. Loan Feature On or Off")
                print("7. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    name = input("Enter user's name: ")
                    email = input("Enter user's email: ")
                    address = input("Enter user's address: ")
                    account_type = input("Enter user's account type (Savings/Current): ")
                    admin.create_user_account(name, email, address, account_type)
                elif choice == 2:
                    account_number = int(input("Enter account number to delete: "))
                    admin.delete_user_account(account_number)
                elif choice == 3:
                    admin.show_user_account()
                elif choice == 4:
                    admin.total_bank_balance()
                elif choice == 5:
                    admin.total_bank_loan()
                elif choice == 6:
                    admin.loan_feature()
                elif choice == 7:
                    print("Logged out from admin account")
                    break
                else:
                    print("Invalid choice. Please try again")
    else:
        print("Invalid username or password.")



def User_menu():

    while True:
        print("\n.......User Menu........")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Check Transaction History")
        print("6. Take Loan")
        print("7. Transfer")
        print("8. Exit")

        user_option = int(input("Enter your option: "))
        if user_option == 1:
            name = input("Enter Your name: ")
            email = input("Enter your Email: ")
            address = input("Enter your Address: ")
            account_type = input("Enter your Account_type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)
        elif user_option == 2:
            account_num = int(input("Enter your Account number: "))
            amount = int(input("Enter amount you want to deposit: "))
            if account_num in bank.accounts:
                user = User(bank, account_num)
                user.deposit(amount)
            else:
                print("Account does not exist.")
        elif user_option == 3:
            account_num = int(input("Enter your Account number: "))
            amount = int(input("Enter amount you want to withdraw: "))
            if account_num in bank.accounts:
                user = User(bank, account_num)
                user.withdraw(amount)
            else:
                print("Account does not exist.")
        elif user_option == 4:
            account_num = int(input("Enter your Account number: "))
            if account_num in bank.accounts:
                user = User(bank, account_num)
                user.check_balance()
            else:
                print("Account does not exist.")
        elif user_option == 5:
            account_num = int(input("Enter your Account number: "))
            if account_num in bank.accounts:
                user = User(bank, account_num)
                user.check_transactions()
            else:
                print("Account does not exist.")
        elif user_option == 6:
            account_num = int(input("Enter your Account number: "))
            amount = int(input("Enter loan amount: "))
            if account_num in bank.accounts:
                user = User(bank, account_num)
                user.take_loan(amount)
            else:
                print("Account does not exist.")
        elif user_option == 7:
            account_num = int(input("Enter your Account number: "))
            recipient_account_num = int(input("Enter recipient's Account number: "))
            amount = int(input("Enter amount you want to transfer: "))
            if account_num in bank.accounts:
                if recipient_account_num in bank.accounts:  
                    user = User(bank, account_num)
                    user.transfer(recipient_account_num, amount)
            else:
                print("One or both of the accounts do not exist.")
        elif user_option == 8:
            print("Logged out from user account")
            break
        else:
            print("Invalid option.")






while True:
    print("\n<-------------------WELCOME TO OUR BANK--------------------------->")
    print("1.Admin")
    print("2.User")
    print("3.Exit")

    option =input("Enter Your choice : ")
    if option =='1':
        Admin_menu()

    elif option =='2':
        User_menu()

    elif option =='3':
        break
    else:
        print("Invalid Option")
