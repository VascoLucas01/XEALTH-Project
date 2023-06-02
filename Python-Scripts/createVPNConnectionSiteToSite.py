#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Creates a VPN connection site-to-site
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 6:
        print("usage: {0} <tag_name> <customer_gateway_id> <virtual_private_gateway_id> <local_ipv4_network_cidr> <remote_ipv4_network_cidr>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    tag_name                   = sys.argv[1]
    customer_gateway_id        = sys.argv[2]
    virtual_private_gateway_id = sys.argv[3]
    local_ipv4_network_cidr    = sys.argv[4]
    remote_ipv4_network_cidr   = sys.argv[5]
    
    
    ec2 = boto3.client('ec2')
    
    try:
        ec2.create_vpn_connection(
            CustomerGatewayId=customer_gateway_id,
            VpnGatewayId=virtual_private_gateway_id,
            Type='ipsec.1',
            Options={
                'LocalIpv4NetworkCidr': local_ipv4_network_cidr,
                'RemoteIpv4NetworkCidr': remote_ipv4_network_cidr
            },
            TagSpecifications=[
                {
                    'ResourceType': 'vpn-connection',
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
        print(f"---- Something went wrong when creating the VPN connection site-to-site ----")




    
if __name__ == "__main__":
    main()    
    
