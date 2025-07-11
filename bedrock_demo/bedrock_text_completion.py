import boto3
import json

# Create a Bedrock Runtime client
client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

# Example modelId (change if needed)
model_id = "anthropic.claude-instant-v1"

# Prepare the request payload
payload = {
    "prompt": "\n\nHuman: Write a short poem about the cloud.\n\nAssistant:",
    "max_tokens_to_sample": 100,
    "temperature": 0.5,
}

# Send request to Bedrock
response = client.invoke_model(
    modelId=model_id,
    contentType="application/json",
    accept="application/json",
    body=json.dumps(payload),
)

# Parse and display the result
response_body = json.loads(response['body'])
completion_text = response_body.get("completion", "")

print("Response from Bedrock model:")
print(completion_text)
