import os
import json
import boto3
from datetime import datetime,date,timedelta
 
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
IAM_ROLE_ARN = os.environ['IAM_ROLE_ARN']
KMS_KEY_ARN = os.environ['KMS_KEY_ARN']
 
client = boto3.client('rds')
 
def lambda_handler(event, context):
 
    today = datetime.today()
    yesterday = today - timedelta(days=1)
 
    SOURCE_ARN="arn:aws:rds:ap-northeast-1:xxxxxxxxxx:cluster-snapshot:rds:xxxx-" + datetime.strftime(yesterday, '%Y-%m-%d-xx-xx')
    EXPORT_TASK_IDENTIFIER="hoge" + datetime.now().strftime("%Y%m%d%H%M%S")
 
    response = client.start_export_task(
        ExportTaskIdentifier=EXPORT_TASK_IDENTIFIER,
        SourceArn=SOURCE_ARN,
        S3BucketName=S3_BUCKET_NAME,
        IamRoleArn=IAM_ROLE_ARN,
        KmsKeyId=KMS_KEY_ARN,
        ExportOnly=[
        'hoge',
        ]
    )
