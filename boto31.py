import sys
import boto3
# get the list of AWS region list
client = boto3.client('ec2')
regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
# define ami-id
ami_id = sys.argv[1]
# find the region name per ami id
for i in regions:
    client = boto3.client('ec2', region_name = i)
    response = client.describe_images(
        Filters =  [ {'Name': 'image-id', 'Values': [ami_id] } ],
    )['Images']
    if str(response) != '[]':
        print ("region_name with ami_id is ", i)
        break
# usage 
# $python find-aws-region-by-ami-id ami_id