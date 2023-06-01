#!/usr/bin/python3

### LIBRARIES
import boto3

def main():

    iam = boto3.client('iam')
    
    user_name = input("Enter the user name:\n> ")
    
    response = iam.create_user(UserName=user_name)
    
    print(response) 
    

if __name__ == "__main__":
    main()    
    
