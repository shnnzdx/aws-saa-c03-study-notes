# Load Balancing + Certificates（考点速记）

## 1. ALB Listener Redirect

- 题目关键词：HTTP -> HTTPS、旧域名到新域名、旧路径到新路径。
- 正确术语：`listener rule with redirect action`。
- 常见动作：301 / 302 redirect。
- 易区分：
- redirect：跳转 URL
- path-based routing：按路径转发目标组
- host-based routing：按域名转发目标组
- fixed-response：返回静态响应

## 2. ACM-issued vs Imported

- ACM-issued：ACM 签发，支持 managed renewal。
- Imported：外部 CA 证书导入，需手动 reimport。

## 3. API Gateway / CloudFront 证书区域规则

- Regional API Gateway custom domain：证书在同 Region。
- Edge-optimized API Gateway custom domain：证书在 `us-east-1`。
- CloudFront custom domain：证书在 `us-east-1`。

## 4. DNS 流量 vs CDN 流量

- DNS server 流量（UDP/TCP 53）负载均衡：NLB（L4，支持 UDP/TCP）。
- Web 内容加速（HTTP/HTTPS）：CloudFront（CDN）。
- 不要把 CloudFront 当 DNS 查询处理服务。
