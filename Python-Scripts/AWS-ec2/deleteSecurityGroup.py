#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Deletes a security group
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 3:
        print("usage: {0} <security-group-id> <security-group-name>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    security_group_id   = sys.argv[1]
    security_group_name = sys.argv[2]
    
    
    ec2 = boto3.client('ec2')

    
    try:
        ec2.delete_security_group(
            GroupId=security_group_id,
            GroupName=security_group_name
        )
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when deleting the security group ----")




    
if __name__ == "__main__":
    main()    
    
