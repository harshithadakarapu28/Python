""" Question: Password Strength Validator
You are building a password validation module for a registration system. The system should accept only strong passwords based on the following rules
Password rules:
Must be at least 8 characters long.
Must not start with a digit.
Must contain at least one uppercase letter.
Must contain at least one lowercase letter.
Must contain at least one digit.
Must contain at least one special character from: @ # $ % & * !
 Task:
Write a function password(string) that:
Returns 1 if the password is strong (i.e., all rules are satisfied),
Returns 0 if the password is weak.
Then, based on the result:
Print "Password is strong" if it returns 1,
Print "Password is weak" otherwise."""

def password(string):
    digit = 0
    uppercase = 0
    lowercase = 0
    specialChar = 0
    special_chars = "@#$%&*!"
    if len(string) <= 4 or string[0].isdigit():
        return 0
    if len(string) >= 8:
        for i in string:
            if i.isupper(): 
                uppercase += 1
            elif i.islower():
                lowercase += 1
            elif i.isdigit():
                digit += 1
            elif i in special_chars:
                specialChar += 1

        if specialChar >= 1 and uppercase >= 1 and lowercase >= 1 and digit >= 1:
            return 1
        else:
            return 0
    else:
        return 0

string = input("Enter password: ")
if password(string):
    print("Password is strong ")
else:
    print("Password is weak ")
