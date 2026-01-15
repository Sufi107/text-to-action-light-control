 TEXT TO ACTION

Cloud Platform - Amazon Web Services (AWS)
API Layer - Amazon API Gateway (HTTP API)
Compute - AWS Lambda (Python)
Database - Amazon DynamoDB (further)
Testing Tool – Postman

Architecture Flow: User → API Gateway → AWS Lambda → DynamoDB → Response to User

This project converts text commands into actions such as turning a light ON or OFF.
Example Commands
- "turn on light"
- "turn off light"

AWS Services Used
- AWS Lambda
- API Gateway
- DynamoDB
- AWS Budgets
How to Test
Send a POST request with JSON:
{
  "command": "turn on light"
}
