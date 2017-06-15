import boto3

# Create  Cloudwatch client
cloudwatch = boto3.client('cloudwatch')
periods_in_seconds = 300  # used for granularity
check_status_list = ['StatusCheckFailed','StatusCheckFailed_Instance','StatusCheckFailed_System']
autoscale_grp = 'autoscale'

# Create Alarm
for status in check_status_list:
    response = cloudwatch.put_metric_alarm(
            AlarmName=autoscale_grp+'-'+status,
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
                    'Name': 'AutoScalingGroupName',
                    'Value': autoscale_grp
                },
            ],
            Unit='Percent'
        )
