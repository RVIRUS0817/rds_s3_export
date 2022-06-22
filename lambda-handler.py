import json
import boto3
from datetime import datetime,date,timedelta

S3_BUCKET_NAME="xxxxxxxxxx"
IAM_ROLE_ARN="arn:aws:iam::xxxxxxxxxxxx:role/lambda-rds-s3-export"
KMS_KEY_ID="arn:aws:kms:ap-northeast-1:xxxxxxxxxx:key/xxxxxxxxxxxxxxxxxxxxx"

client = boto3.client('rds')

def lambda_handler(event, context):

    today = datetime.today()
    yesterday = today - timedelta(days=1)

    SOURCE_ARN="arn:aws:rds:ap-northeast-1:xxxxxxxxxx:cluster-snapshot:rds:xxxx-" + datetime.strftime(yesterday, '%Y-%m-%d-xx-xx')
    export_task_identifier="xxxxxxxx" + datetime.now().strftime("%Y%m%d%H%M%S")

    response = client.start_export_task(
        ExportTaskIdentifier=export_task_identifier,
        SourceArn=SOURCE_ARN,
        S3BucketName=S3_BUCKET_NAME,
        IamRoleArn=IAM_ROLE_ARN,
        KmsKeyId=KMS_KEY_ID,
#        ExportOnly=[
#        'hoge',
#        ]
    )

