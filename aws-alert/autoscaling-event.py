import boto3
import json

# Define common Variables

lambda_arn='arn:aws:lambda:us-west-2:699325298196:function:LogEC2InstanceStateChange'
role_arn='arn:aws:iam::699325298196:role/mycloudwatch'
rule_name='InstanceLaunchTerminate'
autoscale_grp='autoscale'

# Create  Cloudwatch client
client = boto3.client('events')

# Create Cloudwatch Rule
event_rule = client.put_rule(
    Name=rule_name,
    EventPattern=json.dumps(
        {
            "source": [
                "aws.autoscaling"
            ],
            "detail-type": [
                "EC2 Instance Launch Successful",
                "EC2 Instance Terminate Successful",
                "EC2 Instance Launch Unsuccessful",
                "EC2 Instance Terminate Unsuccessful",
                "EC2 Instance-launch Lifecycle Action",
                "EC2 Instance-terminate Lifecycle Action"
            ],
            "detail": {
                "AutoScalingGroupName": [
                    autoscale_grp
                ]
            }
        }
    ),
    State='ENABLED',
    Description='Autoscale instance Launch and Terminate Events',
    RoleArn=role_arn
)

## Create event Target for the above rule

event_target = client.put_targets(
    Rule = rule_name,
    Targets=[
        {
            'Id': rule_name + '-prod',
            'Arn': lambda_arn,

       }
    ]
)