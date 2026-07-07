import os
import boto3
from moto import mock_aws

# -------------------------------------------------
# Mock AWS Credentials
# -------------------------------------------------
os.environ["AWS_ACCESS_KEY_ID"] = "test"
os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

# -------------------------------------------------
# Start Moto Mock
# -------------------------------------------------
mock = mock_aws()
mock.start()

# Import AFTER mock starts
from api_aws import app
import api_aws


def setup_mock_aws():
    print(">>> Initializing Mock AWS for FurnishFusion (API Mode)...")

    dynamodb = boto3.resource("dynamodb")
    sns = boto3.client("sns")

    # ---------------- DynamoDB Tables ----------------

    dynamodb.create_table(
        TableName="Users",
        KeySchema=[{"AttributeName": "username", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "username", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    )

    dynamodb.create_table(
        TableName="Products",
        KeySchema=[{"AttributeName": "product_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "product_id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    )

    dynamodb.create_table(
        TableName="Orders",
        KeySchema=[{"AttributeName": "order_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "order_id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    )

    # ---------------- SNS ----------------

    topic = sns.create_topic(Name="furnishfusion_orders")
    api_aws.SNS_TOPIC_ARN = topic["TopicArn"]

    print(">>> Mock AWS ready")
    print(">>> SNS Topic:", api_aws.SNS_TOPIC_ARN)


if __name__ == "__main__":
    try:
        setup_mock_aws()

        print("\n>>> Starting FurnishFusion API (Local Test Mode)")
        print(">>> http://localhost:5000")
        print(">>> JSON-only responses, no templates")

        app.run(
            host="0.0.0.0",
            port=5000,
            debug=True,
            use_reloader=False
        )

    finally:
        mock.stop()
        print("\n>>> Mock AWS stopped")
