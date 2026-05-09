# VPC Networking (Exam-Focused)

## Why this matters in SAA-C03

Networking questions are usually not asking for raw definitions. They test whether you can pick the architecture that best matches one keyword in the scenario:

- `private access` -> endpoint or private connectivity
- `no internet exposure` -> private subnet + controlled ingress
- `least operational overhead` -> managed networking services
- `multi-VPC at scale` -> transit gateway pattern

## Core mental model

Think in this order for every networking question:

1. Traffic source and destination
2. Whether internet is allowed
3. Which routing hop is required
4. Which security layer can enforce the requirement

## VPC and subnet essentials

- VPC is regional.
- Subnet is Availability Zone specific.
- CIDR range is `/16` to `/28`.
- AWS reserves 5 IP addresses per subnet.
- Public or private subnet is decided by route table, not subnet name.

## Route table quick rules

- Most specific route wins.
- Public subnet needs `0.0.0.0/0 -> Internet Gateway`.
- Private subnet outbound internet commonly uses `0.0.0.0/0 -> NAT Gateway`.
- For HA, use one NAT Gateway per AZ and route private subnets to same-AZ NAT when possible.

## Security Groups vs NACL (high-frequency trap)

| Item | Security Group | NACL |
|---|---|---|
| Level | ENI / instance | Subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow + deny |
| Rule evaluation | All rules | Number order |
| Common use | Workload access control | Coarse subnet guardrails |

Exam trap:

- Need to block a specific IP quickly at subnet boundary -> NACL is often the best answer.
- Need instance-level least privilege access -> Security Group is usually expected.

## Connectivity decision tree

### Private subnet needs outbound internet

- Use NAT Gateway in public subnet.
- Do not attach public IP directly to private instances.

### Access S3/DynamoDB privately from VPC

- Use Gateway VPC Endpoint.

### Access most other AWS services privately

- Use Interface VPC Endpoint (PrivateLink).

### Connect two VPCs

- Small/simple pair: VPC Peering.
- Many VPCs or transitive routing needed: Transit Gateway.

### Connect on-premises to AWS

- Fast setup, encrypted over internet: Site-to-Site VPN.
- Dedicated, stable, high-throughput private link: Direct Connect.

## Route 53 policies you must not confuse

- Weighted: traffic split for migration or A/B.
- Latency: best user latency.
- Failover: active-passive DR with health checks.
- Geolocation: route by user location.
- Multi-value: multiple healthy records.

## Top exam traps (from practice patterns)

1. Choosing IGW when question requires private outbound-only access.
2. Choosing Security Group for explicit deny requirements.
3. Using VPC Peering when topology needs transitive routing.
4. Ignoring "least operational overhead" and picking self-managed NAT instance.
5. Missing "without traversing the internet" and not selecting VPC Endpoint.

## 60-second answer framework (during exam)

1. Underline requirement words: private / encrypted / lowest latency / low ops.
2. Remove options that violate the requirement directly.
3. Among remaining options, pick the most managed and least complex architecture.

## Rapid self-check

- Can you explain SG vs NACL in one sentence each?
- Can you decide NAT Gateway vs VPC Endpoint from one requirement line?
- Can you justify TGW over peering for multi-VPC growth?
- Can you pick Route 53 policy in under 10 seconds from scenario keywords?

## Source integration notes

This note is an integrated and adapted summary from:

- https://github.com/ChathurangaVKD/AWS-Certified-Solutions-Architect-Associate-SAA-C03/tree/main/06-Networking
