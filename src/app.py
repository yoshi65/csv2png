import base64
import json
from io import BytesIO, StringIO

import boto3
import matplotlib.pyplot as plt
import pandas as pd

print('Loading function')


class csv2png:
    def __init__(self):
        self.csv_data = None
        self.image = None

    def read_data(self, body):
        self.csv_data = pd.read_csv(StringIO(body), header=None)

    def draw_graph(self):
        buf = BytesIO()
        Column_name = self.csv_data.columns.values
        for i in range(1, len(self.csv_data.columns)):
            plt.plot(self.csv_data[Column_name[0]],
                     self.csv_data[Column_name[i]],
                     label=Column_name[i])
        plt.savefig(buf, format='png')
        buf.seek(0)
        self.image = buf.read()

    def response(self):
        return base64.b64encode(bytes(self.image)).decode('utf-8')


def lambda_handler(event, context):

    # check post
    try:
        request_body = event['body']
    except AttributeError:
        return {
            "statusCode":
            500,
            "body":
            json.dumps({
                "message": "'dict' object has no attribute 'body'",
            }),
        }

    # constacter
    cp = csv2png()
    # read csv format data
    cp.read_data(body=request_body)
    # draw graph
    cp.draw_graph()

    return {
        "statusCode": 200,
        "body": cp.response(),
        "headers": {
            'Content-Type': 'image/png'
        },
        "isBase64Encoded": True
    }
