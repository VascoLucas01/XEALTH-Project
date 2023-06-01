#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys

### FUNCTIONS
# Function name: main
# Purpose      : Deletes a VPC
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names == 1:
        print("usage: {0} <vpc_id>".format(
            sys.argv[0]
            )
        )
        exit(0)
        
    vpc_id  = sys.argv[1]
    
    ec2 = boto3.client('ec2')

    try:
        ec2.delete_vpc(VpcId=vpc_id)
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when creating the vpc ----")
    
    
    
if __name__ == "__main__":
    main()    
    
