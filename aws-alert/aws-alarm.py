import boto3

# Create  Cloudwatch client
cloudwatch = boto3.client('cloudwatch')

INSTANCE_ID = ['i-0496f9e0749f57d01', 'i-02bd4aa0102cfa119']

for instanceid in INSTANCE_ID:

# Create Alarm
    response = cloudwatch.put_metric_alarm(
        AlarmName=instanceid + '-EC2 CPU Utilization',
        ComparisonOperator='GreaterThanThreshold',
        AlarmActions=[
            'arn:aws:sns:us-west-2:699325298196:my-topic'],
        EvaluationPeriods=1,
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Period=300,
        Statistic='Average',
        Threshold=75.0,
        ActionsEnabled=True,
        AlarmDescription='Alarm When Server CPU exceeds 75%',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instanceid
            },
        ],
        Unit='Percent'
    )
