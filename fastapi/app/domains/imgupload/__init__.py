import boto3

s3 = boto3.resource('s3')
client = boto3.client('s3')
bucket_name = 'zuplae-tests'

from . import actions
