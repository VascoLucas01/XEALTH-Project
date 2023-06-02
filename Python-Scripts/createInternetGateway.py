#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Creates an internet gateway
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 3:
        print("usage: {0} <internet-gateway-name>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    internet_gateway_name = sys.argv[1]
    
    ec2 = boto3.client('ec2')

    try:
        ec2.create_internet_gateway(
            TagSpecifications=[
                {
                    'ResourceType': 'internet-gateway',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': internet_gateway_name
                        },
                    ]
                },
            ],

        )
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when creating the internet gateway ----")




    
if __name__ == "__main__":
    main()    
    
