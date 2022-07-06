# rds_s3_export

It is a program to export to S3 with lambda from the previous day snapshot of RDS.

https://blog.adachin.me/archives/49717

![スクリーンショット 2022-07-05 15 08 58](https://user-images.githubusercontent.com/5633085/177260914-72bd06bf-a118-464f-a2dc-679046f0bcbc.jpg)


## Environment

https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html

- Lambda
  - Python3.9
- EventBridge Rule
- KMS
- RDS
  - snapshot
- S3
- AWS Glue
- Amazon Athena
- Redash

