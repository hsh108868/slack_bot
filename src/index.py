import os
import boto3
import logging
import json
import urllib.request

s3 = boto3.client('s3', region_name='ap-northwest-2')


def lambda_handler(event, context) -> str:
    json_region = os.environ['ap-northwest-2']
    logging.info(json.dumps(event))

    if "upload" in event:
        return event.get("challenge")
