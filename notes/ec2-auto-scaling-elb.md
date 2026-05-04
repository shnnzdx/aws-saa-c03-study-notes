# EC2, Auto Scaling & ELB

## Overview

This note covers compute scaling with Amazon EC2, Application Load Balancer (ALB), and Auto Scaling.

## When to use

- Applications requiring custom server configuration or legacy workloads
- Workloads that need control over the OS and runtime
- Scenarios where autoscaling and load balancing improve availability

## Common decision logic

- Use ALB for HTTP/HTTPS traffic and path-based routing.
- Use Auto Scaling groups to maintain instance capacity based on demand.
- Place instances in private subnets with a public-facing load balancer for isolation.

## Design implications

- Ensure health checks and scaling policies align with application startup time.
- Use multiple Availability Zones to improve fault tolerance.
- Combine Auto Scaling with Spot or On-Demand instances depending on cost and reliability.

## Practical points

- ALB offloads SSL termination and supports container-based targets.
- Auto Scaling should be sized for both normal and peak traffic.
- EC2-based designs require patching, monitoring, and OS-level security management.
