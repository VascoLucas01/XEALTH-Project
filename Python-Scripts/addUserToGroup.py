#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3


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
        return False
    except:
        return False
    
    
# Function name: group_exists
# Purpose      : Verify if the group specified exists
# Arguments    : iam, group_name
# Return       : none   
def group_exists(iam, group_name):
    try:
        iam.get_group(GroupName=group_name)
        return True
    except iam.exceptions.NoSuchEntityException:
        return False
    except:
        return False


# Function name: main
# Purpose      : Prompts the user to specify the user and the group in order to add that user to that specific group
# Arguments    : none
# Return       : none        
def main():
    
    iam = boto3.client('iam')

    user_name = input("Enter the user you want to add to a group:\n\n> ")
    group_name = input("\n\nEnter group name:\n\n> ")

    if(user_exists(iam, user_name)):
        if(group_exists(iam,group_name)):
            try:
                iam.add_user_to_group(
                    GroupName=group_name,
                    UserName=user_name
                )
            except Exception as e:
                print(f"Exception type: {type(e)}\n")
        else:
            print(f"---- The group {group_name} does not exist ----")
    else:
        print(f"---- The user {user_name} does not exist ----")
            



if __name__ == "__main__":
    main()


