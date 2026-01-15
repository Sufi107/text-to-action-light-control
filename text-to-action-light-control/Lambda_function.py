mport json

def lambda_handler(event, context):
    # Parse body safely
    body = json.loads(event.get("body", "{}"))
    command = body.get("command", "").lower()

    if "turn on light" in command:
        message = "Light is turned ON"
    elif "turn off light" in command:
        message = "Light is turned OFF"
    else:
        message = "Command not recognized."

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message
        })
    }