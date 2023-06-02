#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Creates a virtual private gateway
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 2:
        print("usage: {0} <tag_name>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    tag_name            = sys.argv[1]
    
    
    ec2 = boto3.client('ec2')
    
    try:
        ec2.create_vpn_gateway(
            Type='ipsec.1',
            TagSpecifications=[
                {
                    'ResourceType': 'vpn-gateway',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': tag_name
                        },
                    ]
                },
            ]
        )
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when creating the virtual private gateway ----")




    
if __name__ == "__main__":
    main()    
    
