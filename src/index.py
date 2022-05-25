from concurrent.futures import process
from email import message
from lib2to3.pgen2 import token
import os
import boto3

s3 = boto3.client('s3', region_name='ap-northwest-2')


def awsLambdaReceiver():
    signingSecret = process.env.SLACK_SIGNING_SECRET
    return {
        signingSecret: signingSecret
    }


def app():
    return{token: process.env.SLACK_BOT_TOKEN,
           "receiver": awsLambdaReceiver}
