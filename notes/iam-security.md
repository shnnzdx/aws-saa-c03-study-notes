# IAM and Security

## Overview

IAM and security controls are foundational for AWS solution design.

## When to use

- Define roles and permissions for users, applications, and services
- Secure resources using least privilege and multi-factor authentication
- Protect sensitive data with encryption and endpoint controls

## Common decision logic

- Use IAM roles for applications and services instead of long-lived credentials.
- Apply least privilege to limit access to only the required resources.
- Use AWS Organizations and service control policies for account-level governance.

## Design implications

- IAM policies should be scoped to actions, resources, and conditions.
- Combine IAM with AWS Key Management Service for encryption key control.
- Use AWS Config, CloudTrail, and AWS Security Hub for auditing and compliance.

## Practical points

- Monitor for unused permissions and remove unnecessary access.
- Use AWS Managed Policies when they align with your use case.
- Secure management interfaces and avoid exposing the AWS management plane publicly.
