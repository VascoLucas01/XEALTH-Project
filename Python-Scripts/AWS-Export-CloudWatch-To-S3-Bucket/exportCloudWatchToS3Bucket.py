############################## Author ##############################
# Rekhu
# Rekhu Repo: https://github.com/RekhuGopal
# Location of this python script in Rekhu Repo: https://github.com/RekhuGopal/PythonHacks/blob/main/AWS_Export_Cloudwatchlogs_to_s3_bucket/export_cloudwatchlogs_to_s3.py
####################################################################

import boto3
import os
import datetime



GROUP_NAME = "data-protection-audit-logs"
DESTINATION_BUCKET = "test2001t"
PREFIX = "XEALTH"
NDAYS = 0
nDays = int(NDAYS)


currentTime = datetime.datetime.now()
StartDate = currentTime - datetime.timedelta(days=nDays)
EndDate = currentTime - datetime.timedelta(days=nDays - 1)


fromDate = int(StartDate.timestamp() * 1000)
toDate = int(EndDate.timestamp() * 1000)

BUCKET_PREFIX = os.path.join(PREFIX, StartDate.strftime('%Y{0}%m{0}%d').format(os.path.sep))


def lambda_handler(event, context):
    client = boto3.client('logs')
    response = client.create_export_task(
         logGroupName=GROUP_NAME,
         fromTime=fromDate,
         to=toDate,
         destination=DESTINATION_BUCKET,
         destinationPrefix=BUCKET_PREFIX
        )
    print(response)
