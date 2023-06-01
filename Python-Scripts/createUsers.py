#!/usr/bin/python3

### LIBRARIES
import boto3
import sys

def main():

    len = len(sys.argv)
    if len == 1:
        print("usage: {0} <name_1> <name_2> ... <name_n>".format(
            sys.argv[0]
            )
        )
        exit(0)
        
    iam = boto3.client('iam')
    
    for i in len:
        iam.create_user(UserName=sys.argv[i])
     
    

if __name__ == "__main__":
    main()    
    
