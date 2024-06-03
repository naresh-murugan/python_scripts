import boto3
def terminate_instance(access_key,secret_access_key,region_name,instance_id):
    ec2 = boto3.client('ec2',
                       aws_access_key_id=access_key,
                       aws_secret_access_key=secret_access_key,
                       region_name=region_name)
    ec2.terminate_instances(InstanceIds=[instance_id])
terminate_instance(input("Enter access key: "),input("\nEnter secert access key: "),input("\n Enter region: "),input("\n Enter instance id: "))
import pandas as pd
a= pd.DataFrame()
