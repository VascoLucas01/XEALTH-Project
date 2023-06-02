#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Attaches an internet gateway to a VPC
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names == 1:
        print("usage: {0} <internet-gateway-id> <vpc_id>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    internet_gateway_id = sys.argv[1]
    vpc_id              = sys.argv[2]
    
    
    ec2 = boto3.client('ec2')

    try:
        ec2.attach_internet_gateway(
            InternetGatewayId=internet_gateway_id,
            VpcId=vpc_id
        )
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when attaching the internet gateway to vpc ----")




    
if __name__ == "__main__":
    main()    
    
