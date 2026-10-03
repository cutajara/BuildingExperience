import json
import os
from datetime import datetime, timezone

import boto3

sns = boto3.client("sns")


def lambda_handler(event, context):
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Methods": "OPTIONS,POST",
    }

    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": headers,
            "body": "",
        }

    try:
        body = json.loads(event.get("body") or "{}")
    except (TypeError, ValueError):
        return {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({"success": False, "message": "Request body is not valid JSON."}),
        }

    name = str(body.get("name", "")).strip()
    email = str(body.get("email", "")).strip()
    phone = str(body.get("phone", "")).strip()
    message = str(body.get("message", "")).strip()
    source = str(body.get("source", "website")).strip() or "website"

    if not name or not email or not message:
        return {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps(
                {"success": False, "message": "Name, email, and message are required."}
            ),
        }

    contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "message": message,
        "source": source,
        "receivedAt": datetime.now(timezone.utc).isoformat(),
    }

    try:
        sns.publish(
            TopicArn=os.environ["CONTACT_TOPIC_ARN"],
            Subject=f"New enquiry from {name}",
            Message=json.dumps(contact, indent=2),
        )

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(
                {"success": True, "message": "Your enquiry has been received. We will be in touch shortly."}
            ),
        }
    except Exception as exc:  # pragma: no cover - runtime/logging path
        print(f"SNS publish failed: {exc}")
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps(
                {"success": False, "message": "The enquiry could not be sent. Please try again later."}
            ),
        }
