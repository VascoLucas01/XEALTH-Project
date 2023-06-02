#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Creates a customer gateway
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 3:
        print("usage: {0} <tag_name> <ip_address>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    tag_name            = sys.argv[1]
    ip_address          = sys.argv[2]
    
    
    ec2 = boto3.client('ec2')
    
    try:
        ec2.create_customer_gateway(
            PublicIp=ip_address,
            Type='ipsec.1',
            TagSpecifications=[
                {
                    'ResourceType': 'customer-gateway',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': tag_name
                        },
                    ]
                },
            ]
            #IpAddress='string',
        )
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when creating the customer gateway ----")




    
if __name__ == "__main__":
    main()    
    
