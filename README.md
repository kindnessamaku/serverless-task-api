# Serverless Task Incident Management API
## Overview
This project demonstrates the design and deployment of a serverless incident management REST API on AWS. The system enables engineering teams to create incidents, track timestamps, and monitor service failure latency through a scalable API interface. The application exposes REST endpoints that allow teams to log operational incidents, retrieve incident records for analysis, and delete resolved incidents. Each incident contains timestamp data that can be used to measure failure response time and operational efficiency. It uses fully managed AWS serverless services, eliminating the need to provision or manage infrastructure while ensuring automatic scalability and high availability.
## Key Features
### The API supports the core lifecycle operations for incident tracking:

- PUT — Create Incident
  - Stores a new incident record in DynamoDB
  - Records incident timestamp for latency analysis

- GET — Retrieve Incidents
  - Retrieves all recorded incidents
  - Enables teams to analyze operational response timelines

- DELETE — Remove Incident
  - Deletes incidents once they are resolved
  - Helps maintain clean operational records
 
### The System also constitues components of the AWS Well-Architected Framework : 
- **Serverless Architecture** : It uses AWS serverless services to achieve automatic scaling and high availability without managing servers.
   - Amazon API Gateway for REST API endpoints
   - AWS Lambda for serverless compute
   - Amazon DynamoDB for persistent data storage
 
- **Security** : It is implemented using IAM roles that grant only the permissions required for the Lambda function to operate, including:
   - Writing logs to CloudWatch
   - Reading and writing data to DynamoDB

- **Monitoring and Observability** : Operational visibility is provided using:
  - CloudWatch Logs for debugging Lambda execution
  - CloudWatch Alarms for monitoring production API performance
 
## Prerequisites
  - An AWS account
  - AWS CLI configured locally
  - Git installed
  - A GitHub repository containing the Lambda code
  - Postman or any REST API testing tool

## Architecture Diagram
![serverless](https://github.com/user-attachments/assets/cabb9e9b-c753-4dd7-b7d7-8c22eb29fac9)


## Deployment Guide

  - **Step 1 — Create DynamoDB Table** : This table will store incident records and their timestamps.
  - **Step 2 — Create IAM Role for Lambda** : The role should allow **Writing logs to CloudWatch** and **Reading and writing items in DynamoDB**.
  - **Step 3 — Create Lambda Function** : Copy the Lambda function code from this repository and edit the code to ensure that it aligns with the name of your dynamodb table.

- **Step 4 — Create API Gateway REST API** : Add the following HTTP methods: PUT, GET, DELETE.
- **Step 5 — Deploy the API** : Copy the Invoke URL and test the endpoints using Postman. Successful responses should return '200 OK'
- **Step 6 — Configure CloudWatch Alarms** : Create CloudWatch alarms for the production stage to monitor API performance.

## Adding CI/CD Pipeline
Why CI/CD?
A CI/CD pipeline automates the build, testing, and deployment process, reducing manual errors and enabling faster, reliable releases.

- **Step 1 — Create buildspec.yml** : A buildspec file defines the build instructions used by CodeBuild. It specifies:
   - Build phases
   - Commands to execute
   - Artifact output configuration
To use the buildspec file, clone the repository locally:
```
git clone <repo-url>
```
The buildspec file will be used during the build stage of the pipeline.

- **Step 2 — Create IAM Role for CodeBuild** : Create an IAM role that allows CodeBuild to:
  - Access Lambda
  - Upload artifacts to S3
  - Write logs to CloudWatch
 
- **Step 3 — Create CodePipeline** : Create a pipeline using AWS CodePipeline. Connect your GitHub account and select the repository containing the project code. Once configured, the CI/CD workflow becomes fully automated.

## Challenges and Key Lessons Learned
 - **Challenge 1 — 500 Internal Server Error**
   
   - Problem : When calling the GET endpoint in Postman, the API returned: **500 Internal Server Error**. This indicated that API Gateway successfully invoked Lambda but the Lambda function failed during execution.
     
   - Investigation : CloudWatch logs were examined to identify the root cause.
The logs revealed that the Lambda execution role lacked permission to read from DynamoDB using the Scan operation.

   - Resolution : The IAM policy was updated to include
    ```
     dynamodb:Scan
    ```
After updating the role and testing again in Postman, the API returned: **200 OK**

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/06e9dd52-5f41-414a-8684-61353f66efba" width="300" alt="Server Error">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/fcd92857-78db-434c-8370-53cc7ce6c331" width="300" alt="Logs">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/3ff5812a-b07e-4c10-adde-0cb48a65efb8" width="300" alt="Successful">
    </td>
  </tr>
</table>

- **Challenge 2 — CodePipeline Build Failure**
  
  - Problem : The build stage of the CI/CD pipeline failed during execution.
  - Investigation : CloudWatch build logs revealed a syntax error in the buildspec.yml file.
  - Resolution : The syntax error was corrected and the pipeline was executed again.
The build completed successfully and the pipeline resumed normal operation.

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/a0946ab9-2b3e-438b-b420-c2f2689862c4" width="300" alt="Build Error">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/068da17d-3235-43d5-89ab-068c46b57ad3" width="300" alt="Logs">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/e9a33524-74d4-48e4-a184-17b9f979f410" width="300" alt="Successful">
    </td>
  </tr>
</table>

## Key Achievements
- Eliminated the need for always-on servers, saving an estimated 70-90%compared to EC2-based solutions.
- Reduced debbuging time by 60% using centralized cloudwatch logging.
- Reduced deployment time from 15 minutes to under 3 minutes using CI/CD






 






