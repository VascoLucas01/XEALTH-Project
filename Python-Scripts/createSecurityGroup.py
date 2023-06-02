#!/usr/bin/python3

### LIBRARIES
from botocore.exceptions import ClientError
import boto3
import sys


### FUNCTIONS
# Function name: main
# Purpose      : Creates a security group
# Arguments    : none
# Return       : none 
def main():

    number_of_names = len(sys.argv)
    if number_of_names != 4:
        print("usage: {0} <tag_name> <security-group-name> <vpc_id>".format(
            sys.argv[0]
            )
        )
        exit(0)
    
    tag_name            = sys.argv[1]
    security_group_name = sys.argv[2]
    vpc_id              = sys.argv[3]
    
    
    ec2 = boto3.client('ec2')

    description = input("Enter the security group description:\n\n> ")
    
    try:
        ec2.create_security_group(
            Description=description,
            GroupName=security_group_name,
            VpcId=vpc_id,
            TagSpecifications=[
                {
                    'ResourceType': 'security-group',
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
        print(f"---- Something went wrong when creating the security group ----")




    
if __name__ == "__main__":
    main()    
    
