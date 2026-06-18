import json

# import requests
# import boto3
# import pandas as pd
import io

from src.commons.config import host, password, port, user


def lambda_handler(event, context):
    print(event)

    print("Host name: ", host)
    print("user: ", user)
    print("password: ", password)
    print("port: ", port)


    # s3_content = event['Records'][0]['s3']
    # bucket_name = s3_content['bucket']['name']
    # file_name = s3_content['object']['key']
    # print("bucket name: ", bucket_name)
    # print('File Name: ', file_name)
    #
    # s3 = boto3.client("s3")
    #
    # response = s3.get_object(Bucket=bucket_name, Key=file_name)
    # df = pd.read_csv(io.BytesIO(response["Body"].read()))
    #
    # from io import StringIO
    # csv_buffer = StringIO()
    # df.to_csv(csv_buffer, index=False)
    #
    # s3.put_object(Bucket="batch-may-15-2026", Key="cleaned_data.csv", Body=csv_buffer.getvalue())
    #
    # print(df.head())

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
