import boto3
s3 = boto3.client('s3')
s3.upload_file(local_file, bucket, s3_file, ExtraArgs=dict(ContentType='image/png'))
# upoad_file -- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/upload_file.html#
# extra_args -- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.S3Transfer.ALLOWED_UPLOAD_ARGS
