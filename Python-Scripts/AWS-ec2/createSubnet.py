#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys

############################# IMPORTANT NOTE #############################
#This script does not 'Enable auto-assign public IPv4 address'
##########################################################################


### FUNCTIONS
# Function name: main
# Purpose      : Creates a subnet
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 4:
        print("usage: {0} <subnet_name> <vpc_id> <CIDR_block> (suggestion for CIDR_block: 10.0.0.0/24)".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    subnet_name = sys.argv[1]
    vpc_id      = sys.argv[2]
    CIDR_block  = sys.argv[3]
    
    ec2 = boto3.client('ec2')
    
    try:
        subnet = ec2.create_subnet(
            TagSpecifications=[
                {
                    'ResourceType': 'subnet',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': subnet_name
                        },
                    ],
                }
            ],
            CidrBlock=CIDR_block,
            VpcId=vpc_id
        )
        
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when creating the subnet ----")
            
            
    
if __name__ == "__main__":
    main()    
    
