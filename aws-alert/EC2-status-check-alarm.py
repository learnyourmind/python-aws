import boto3

# Create  Cloudwatch client
cloudwatch = boto3.client('cloudwatch')
periods_in_seconds = 300  # used for granularity
check_status_list = ['StatusCheckFailed','StatusCheckFailed_Instance','StatusCheckFailed_System']
instance_list = ['i-023281f0c3d803718','i-0496f9e0749f57d01']

# Create Alarm
for instance in instance_list:
    for status in check_status_list:
        response = cloudwatch.put_metric_alarm(
            AlarmName=instance+'-'+status,
            Namespace='AWS/EC2',
            ComparisonOperator='GreaterThanThreshold',
            AlarmActions=[
                'arn:aws:sns:us-west-2:699325298196:my-topic'],
            EvaluationPeriods=1,
            MetricName=status,
            Period=periods_in_seconds,
            Statistic='Average',
            Threshold=3,
            ActionsEnabled=True,
            AlarmDescription='Alarm Auto Scale group status check Failed',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': instance
                },
            ],
            Unit='Percent'
        )
