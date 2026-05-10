# Final Exam Memory Cards

- Run Command：不 SSH，批量远程执行命令。
- Session Manager：安全交互式登录，不需要 bastion。
- ALB URL 跳转：listener redirect action（不是 replace URL text）。
- ACM-issued：自动续期；Imported：手动 reimport。
- Regional API Gateway 证书：同 Region。
- CloudFront/edge-optimized API 证书：us-east-1。
- KMS key policy：谁能用 key。
- IAM trust policy：谁能 assume role。
- IAM permissions policy：assume 后能做什么。
- S3 Versioning：误删/误覆盖恢复。
- SSE-KMS：保密性，不防删除。
- DNS 流量负载均衡：NLB；Web 加速：CloudFront。
- NACL stateless：记得放行 ephemeral ports 回包。
- Aurora writer endpoint=写；reader endpoint=读。
- Cross-account role：通常建在资源账户。
- Control Tower landing zone：management account 管理。
- EC2 同时只能一个 instance profile/role。
- Security Group 不能按 URL/domain 过滤。
