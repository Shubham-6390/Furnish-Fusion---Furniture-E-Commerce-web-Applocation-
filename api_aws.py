from flask import Flask, jsonify, request
import boto3

app = Flask(__name__)

dynamodb = boto3.resource("dynamodb")
users_table = dynamodb.Table("Users")
products_table = dynamodb.Table("Products")
orders_table = dynamodb.Table("Orders")

SNS_TOPIC_ARN = None
sns = boto3.client("sns")


@app.route("/health")
def health():
    return jsonify({"status": "FurnishFusion API running"})


@app.route("/products", methods=["POST"])
def add_product():
    data = request.json
    products_table.put_item(Item=data)
    return jsonify({"message": "Product added"})


@app.route("/products", methods=["GET"])
def list_products():
    response = products_table.scan()
    return jsonify(response.get("Items", []))


@app.route("/order", methods=["POST"])
def create_order():
    data = request.json
    orders_table.put_item(Item=data)

    if SNS_TOPIC_ARN:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=f"New order placed: {data['order_id']}"
        )

    return jsonify({"message": "Order placed successfully"})
