# Building Experience AWS CDK deployment

This folder contains the Python AWS CDK app for the website enquiry form pipeline:

- API Gateway REST API
- Lambda function
- SNS topic

## Prerequisites

- Python 3.10+
- AWS CLI configured with credentials and a default region
- AWS CDK bootstrapped in the target account/region

## Install

```bash
cd infra
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Deploy

```bash
cd infra
cdk bootstrap
cdk deploy
```

## Update the website form endpoint

After deployment, copy the value from the stack output named `ApiGatewayUrl` and replace the placeholder in the site form:

```html
<form class="aws-form" data-api-url="https://YOUR_API_ID.execute-api.ap-southeast-2.amazonaws.com/prod/contact">
```

Use the real URL returned by CDK, for example:

```html
<form class="aws-form" data-api-url="https://abc123.execute-api.ap-southeast-2.amazonaws.com/prod/contact">
```

## Lambda behaviour

The Lambda validates the request, then publishes the enquiry to the SNS topic. The topic can be subscribed to an email address or an internal notification system after deployment.
