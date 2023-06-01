#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys

### FUNCTIONS
# Function name: main
# Purpose      : Creates users
# Arguments    : none
# Return       : none    
def main():

    number_of_names = len(sys.argv)
    if number_of_names == 1:
        print("usage: {0} <name_1> <name_2> ... <name_n>".format(
            sys.argv[0]
            )
        )
        exit(0)
        
    iam = boto3.client('iam')
    
    # iterate from 1 to the number_of_names provided
    for i in range(1,number_of_names):
        try:
            iam.create_user(UserName=sys.argv[i])
        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityAlreadyExists':
                print(f"Creation of User unsuccessful: The user \'{sys.argv[i]}\' already exists.")
        except Exception as e:
            print(f"Exception type: {type(e)}\n")
            print(f"---- Something went wrong when creating user \'{sys.argv[i]}\'----")
    

if __name__ == "__main__":
    main()    
    
