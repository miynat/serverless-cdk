import csv
import os

import boto3

_s3 = boto3.client("s3")
ddb = boto3.resource("dynamodb")
TABLE_NAME = os.environ["DYNAMODB_TABLE_NAME"]
BUCKET_NAME = os.environ["BUCKET_NAME"]


def handler(event, context):
    table = ddb.Table(TABLE_NAME)
    fh = event["Records"][0]["s3"]["object"]["key"]

    obj = _s3.get_object(Bucket=BUCKET_NAME, Key=fh)
    obj_content = obj["Body"].read().decode("utf-8")
    csv_file = obj_content.splitlines()
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        try:
            table.put_item(Item={"studentId": row[0], "Name": row[1], "City": row[2]})
        except Exception as e:
            return {"statusCode": 500, "body": e}

    return {"statusCode": 200, "body": "OK"}
