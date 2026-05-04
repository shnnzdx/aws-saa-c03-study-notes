# VPC Networking

## Overview

VPC networking defines how resources communicate within AWS and with external systems.

## When to use

- Segment applications with public, private, and database subnets
- Control traffic with security groups and network ACLs
- Connect on-premises networks to AWS using VPN or Direct Connect

## Common decision logic

- Use multiple Availability Zones for subnet redundancy.
- Place load balancers in public subnets and backend workloads in private subnets.
- Use NAT Gateway for private subnet internet egress when needed.

## Design implications

- Security groups are stateful and operate at the instance or ELB level.
- Network ACLs are stateless and useful for subnet-level controls.
- VPC endpoints can keep traffic to AWS services internal to AWS.

## Practical points

- Keep CIDR ranges large enough for future growth, but small enough to avoid waste.
- Use route tables to control traffic paths between subnets and gateways.
- Review subnet placement when designing highly available architectures.
