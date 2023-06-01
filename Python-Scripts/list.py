#!/usr/bin/python3

### LIBRARIES
import boto3

### FUNCTIONS
# Function name: list_groups
# Purpose      : Lists groups
# Arguments    : iam
# Return       : none 
def list_groups(iam):
    for group in iam.list_groups()['Groups']:
        print("Group: {0}\nGroupID: {1}\nCreatedOn: {3}\n".format(
            group['GroupName'],
            group['GroupId'],
            group['Arn'],
            group['CreateDate']
            )
        )

# Function name: list_users
# Purpose      : Lists users
# Arguments    : iam
# Return       : none 
def list_users(iam):
    for user in iam.list_users()['Users']:
        print("User: {0}\nUserID: {1}\nCreatedOn: {3}\n".format(
            user['UserName'],
            user['UserId'],
            user['Arn'],
            user['CreateDate']
            )
        )
            
# Function name: main
# Purpose      : Prompts the user if he/she/other wants to list users or groups
# Arguments    : none
# Return       : none        
def main():
    
    iam = boto3.client('iam')

    user_input = input("Select one of the following options:\n\t1 - List Users\n\t2 - List Groups\n\n> ")

    match(user_input):
        case "1":
            list_users(iam)
        case "2":
            list_groups(iam)
        case _:
            print("\n ----- You do not entered a correct option -----\n")



if __name__ == "__main__":
    main()
