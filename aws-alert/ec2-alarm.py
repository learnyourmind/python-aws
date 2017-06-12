import boto3

# Create  Cloudwatch client
cloudwatch = boto3.client('cloudwatch')
ec2 = boto3.client('ec2')
seconds_in_one_day = 86400  # used for granularity
#INSTANCE_ID = ['i-0496f9e0749f57d01', 'i-02bd4aa0102cfa119']
#for instanceid in INSTANCE_ID:

# Create Alarm
response= ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])
        cloudwatch.put_metric_alarm(
            AlarmName=instance['InstanceId'] + '-EC2 CPU Utilization',
            Namespace='AWS/EC2',
            ComparisonOperator='GreaterThanThreshold',
            AlarmActions=[
                'arn:aws:sns:us-west-2:699325298196:my-topic'],
            EvaluationPeriods=1,
            MetricName='CPUUtilization',
            Period=seconds_in_one_day,
            Statistic='Average',
            Threshold=75.0,
            ActionsEnabled=True,
            AlarmDescription='Alarm When Server CPU exceeds 75%',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': instance['InstanceId']
                },
            ],
            Unit='Percent'
        )
