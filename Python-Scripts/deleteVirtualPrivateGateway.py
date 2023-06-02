#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Deletes a virtual private gateway
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 2:
        print("usage: {0} <virtual_private_gateway_id>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    virtual_private_gateway_id = sys.argv[1]
    
    
    ec2 = boto3.client('ec2')
    
    try:
        ec2.delete_vpn_gateway(VpnGatewayId=virtual_private_gateway_id)
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when deleting the virtual private gateway ----")




    
if __name__ == "__main__":
    main()    
    
