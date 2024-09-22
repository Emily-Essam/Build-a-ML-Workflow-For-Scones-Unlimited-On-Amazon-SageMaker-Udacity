import json

THRESHOLD = 0.93

def lambda_handler(event, context):
    # Print the event for debugging
    print("Received event:", json.dumps(event))

    # Parse the body from the event
    body = json.loads(event["body"])

    # Grab the inferences from the parsed body
    inferences = json.loads(body["inferences"])  # This will convert the string to a list

    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(confidence >= THRESHOLD for confidence in inferences)

    # If our threshold is met, pass our data back out of the Step Function,
    # else, end the Step Function with an error
    if meets_threshold:
        return {
            'statusCode': 200,
            'body': json.dumps(event)
        }
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")