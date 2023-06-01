#!/usr/bin/python3

### LIBRARIES
import botocore
import boto3
import sys

### FUNCTIONS
# Function name: user_exists
# Purpose      : Verify if the user specified exists
# Arguments    : iam, username
# Return       : none   
def user_exists(iam, username):
    try:
        iam.get_user(UserName=username)
        return True
    except iam.exceptions.NoSuchEntityException:
        print("aqui")
        return False
    except:
        print("aqui2")
        return False
    
    
# Function name: main
# Purpose      : Delete users
# Arguments    : none
# Return       : none   
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 3:
        print("usage: {0} <name> <password>".format(
            sys.argv[0]
            )
        )
        exit(0)
        
    iam = boto3.client('iam')
    username = sys.argv[1]
    password = sys.argv[2]
    
    
    if(user_exists(iam, username)):       
        iam.create_login_profile(
            UserName=username,
            Password=password,
            PasswordResetRequired=True
        )
    else:
        print(f"---- The user {username} does not exist ----")
    


if __name__ == "__main__":
    main()    
    
