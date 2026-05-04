# Serverless Architecture

## Overview

Serverless architectures reduce operational overhead by using managed compute and event-driven services.

## When to use

- APIs, event processing, and lightweight business logic
- Workloads that can scale quickly with demand
- Use cases where infrastructure management should be minimized

## Common decision logic

- Use Lambda for compute functions that run in response to events.
- Use API Gateway to expose serverless APIs securely.
- Use managed databases such as DynamoDB for serverless data persistence.

## Design implications

- Serverless functions should remain stateless to scale effectively.
- Monitor cold start impact and design for idempotent processing.
- Use tracing and logs to troubleshoot distributed serverless workflows.

## Practical points

- Serverless often lowers upfront cost but requires careful architecture for performance.
- Use managed services like EventBridge and SQS to decouple components.
- Identify stateful needs early and keep them outside Lambda functions.
