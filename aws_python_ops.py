import boto3
s3 = boto3.resource('s3')

c = 0
for bucket in s3.buckets.all():
    print(bucket)
    c = 0 + 1