#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Deletes a route table
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 2:
        print("usage: {0} <route_table_id>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    route_table_id = sys.argv[1]
    
    ec2 = boto3.client('ec2')

    try:
        ec2.delete_route_table(RouteTableId=route_table_id)
    except Exception as e:
        print(e)
        print(f"Exception type: {type(e)}\n")
        print(f"---- Something went wrong when deleting the route table ----")




    
if __name__ == "__main__":
    main()    
    
