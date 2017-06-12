#!/usr/bin/python
import boto3

alarm_name='s3BucketsizeByte'
seconds_in_one_day = 86400  # used for granularity
cloudwatch = boto3.client('cloudwatch')
s3 = boto3.resource('s3')

# Create Alarm for S3 Buckets

for bucket in s3.buckets.all():
    print ("Allarm will be created for Bucket:"+     bucket.name)
    response = cloudwatch.put_metric_alarm(
        AlarmName=bucket.name +'-'+ alarm_name,
        Namespace='AWS/S3',
        AlarmActions=[
                'arn:aws:sns:us-west-2:699325298196:my-topic'],
        MetricName='BucketSizeBytes',
        ComparisonOperator='GreaterThanThreshold',
        Threshold=1073741824,
        EvaluationPeriods=1,
        Period= seconds_in_one_day,
        Statistic='Average',
        ActionsEnabled=True,
        AlarmDescription='Alarm When s3 Bucket size crosses 10GB',

        Dimensions=[
            {
                'Name': 'BucketName',
                'Value': bucket.name
            },
            {
                'Name': 'StorageType',
                'Value': 'StandardStorage'
            }
        ],
        Unit='Bytes'
    )
