output "api_endpoint" {
  description = "API Gateway endpoint URL"
  value       = "${aws_api_gateway_rest_api.lambda_api.execution_arn}/prod/api"
}