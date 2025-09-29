# a=int(input("Enter any value between 5 and 9:"))


a = input("Enter any value between 5 and 9: ")

if a == "quit":
    print("OK")
else:
    try:
        num = int(a)
        if 5 <= num <= 9:
            print("OK")
        else:
            raise ValueError("Value should be between 5 and 9")
    except ValueError:
        raise ValueError("Value should be between 5 and 9")



class CustomError(Exception):
    pass

user_input = input("Enter 'yes' to continue: ")

if user_input != "yes":
    raise CustomError("You did not enter 'yes'. CustomError raised!")
else:
    print("Thank you! You may continue.")