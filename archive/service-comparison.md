# AWS Service Comparison

## S3 Standard vs S3 Intelligent-Tiering vs S3 Standard-IA vs Glacier

| Service | Best use case | Strengths | Limitations | Common decision logic |
| --- | --- | --- | --- | --- |
| S3 Standard | Frequently accessed objects with unpredictable access patterns | Low latency, high durability, immediate availability | Higher storage cost | Use when data is accessed often or requires fast retrieval. |
| S3 Intelligent-Tiering | Data with unknown or changing access patterns | Automated tiering, minimal management | Monitoring and automation costs apply | Choose when workloads have unpredictable access and you want automated cost optimization. |
| S3 Standard-IA | Infrequently accessed data that still requires rapid retrieval | Lower storage cost than Standard, immediate access | Retrieval fee and minimum storage duration | Use for backups or archives where access is rare but still needs fast access. |
| Glacier | Long-term archive with infrequent retrieval | Lowest storage cost, strong durability | Retrieval delay and retrieval pricing | Choose for long-retention archives and regulatory records with rare access. |

## SQS Standard vs SQS FIFO

| Service | Best use case | Strengths | Limitations | Common decision logic |
| --- | --- | --- | --- | --- |
| SQS Standard | High-throughput, loosely ordered message processing | Unlimited throughput, at-least-once delivery | Messages may be delivered out of order or duplicated | Use when order is not strict and parallel processing is important. |
| SQS FIFO | Ordered processing and exactly-once handling | Preserves message order and deduplication | Lower throughput, requires message group IDs | Use when processing must preserve order or avoid duplicates. |

## SNS vs SQS vs EventBridge

| Service | Best use case | Strengths | Limitations | Common decision logic |
| --- | --- | --- | --- | --- |
| SNS | Pub/sub notification fan-out | Push-based delivery to multiple subscribers | Not designed for long-term persistence or complex routing | Use for real-time notifications and fan-out to multiple endpoints. |
| SQS | Decoupled processing with message queuing | Durable queue, retries, visibility timeout | Requires consumers to poll and process messages | Use when asynchronous backend processing or buffering is needed. |
| EventBridge | Event routing with schema and filtering | Complex event patterns, SaaS integrations | Higher latency for real-time events than direct push | Use for event-driven architectures with multiple targets and rules. |

## RDS vs Aurora vs DynamoDB

| Service | Best use case | Strengths | Limitations | Common decision logic |
| --- | --- | --- | --- | --- |
| RDS | Traditional relational databases with managed operations | Familiar engines, managed backups, replicas | Limited scalability compared to serverless NoSQL | Use for relational workloads with structured schema and transactional requirements. |
| Aurora | High-performance relational database with cloud-native scaling | Better performance and read scaling than RDS | Higher cost and more AWS-specific features | Use when you need managed relational database performance and availability at scale. |
| DynamoDB | Serverless key-value and document database | Fully managed, single-digit ms latency, auto scaling | Not suitable for complex relational joins | Use for high-scale, low-latency access with flexible schema. |

## NAT Gateway vs VPC Endpoint

| Service | Best use case | Strengths | Limitations | Common decision logic |
| --- | --- | --- | --- | --- |
| NAT Gateway | Private subnet internet egress for updates and outbound traffic | Simple internet access for private resources | Continuous hourly cost and data processing fees | Use when private resources need outbound internet access. |
| VPC Endpoint | Private access to supported AWS services without internet | Secure service access inside VPC, no NAT required | Limited to supported services and endpoint types | Use when connecting privately to S3, DynamoDB, or supported AWS services from private subnets. |

## CloudFront vs Global Accelerator

| Service | Best use case | Strengths | Limitations | Common decision logic |
| --- | --- | --- | --- | --- |
| CloudFront | Content delivery for web and API traffic | Global caching, edge security, low latency for static and dynamic content | Not optimized for non-HTTP/TCP traffic | Use for web assets, APIs, and edge caching. |
| Global Accelerator | Accelerate TCP/UDP traffic and improve global application availability | Static anycast IPs, optimized network paths | Not a CDN; no edge caching | Use for latency-sensitive applications and TCP/UDP traffic across regions. |

## Secrets Manager vs Systems Manager Parameter Store

| Service | Best use case | Strengths | Limitations | Common decision logic |
| --- | --- | --- | --- | --- |
| Secrets Manager | Manage database credentials, API keys, and secrets with rotation | Automatic secret rotation, secure secrets lifecycle | Higher cost per secret | Use when managing sensitive credentials with automatic rotation and advanced auditing. |
| Parameter Store | Store configuration values and standard parameters | Low-cost option for plaintext and secure strings | Lacks built-in rotation and some auditing features | Use for application configuration and less sensitive encryption keys. |
