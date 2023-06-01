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
        return False
    except Exception as e:
        return False
    
    
# Function name: main
# Purpose      : Deletes the users specified
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
            iam.delete_login_profile(UserName=sys.argv[i])
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchEntity':
                print(f"The login profile of the user \'{sys.argv[i]}\' was not deleted: User \'{sys.argv[i]}\' cannot be found.")
        except Exception as e:
            print(f"Exception type: {type(e)}\n")
            print(f"---- Something went wrong when deleting login profile of user \'{sys.argv[i]}\' ----")
    
    

if __name__ == "__main__":
    main()    
    
