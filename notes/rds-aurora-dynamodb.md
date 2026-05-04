# RDS, Aurora & DynamoDB

## Overview

This note compares relational and serverless database options for AWS architectures.

## When to use

- Use RDS for traditional relational applications with fixed schema.
- Use Aurora for high-performance relational workloads and read scaling.
- Use DynamoDB for serverless, high-scale key-value document storage.

## Common decision logic

- Choose RDS when you need a familiar database engine and managed backups.
- Choose Aurora when you need cloud-native relational scaling and high availability.
- Choose DynamoDB when you need fully managed low-latency access and flexible schema.

## Design implications

- RDS and Aurora are good choices for SQL workloads with transactions.
- DynamoDB works well for event-driven or mobile backends where schema evolves.
- Evaluate backup, recovery, and replication needs for each database type.

## Practical points

- Use read replicas or Aurora replicas for read scaling.
- Use DynamoDB partition keys and secondary indexes for efficient queries.
- Account for licensing and instance sizing in RDS/Aurora cost models.
