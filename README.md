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

