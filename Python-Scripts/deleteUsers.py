#!/usr/bin/python3

### LIBRARIES
import botocore
import boto3
import sys

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
            iam.delete_user(UserName=sys.argv[i])
        except Exception as e:
            print(f"Exception type: {type(e)}\n")
            print(f"---- Something went wrong when deleting user \"{sys.argv[i]}\" ----")

    

if __name__ == "__main__":
    main()    
    
