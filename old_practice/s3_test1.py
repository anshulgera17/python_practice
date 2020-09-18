import boto3
import datetime

now = datetime.datetime.now()
s3 = boto3.resource('s3')
cw = boto3.client('cloudwatch',region_name='us-east-1')
#print('Bucket'.ljust(35) + 'Bucket creation date'.ljust(28)+ 'objects count'.ljust(5)+ 'Size in Bytes'.ljust(25))
#print('------------------------------------------------------------------------------')
for bucket in s3.buckets.all():
        count=0
        total_bytes = 0
        for obj in bucket.objects.all():	
                count=count+1
#                print('------------------------------------------------------------------------------')
#                print(obj)
        response = cw.get_metric_statistics(Namespace='AWS/S3',
                                        MetricName='BucketSizeBytes',
                                        Dimensions=[
                                            {'Name': 'BucketName', 'Value': 'bucket.name'},
                                            {'Name': 'StorageType', 'Value': 'StandardStorage'}
                                        ],
                                        Statistics=['Average'],
                                        Period=3600,
                                        StartTime=(now-datetime.timedelta(days=2)).isoformat(),
                                        EndTime=now.isoformat(),
                                        Unit='Bytes'|'Kilobytes',
                                        ReturnData = True|False
                                        )				
        print(bucket.name.ljust(35) + str(bucket.creation_date).ljust(28)+ str(count).ljust(5))