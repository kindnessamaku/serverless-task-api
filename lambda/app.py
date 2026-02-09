import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ.get("TABLE_NAME", "DefaultTable"))

def lambda_handler(event, context):

    method = event.get("httpMethod")

    try:
        if method == "PUT":
            body = json.loads(event.get("body", "{}"))
            table.put_item(Item=body)
            return response(201, {"message": "Incident created/updated", "data": body})

        elif method == "GET":
            result = table.scan()
            return response(200, result.get("Items", []))

        elif method == "DELETE":
            path_params = event.get("pathParameters") or {}
            task_id = path_params.get("taskId")

            if not task_id:
                return response(400, "Missing 'taskId' in path")

            table.delete_item(
                Key={"taskId": task_id}
            )

            return response(200, f"Task {task_id} deleted")

    except Exception as e:
        print(f"Error: {e}") # Viewable in CloudWatch Logs
        return response(500, "Internal Server Error")

def response(status, message):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(message)
    }
