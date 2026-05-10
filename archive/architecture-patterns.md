# AWS Architecture Patterns

## Static website with S3 + CloudFront

- **Use case**: Host a simple public website with low operational overhead and fast global access.
- **Key AWS services**: Amazon S3, Amazon CloudFront, Route 53, AWS Certificate Manager.
- **Basic architecture flow**:
  1. Store static assets in an S3 bucket configured for website hosting.
  2. Use CloudFront as a CDN to cache assets at edge locations.
  3. Route traffic through Route 53 and use ACM for TLS.
- **Why this design works**: It decouples content storage from delivery, reduces latency, and avoids managing servers.
- **Common trade-offs**:
  - Great for read-heavy static content, but not suitable for dynamic server-side rendering.
  - Cache invalidation may require planning for content updates.
  - Requires correct bucket policies and origin settings to avoid public access issues.

## Three-tier web application with ALB + EC2 Auto Scaling + RDS

- **Use case**: Deploy a multi-tier web application with separate presentation, application, and database layers.
- **Key AWS services**: Amazon EC2, Application Load Balancer, Auto Scaling, Amazon RDS, VPC, Security Groups.
- **Basic architecture flow**:
  1. ALB receives traffic and forwards requests to EC2 instances in private subnets.
  2. Auto Scaling adjusts instance capacity based on load.
  3. EC2 application servers access RDS in a private subnet for persistent storage.
- **Why this design works**: It provides isolation between tiers, supports scaling, and improves fault tolerance.
- **Common trade-offs**:
  - Offers strong control over application runtime, but requires more management than serverless.
  - Database scaling can be a bottleneck if not designed with replicas or read replicas.
  - Cost is higher than simple serverless setups due to reserved capacity and managed database costs.

## Serverless order processing with API Gateway + Lambda + SQS + DynamoDB

- **Use case**: Build an event-driven backend for processing requests, especially when traffic is variable.
- **Key AWS services**: Amazon API Gateway, AWS Lambda, Amazon SQS, Amazon DynamoDB.
- **Basic architecture flow**:
  1. Clients submit requests through API Gateway.
  2. API Gateway triggers Lambda, which validates input and enqueues messages in SQS.
  3. A second Lambda consumes SQS messages and updates DynamoDB.
- **Why this design works**: It decouples request reception from processing, enabling better reliability and scaling.
- **Common trade-offs**:
  - Great for bursty workloads and pay-per-use pricing, but cold start latency may affect response time.
  - Requires careful monitoring of queue depth, Lambda concurrency, and DynamoDB capacity.
  - Not ideal for applications requiring long-lived sessions or complex in-memory state.

## Hybrid connectivity with Direct Connect and VPN backup

- **Use case**: Connect on-premises data centers to AWS with high reliability and lower network latency.
- **Key AWS services**: AWS Direct Connect, AWS Site-to-Site VPN, AWS Transit Gateway, VPC.
- **Basic architecture flow**:
  1. Primary connectivity uses Direct Connect to provide dedicated bandwidth.
  2. Site-to-Site VPN serves as a backup path over the public internet.
  3. Transit Gateway routes traffic between on-premises and multiple AWS VPCs.
- **Why this design works**: It delivers stable connectivity while protecting against a single link failure.
- **Common trade-offs**:
  - Direct Connect requires longer procurement and setup timelines than VPN.
  - Costs are higher for dedicated connectivity, but latency and throughput are superior.
  - Operational overhead includes managing both network paths and failover rules.

## Private subnet access to S3 using VPC Gateway Endpoint

- **Use case**: Allow EC2 instances in private subnets to access S3 without internet egress.
- **Key AWS services**: Amazon VPC, Gateway VPC Endpoint for S3, IAM policies, S3 bucket policies.
- **Basic architecture flow**:
  1. Create an S3 VPC Gateway Endpoint in the VPC.
  2. Update route tables for private subnets to use the endpoint.
  3. Configure IAM and bucket policies to restrict access to the endpoint.
- **Why this design works**: It improves security and reduces data transfer costs by keeping traffic within AWS.
- **Common trade-offs**:
  - Works well for private subnet workloads, but does not support all AWS services.
  - Endpoint policies need to be carefully scoped to avoid over-permission.
  - Not a replacement for internet access when external API calls are required.
