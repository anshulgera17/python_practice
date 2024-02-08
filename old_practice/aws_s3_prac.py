#import boto3
#code is for list all the buckets in aws account

# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)


# for upload an image in bucket
    
# with open('test.jpg', 'rb') as data:
#     s3.Bucket('bucket-test-name-bbaacc').put_object(Key='test.jpg', Body=data)

# print the objects inside bucket
    
# from boto3 import client

# conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
# for key in conn.list_objects(Bucket='bucket-test-name-bbaacc')['Contents']:
#     print(key['Key'])
