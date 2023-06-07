#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys

### FUNCTIONS
# Function name: main
# Purpose      : Creates a VPC
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 3:
        print("usage: {0} <vpc_name> <CIDR_block> (suggestion for CIDR_block: 10.0.0.0/16)".format(
            sys.argv[0]
            )
        )
        exit(0)
        
    vpc_name  = sys.argv[1]
    CIDR_block = sys.argv[2]
    
    ec2 = boto3.client('ec2')

    try:
        ec2.create_vpc(
            CidrBlock=CIDR_block,
            InstanceTenancy='default',
            TagSpecifications=[
                {
                    'ResourceType': 'vpc',
                    'Tags': [
                        {'Key': 'Name', 'Value': vpc_name}
                    ]
                }
            ]
            )
    except Exception as e:
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when creating the vpc ----")
    
    
    
if __name__ == "__main__":
    main()    
    
