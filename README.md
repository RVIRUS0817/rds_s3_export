# rds_s3_export

It is a program to export to S3 with lambda from the previous day snapshot of RDS.

![スクリーンショット 2022-07-05 15 08 58](https://user-images.githubusercontent.com/5633085/177260914-72bd06bf-a118-464f-a2dc-679046f0bcbc.jpg)


## Environment

https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html

- RDS
  - snapshot
- EventBridge
- S3
- Glue
- Athena
- KMS
- Lambda
  - Python3.9

