# API Gateway + App-layer Security（考点速记）

## 1. API Gateway 端点类型

- Regional：区域内入口，可配合 Route 53 策略。
- Edge-optimized：借助 CloudFront 边缘访问，全球客户端友好。
- Private API：仅 VPC 内访问，常配 interface VPC endpoint。

## 2. User-Agent Header

- 是 HTTP header，不是 IAM identity。
- 可用于日志分析、WAF 规则匹配、基于 header 的策略。

## 3. Security Group vs WAF vs Network Firewall

- Security Group：L3/L4，IP/port/protocol，stateful，不能按 URL/domain 过滤。
- AWS WAF：L7，防 SQLi/XSS/bad bots，检查 header/query/path/body。
- AWS Network Firewall：VPC 级流量检查，可做 domain list 规则。

## 4. “只允许访问指定第三方域名”常见解法

- Network Firewall domain rules
- Route 53 Resolver DNS Firewall
- Proxy 方案

不要选：Security Group 直接按 URL/domain 过滤。
