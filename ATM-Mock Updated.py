import datetime
import random
import database
import validate
from getpass import getpass

def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do yo have an account number with us? 1. (Yes) 2. (No) 3. (Exit) \n"))
    
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    elif have_account == 3:
        print("Thank you for banking with us.")
        exit()
    else:
        print("Invalid Selection. Please try again")
        init()


def login():
    print("****** Login ******")

    account_number_from_user = input("Please enter your account number. \n")

    is_valid_account_number = validate.account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = getpass("Please enter your password. \n")

        user = database.authenticate_user(account_number_from_user, password)

        if user:
            bank_operations(user)

        print("Invalid account or password")
        login()
    else:
        print("Account number invalid")
        print("Account should be only digits and 10 digits long.")
        init()


def register():
    print("****** Register ******")

    email = input("Please enter your email address. \n")
    first_name = input("Please enter your First name. \n")
    last_name = input("Please enter your Last name. \n")
    password = input("Create your password. \n")
    opening_balance = int(input("How much do you want to deposit as your opening balance? \n"))

    account_number = generate_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password, opening_balance)

    if is_user_created:

        print("Your account has been created")
        print("==== ==== ==== ===== ====")
        print("==== ==== ==== ===== ====")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep this safe")
        print("Your current balance is: %s" % opening_balance)
        print("==== ==== ==== ===== ====")
        login()
    else:
        print("Something went wrong. Please try again.")
        register()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def bank_operations(user):
    print("Welcome %s %s " % (user[0], user[1]))

    datetime.datetime.now()

    selected_option = int(input("What would you like to do? 1. Deposit 2. Withdrawal 3. Logout 4. Exit \n"))

    if selected_option == 1:
        deposit_operation(user)
    elif selected_option == 2:
        withdrawal_operation(user)
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        print("Thank you for banking with us.")
        exit()
    else:
        print("Invalid Selection")
        bank_operations(user)


def deposit_operation(user):
    
    account_balance = float(database.current_balance(user))

    amount_to_deposit = input("How much would you like to deposit? \n")

    is_valid_amount = validate.amount_validation(amount_to_deposit)

    if is_valid_amount:
        account_balance += float(amount_to_deposit)
        print('Your new balance is %s' % account_balance)
        next_operation()

    else:       
        print('*****************************************************************')
        print('Invalid entry. Amount to be deposited should only contain digits.')
        print('                                                                 ')
        deposit_operation(user)
    
 

def withdrawal_operation(user):

    account_balance = float(database.current_balance(user))

    amount_to_withdraw = input('How much would you like to withdraw? \n')

    is_valid_amount = validate.amount_validation(amount_to_withdraw)

    if is_valid_amount:
        if amount_to_withdraw < account_balance:
            print('Take your cash')
            account_balance -= amount_to_withdraw
            print('Your new Account Balance: %f' % account_balance)
            next_operation()
        else:
            print('Insufficient Funds.')
    else:       
        print('*****************************************************************')
        print('Invalid entry. Amount to be withdrawn should only contain digits.')
        print('                                                                 ')
        withdrawal_operation(user)
    
    database.set_current_balance(user, account_balance)

def logout():
    login()


def next_operation():
    next_action = int(input('Do you wish to perform more operations? 1. Yes 2. No \n'))
    if next_action == 1:
        login()
    elif next_action == 2:
        print("Thank yo for banking with us.")
        exit()
    else:
        print("Invalid Selection. Please try again")
        next_operation()


init()
