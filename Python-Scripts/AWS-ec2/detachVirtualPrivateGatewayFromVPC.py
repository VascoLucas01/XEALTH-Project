#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Detaches a virtual private gateway from a VPC
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 3:
        print("usage: {0} <virtual_private_gateway_id> <vpc_id>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    virtual_private_gateway_id = sys.argv[1]
    vpc_id                     = sys.argv[2]
    
    
    ec2 = boto3.client('ec2')

    try:
        ec2.detach_vpn_gateway(
            VpcId=vpc_id,
            VpnGatewayId=virtual_private_gateway_id
        )
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when detaching the virtual private gateway from vpc ----")




    
if __name__ == "__main__":
    main()    
    
