def account_number_validation(account_number_from_user):
    if account_number_from_user:
        try:
            int(account_number_from_user)
            if len(str(account_number_from_user)) == 10:
                return True
            else:
                # print("Error! Account number must be 10 digits")
                return False
        except ValueError:
            # print("Invalid Entry. Account number should only contain digits")
            return False
        except TypeError:
            # print("Invalid Entry. Account number should only contain digits")
            return False
    else:
        # print("Error! Account number field can not be empty.")
        return False


def amount_validation(amount_to_deposit):
    if amount_to_deposit:
        try:
            int(amount_to_deposit)
            if len(str(amount_to_deposit)) > 0:
                return True
        except ValueError:
            # print("Invalid Entry. Amount to be deposited should only contain digits")
            return False
        except TypeError:
            # print("Invalid Entry. Amount to be deposited should only contain digits")
            return False
    else:
        # print("Error! You have not entered any amount.")
        return False

# def initialise_entry(have_account):
#     try:
#         int(have_account)
#         if len(str(have_account)) == 0:
#             return False
#     except ValueError:
#         # print("Invalid Entry. Amount to be deposited should only contain digits")
#         return False
#     except TypeError:
#         # print("Invalid Entry. Amount to be deposited should only contain digits")
#         return False
#     finally:
#         # print("Error! You have not entered any amount.")
#         return True