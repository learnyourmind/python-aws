import boto3
import json

# Define common Variables

lambda_arn='arn:aws:lambda:us-west-2:699325298196:function:LogEC2InstanceStateChange'
role_arn='arn:aws:iam::699325298196:role/mycloudwatch'
rule_name='EC2StateChange'

# Create  Cloudwatch client
client = boto3.client('events')

# Create Cloudwatch Rule
event_rule = client.put_rule(
    Name=rule_name,
    EventPattern=json.dumps(
        {
            "source": ["aws.ec2"],
            "detail-type": ["EC2 Instance State-change Notification"]
        }
    ),
    State='ENABLED',
    Description='EC2 State Change event rule',
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