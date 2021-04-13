import random
database = {}


def init():
    
    print("Welcome to bankPHP!")

   
    have_account = int(input("Do you have account with us: 1. Yes or 2. No \n"))

    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("You have selected invalid option!")
        init()


def login():
    print("********** Login **********")

    # is_login_successful = False

    # while is_login_successful == False:

    user_account_number = int(input("Enter your account number here? \n"))
    password = input("Enter your password? \n")

    for account_number, user_details in database.items():
        if account_number == user_account_number and user_details[3] == password:
            print(f"You are welcome, {user_details[0]} {user_details[1]}!")
            bank_operation()
    else:
        print('Invalid account or password!!')

    
def register():
    print("********** Register **********")

    email = input("What is your email address? \n")
    first_name = input("What is your firstname? \n")
    last_name = input("What is your lastname? \n")
    password = input("Create a password for yourself? \n")

    account_number = account_generator()

    user_details = [ first_name, last_name, email, password ]


    database[account_number] = user_details

    print("Your Account Has Been Created!")
    print("== === ===== ===== ===")
    print(f"Your account number is {account_number}")
    print("Make sure you keep it safe")
    print("== === ===== ===== ===")

    login()

def bank_operation():
    selected_option = int(input("What would you like to do?\n 1. Deposit \t 2. Withdrawal \t\n 3. Logout \t 4. Exit \n"))

    if selected_option == 1:
        deposit_operation(amount)

    elif selected_option == 2:
        withdrawal_operation(amount)

    elif selected_option == 3:
        login()
    
    elif selected_option == 4:
        exit()
    else:
        print("Invalid option selected!")
        bank_operation()

def withdrawal_operation(amount, balance = 10000):
    return f"You just withdrew the sum of ${amount} from your total balance ${balance:,.2f}."

def deposit_operation(amount, balance = 10000):
    balance += amount
    return f"You just deposited the sum of ${amount}, New balance = {balance:,.2f}."

def account_generator():
    print('A new account has been created for you!')
    return random.randrange(1111111110, 2223334445  )


# print(account_generator())
init()
