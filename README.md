# arxv-tool API Service

This repository contains the codebase for an AWS Lambda function that retrieves abstracts from arXiv given a list of URLs and uses OpenAI's API to analyze how the abstracts are interconnected. The infrastructure is managed using Terraform, and deployment is automated with GitHub Actions.

## Table of Contents

- Overview
- Architecture
- Prerequisites
- Setup
- Deployment
- Testing
- Cleanup
- Resources

## Overview

- **Lambda Function**: Processes a list of arXiv URLs, fetches their abstracts, and uses OpenAI's API to analyze how the abstracts are interconnected.
- **API Gateway**: Exposes the Lambda function via a REST API endpoint.
- **Terraform**: Infrastructure as code tool used to provision AWS resources.
- **GitHub Actions**: Automates deployment and infrastructure management.

## Architecture

The application consists of:

- An AWS Lambda function written in Python (index.py).
- An API Gateway REST API that triggers the Lambda function.
- Terraform configurations to manage AWS resources (terraform directory).
- GitHub Actions workflows for CI/CD (workflows directory).

## Prerequisites

- **AWS Account** with appropriate permissions.
- **GitHub Repository** with the following secrets configured:
  - [`AWS_ACCESS_KEY_ID`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FSource%20Code%2FProjects%2Farxv-tool%2F.github%2Fworkflows%2Fterraform-destroy.yml%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A22%2C%22character%22%3A41%7D%7D%5D%2C%229337f1ae-4469-4980-96a2-9d8a92cd26ee%22%5D "Go to definition")
  - [`AWS_SECRET_ACCESS_KEY`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FSource%20Code%2FProjects%2Farxv-tool%2F.github%2Fworkflows%2Fterraform-destroy.yml%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A23%2C%22character%22%3A45%7D%7D%5D%2C%229337f1ae-4469-4980-96a2-9d8a92cd26ee%22%5D "Go to definition")
  - [`AWS_REGION`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FSource%20Code%2FProjects%2Farxv-tool%2F.github%2Fworkflows%2Fterraform-destroy.yml%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A9%2C%22character%22%3A2%7D%7D%5D%2C%229337f1ae-4469-4980-96a2-9d8a92cd26ee%22%5D "Go to definition") (e.g., `us-east-1`)
  - [`TF_API_TOKEN`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%22file%22%2C%22path%22%3A%22%2Fc%3A%2FSource%20Code%2FProjects%2Farxv-tool%2F.github%2Fworkflows%2Fterraform-destroy.yml%22%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A2%7D%7D%5D%2C%22%22%5D "Go to file") (if using Terraform Cloud)
  - [`OPENAI_API_KEY`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%22file%22%2C%22path%22%3A%22%2Fc%3A%2FSource%20Code%2FProjects%2Farxv-tool%2F.github%2Fworkflows%2Fterraform-destroy.yml%22%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A2%7D%7D%5D%2C%22%22%5D "Go to file") (for OpenAI API access)
- **Terraform** installed locally (if deploying manually).
- **Python 3.9** installed locally (for Lambda function development).

## Setup

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/NStefanovski/arxv-tool.git
   ```

2. **Navigate to the Project Directory**:

   ```sh
   cd arxv-tool
   ```

3. **Configure AWS Credentials**:

   Configure your AWS credentials locally or ensure they are set in GitHub Secrets for workflows.

## Deployment

### Deploy Infrastructure with Terraform

Using GitHub Actions:

- Trigger the **Terraform** workflow manually from the Actions tab.

### Deploy Lambda Function

Using GitHub Actions:

- Trigger the **Lambda Deployment** workflow manually from the Actions tab.

## Testing

To test the API:

1. **Obtain the API Endpoint**:

   The API endpoint URL can be found in the Terraform outputs or AWS API Gateway console.

2. **Send a POST Request**:

   Sample JSON payload:

   ```json
   {
     "urls": [
       "https://arxiv.org/abs/2101.00001",
       "https://arxiv.org/abs/2101.00002"
     ]
   }
   ```

   Using `curl`:

   ```sh
   curl -X POST https://your-api-endpoint/prod/api \
   -H "Content-Type: application/json" \
   -d '{"urls": ["https://arxiv.org/abs/2101.00001", "https://arxiv.org/abs/2101.00002"]}'
   ```

## Cleanup

### Destroy Infrastructure with Terraform

Using GitHub Actions:

- Trigger the **Terraform Destroy** workflow manually from the Actions tab.

## Resources

- **Terraform Documentation**: [https://www.terraform.io/docs](https://www.terraform.io/docs)
- **AWS Provider for Terraform**: [AWS Provider Docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- **GitHub Actions Documentation**: [GitHub Actions](https://docs.github.com/en/actions)
- **AWS Lambda Developer Guide**: [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- **AWS API Gateway Developer Guide**: [API Gateway Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
- **OpenAI API Documentation**: [OpenAI API Docs](https://platform.openai.com/docs/)