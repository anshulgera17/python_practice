import boto3
import datetime
#------------------------------------------------------------------------------
#Bucket name
#Creation date (of the bucket)
#Number of files
#Total size of files
#Last modified date (most recent file of a bucket)
#And the most important of all, how much does it cost
#------------------------------------------------------------------------------

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
                print(obj)
        response = cw.get_metric_statistics(Namespace='AWS/S3',
                                        MetricName='BucketSizeBytes',
                                        Dimensions=[
                                            {'Name': 'BucketName', 'Value': bucket.name},
                                            {'Name': 'StorageType', 'Value': 'StandardStorage'}
                                        ],
                                        Statistics=['Average'],
                                        Period=3600,
                                        StartTime=(now-datetime.timedelta(days=2)).isoformat(),
                                        EndTime=now.isoformat(),
										Unit='Megabytes'
                                        )
        print(bucket.name.ljust(35) + str(bucket.creation_date).ljust(28)+ str(count).ljust(5)+str(response["Datapoints"][0]["Average"]).ljust(25))
        

