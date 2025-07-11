# AWS Bedrock Demo

This repo shows how to:
- Connect to AWS Bedrock using the AWS SDK (Boto3)
- Call a Bedrock text-generation model
- Understand basic Bedrock API workflow

---

## ✨ What is AWS Bedrock?

AWS Bedrock is Amazon’s fully managed service for accessing powerful foundation models. It lets you:
- Generate text
- Summarize documents
- Create chat experiences
- And more!

---

## 🛠️ Prerequisites

✅ AWS Account (Bedrock costs may apply)  
✅ AWS CLI configured with credentials and permissions for Bedrock  
✅ Python 3.9+  
✅ Boto3 SDK

---

## ⚙️ Installation

Clone this repo:

```bash
git clone https://github.com/YOUR_USERNAME/aws-bedrock-beginner.git
cd aws-bedrock-beginner

Install dependencies:
```
pip install -r requirements.txt
```

How to Run

Run the Python script:

```
python bedrock_demo/bedrock_text_completion.py
```

Expected output:

Response from Bedrock model:
[generated text]

📝 Example Output
Prompt:

Write a short poem about the cloud.

Response:

The cloud drifts soft across the sky,
A gentle sail where breezes fly... 

(this is an example response)

✅ Supported Models
This example uses a text-generation model, e.g.:

Anthropic Claude

AI21 Jurassic

Amazon Titan

Check which models are available in your region.

🔒 Security Note
Never commit AWS secrets to your repository.

Use minimal IAM permissions for Bedrock access.

📚 Resources

[AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
[Boto3 Bedrock Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html)
