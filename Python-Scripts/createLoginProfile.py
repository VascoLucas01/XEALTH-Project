#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys

### FUNCTIONS
# Function name: user_exists
# Purpose      : Verify if the user specified exists
# Arguments    : iam, user_name
# Return       : none   
def user_exists(iam, user_name):
    try:
        iam.get_user(UserName=user_name)
        return True
    except iam.exceptions.NoSuchEntityException:
        print("aqui")
        return False
    except Exception as e:
        print(e)
        return False
    
    
# Function name: main
# Purpose      : Creates users' login profile
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
    user_name = sys.argv[1]
    password = sys.argv[2]
    
    
    try: 
        if(user_exists(iam, user_name)):       
            iam.create_login_profile(
            UserName=user_name,
            Password=password,
            PasswordResetRequired=True
        )
        else:
            print(f"---- The user {user_name} does not exist ----")
    except ClientError as e:
        if e.response['Error']['Code'] == 'PasswordPolicyViolation':
            print("Creation of Login Profile unsuccessful: \n\n************************IMPORTANT************************\nPassword should have a minimum length of 8. \n\nPassword should meet 2 more of the following requirements: \n1. Password should have at least one uppercase letter \n2. Password should have at least one number \n3. Password should have at least one symbol")
            print("*********************************************************")
    except Exception as e:
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong ----")
    
    

if __name__ == "__main__":
    main()    
    
