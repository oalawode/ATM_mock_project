# create record
# update record
# read record
# delete record
# CURD

import os
import validate
user_db_path = "data/userRecord/"


def create(user_account_number, first_name, last_name, email, password, opening_balance):
    # create a file
    # name of file is account number .txt
    # add the user details to the file
    # return true
    # if saving to the file fails, then delete created file

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(opening_balance)

    if does_account_number_exist(user_account_number):
        return False

    if does_email_exist(email):
        print("User already exists")
        return False

    completion_state = False

    try:

        f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:
        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)
    else:

        f.write(str(user_data));
        completion_state = True

    finally:

        f.close();
        return completion_state


def update(user_account_number):
    print("Update user record")


def read(user_account_number):
    # find user record using account number
    #  fetch content of the file

    is_valid_account_number = validate.account_number_validation(user_account_number)

    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:

        print("User not found!")
    except TypeError:

        print("Invalid Account Number format.")

    else:
        return f.readline()

    return False


def delete(user_account_number):
    # find user record using account number
    # delete the user record
    # return true

    print("Delete user record")
    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print("User not found")
    return is_delete_successful

def find(user_account_number):
    print("Find user record")


def does_email_exist(email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = (str.split(read(user), ","))
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        if user == str(account_number) + ".txt":
            return True
    return False


def authenticate_user(account_number, password):

    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ",")
        if password == user[3]:
            return user

    return False

def current_balance(user):
    current_balance = user[4]
    return current_balance



def set_current_balance(user, account_balance):
    user[4] = account_balance