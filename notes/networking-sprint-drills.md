# Networking Sprint Drills (SAA-C03)

## Goal

Use this file for final-day networking drills with exam-answering logic.

## Drill Set A: Identify the keyword first

For each question, find one primary keyword before reading options:

- private access
- no internet path
- outbound only
- cross-account private service
- multiple VPC scale
- dedicated on-prem connectivity

## Drill Set B: One-line service mapping

- Private subnet internet egress -> NAT Gateway
- Private access to S3/DynamoDB -> Gateway Endpoint
- Private access to most AWS managed services -> Interface Endpoint (PrivateLink)
- Multiple VPC hub-and-spoke -> Transit Gateway
- Two VPC simple direct link -> VPC Peering
- Dedicated data center link -> Direct Connect
- Encrypted internet-based hybrid link -> Site-to-Site VPN

## Drill Set C: Elimination patterns

- Requirement says "least operational overhead" -> eliminate self-managed EC2 middleboxes first
- Requirement says "deny specific source IP" -> prioritize NACL or WAF, not SG deny (SG has no deny)
- Requirement says "traffic must stay on AWS network" -> prefer endpoint/private service patterns
- Requirement says "transitive routing" -> eliminate peering-only topologies

## Drill Set D: Route 53 quick choices

- Active-passive DR -> Failover
- Traffic percentage split -> Weighted
- Lowest response time by region -> Latency
- Country/region specific responses -> Geolocation

## Mini scorecard (daily)

- 20 networking questions attempted: [ ]
- Time per question under 75 seconds: [ ]
- Wrong answers due to concept confusion <= 3: [ ]
- Wrong answers due to misreading requirement <= 2: [ ]

## Last-mile reminder

If two options both work technically, SAA usually prefers:

1. Lower operational overhead
2. Simpler architecture
3. Better alignment with explicit constraint in the question
