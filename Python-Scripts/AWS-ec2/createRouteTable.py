#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Creates a route table
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 3:
        print("usage: {0} <name_route_table> <vpc_id>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    name_route_table = sys.argv[1]
    vpc_id           = sys.argv[2]
    
    ec2 = boto3.client('ec2')

    try:
        ec2.create_route_table(
            VpcId=vpc_id,
            TagSpecifications=[
                {
                    'ResourceType': 'route-table',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': name_route_table
                        },
                    ]
                },
            ]
        )
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when creating the route table ----")




    
if __name__ == "__main__":
    main()    
    
