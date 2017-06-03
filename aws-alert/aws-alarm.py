import boto3

#Create  Cloudwatch client
cloudwatch = boto3.client('cloudwatch')

#Create Alarm
cloudwatch.put_metric_alarm(
    AlarmName='EC2 CPU Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='EC2CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=75.0,
    ActionsEnabled=False,
    AlarmDescription='Alarm When Server CPU exceeds 75%',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'INSTANCE_ID'
        },
    ],
    Unit='Seconds'
)