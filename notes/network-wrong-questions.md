下面是我们目前对话中的 **AWS SAA 知识点错题整理版**。我按考试高频主题整理，并把你特别提到的 **dynamic data 由 ALB 处理、WAF、GWLB** 也加进来了。

---

# 一、核心架构判断口诀

## 1. 静态内容 + 动态内容

经典架构：

```text
User
 ↓
Route 53
 ↓
CloudFront
 ↓                    ↓
S3 静态内容             ALB 动态内容
                       ↓
                     EC2 / ECS / EKS
```

| 内容类型                         | 推荐服务                      |
| ---------------------------- | ------------------------- |
| Static data，例如图片、CSS、JS、视频   | S3 + CloudFront           |
| Dynamic data，例如 API、登录、查询数据库 | ALB + EC2/ECS/EKS         |
| 全球低延迟访问                      | CloudFront                |
| 多 origin 分发                  | CloudFront cache behavior |

重点：

```text
Static → S3
Dynamic → ALB
CloudFront 可以同时配置 S3 和 ALB 作为 origins
```

---

# 二、Route 53 与 DNS

## 1. Public Hosted Zone

用于公网 DNS。

场景：

```text
公网网站
域名迁移
DNS provider 故障
互联网用户访问 example.com
```

正确选择：

```text
Route 53 Public Hosted Zone
```

错误理解：

```text
Resolver endpoint 不是 DNS hosting
```

---

## 2. Private Hosted Zone

用于 VPC 内部 DNS。

场景：

```text
app.internal
db.internal
只允许 VPC 内解析
```

不能解决：

```text
VPC 查询 on-premises DNS
```

因为 Private Hosted Zone 是：

```text
AWS 自己保存 DNS 记录
```

不是转发到本地 DNS。

---

## 3. Route 53 Resolver Inbound / Outbound

这是你之前问得比较多的重点。

| 方向                  | 服务                         |
| ------------------- | -------------------------- |
| AWS VPC 查询本地 DNS    | Resolver Outbound Endpoint |
| 本地数据中心查询 AWS 私有 DNS | Resolver Inbound Endpoint  |

记忆口诀：

```text
Outbound：AWS 出去问本地 DNS
Inbound：本地进来问 AWS DNS
```

---

## 4. Geolocation vs Geoproximity

| 场景            | 选择                   |
| ------------- | -------------------- |
| 按国家/地区控制内容版权  | Geolocation Routing  |
| 按距离、延迟、靠近哪个区域 | Geoproximity Routing |

题目关键词：

```text
distribution rights
copyright
country restriction
```

选：

```text
Route 53 Geolocation
```

---

# 三、负载均衡器 ALB / NLB / GWLB

## 1. ALB：Application Load Balancer

第 7 层负载均衡器。

适合：

* HTTP
* HTTPS
* Web 应用
* API
* 动态内容
* Path-based routing
* Host-based routing
* WAF 集成

典型场景：

```text
Internet
 ↓
ALB
 ↓
EC2 / ECS / EKS
```

重点：

```text
Dynamic data 通常由 ALB 后面的应用服务器处理
```

ALB 不适合：

* 固定 IP 白名单
* UDP
* TCP 原始流量
* 防火墙设备透明转发

---

## 2. NLB：Network Load Balancer

第 4 层负载均衡器。

适合：

* TCP
* UDP
* TLS
* 超高性能
* 低延迟
* 固定 IP
* Elastic IP
* 客户防火墙白名单

看到题目说：

```text
clients can only allow specific IP addresses
static IP
firewall allowlist
UDP application
```

优先想到：

```text
NLB + Elastic IP
```

---

## 3. GWLB：Gateway Load Balancer

这个是你要求补充的重点。

GWLB 用于：

```text
部署、扩展、管理第三方网络安全设备
```

例如：

* 防火墙 appliance
* IDS
* IPS
* 深度包检测设备
* 流量审计设备

典型架构：

```text
VPC traffic
 ↓
Gateway Load Balancer Endpoint
 ↓
Gateway Load Balancer
 ↓
Firewall appliances
 ↓
Destination
```

GWLB 的特点：

| 特性           | 说明                |
| ------------ | ----------------- |
| 层级           | Layer 3 / Layer 4 |
| 主要用途         | 透明插入安全设备          |
| 协议           | 使用 GENEVE 封装      |
| 端口           | UDP 6081          |
| 目标           | 第三方虚拟防火墙、IDS/IPS  |
| 是否处理 HTTP 路由 | 不处理               |
| 是否替代 ALB     | 不替代               |
| 是否替代 WAF     | 不替代               |

考试中看到：

```text
third-party firewall appliances
centralized inspection
transparent network inspection
IDS/IPS
security appliance fleet
```

优先想到：

```text
Gateway Load Balancer
```

---

## ALB vs NLB vs GWLB

| 服务   | 主要用途              | 高频关键词                                             |
| ---- | ----------------- | ------------------------------------------------- |
| ALB  | Web/API 动态流量      | HTTP、HTTPS、path、host、WAF                          |
| NLB  | 高性能 TCP/UDP、固定 IP | UDP、static IP、EIP、allowlist                       |
| GWLB | 安全设备流量检查          | firewall appliance、IDS、IPS、transparent inspection |

---

# 四、WAF / Shield / Network Firewall / GWLB

这是 SAA 安全题最容易混的地方。

## 1. AWS WAF

Web Application Firewall。

防护对象：

* CloudFront
* ALB
* API Gateway
* AppSync

主要防：

* SQL Injection
* XSS
* IP allowlist/blocklist
* Rate limiting
* Bot 控制
* HTTP header/path/query 条件

看到：

```text
SQL injection
cross-site scripting
HTTP/HTTPS
API Gateway
ALB
CloudFront
IP set
```

选：

```text
AWS WAF
```

---

## 2. AWS Shield

主要防 DDoS。

| 服务              | 用途                  |
| --------------- | ------------------- |
| Shield Standard | 免费自动 DDoS 基础防护      |
| Shield Advanced | 高级 DDoS 防护，适合企业关键应用 |

看到：

```text
DDoS
SYN flood
UDP flood
volumetric attack
```

选：

```text
AWS Shield
```

不要把 Shield 和 WAF 混淆：

```text
WAF 防 Web 攻击
Shield 防 DDoS
```

---

## 3. AWS Network Firewall

VPC 级托管网络防火墙。

适合：

* 控制 VPC 出站流量
* 限制只能访问指定域名
* 域名 allowlist
* Stateful inspection
* Suricata-compatible rules
* 私有子网访问互联网前检查

你之前那题：

```text
EC2 在 private subnet
只能访问批准的第三方软件仓库 URL
其他互联网流量阻止
```

正确是：

```text
AWS Network Firewall + domain list rule groups
```

---

## 4. GWLB 和 Network Firewall 的区别

| 场景                                              | 选择                    |
| ----------------------------------------------- | --------------------- |
| 使用 AWS 托管防火墙服务                                  | AWS Network Firewall  |
| 使用 Palo Alto / Fortinet / Check Point 等第三方防火墙设备 | Gateway Load Balancer |
| 按 URL/domain 控制出站                               | AWS Network Firewall  |
| 透明插入 appliance fleet                            | GWLB                  |
| Web 层 SQLi/XSS 防护                               | AWS WAF               |

---

# 五、CloudFront

## 1. CloudFront + S3 + ALB

CloudFront 可以有多个 origin：

```text
/static/* → S3
/api/*    → ALB
```

适合：

* 全球用户低延迟
* 静态内容缓存
* 动态内容加速
* 统一域名入口

---

## 2. CloudFront + WAF + S3

如果要求：

```text
所有网站流量都必须经过 WAF
```

必须防止用户绕过 CloudFront 直接访问 S3。

正确架构：

```text
User
 ↓
CloudFront + WAF
 ↓
OAI / OAC
 ↓
Private S3 Bucket
```

重点：

```text
S3 没有 Security Group
```

S3 权限控制靠：

* Bucket Policy
* IAM Policy
* OAI / OAC

新版更推荐：

```text
OAC，Origin Access Control
```

但考试老题经常出现：

```text
OAI，Origin Access Identity
```

---

## 3. CloudFront vs Global Accelerator

| 场景                | 选择                 |
| ----------------- | ------------------ |
| HTTP/HTTPS 内容分发   | CloudFront         |
| S3 静态内容加速         | CloudFront         |
| 多 origin：S3 + ALB | CloudFront         |
| TCP/UDP 全球加速      | Global Accelerator |
| 固定 Anycast IP     | Global Accelerator |
| 游戏、VoIP、UDP 应用    | Global Accelerator |

---

# 六、Global Accelerator

适合：

```text
全球用户访问 TCP/UDP 应用
提高性能和可用性
快速故障转移
```

支持 endpoint：

* ALB
* NLB
* EC2
* Elastic IP

不支持直接把 S3 当 endpoint。

你之前那题 UDP 应用部署在本地数据中心：

```text
Global Accelerator → NLB → on-premises endpoints
```

因为：

```text
NLB 支持 UDP
ALB 不支持 UDP
CloudFront 不适合普通 UDP 应用
```

---

# 七、VPC 与私有网络

## 1. Public Subnet vs Private Subnet

区别不是名字，而是路由表。

Public subnet：

```text
0.0.0.0/0 → Internet Gateway
```

Private subnet：

```text
没有直接到 IGW 的默认路由
```

---

## 2. 私有 EC2 对公网提供 Web 服务

如果 EC2 必须在 private subnet，但要让公网访问网站：

正确架构：

```text
Internet
 ↓
Internet-facing ALB in public subnets
 ↓
EC2 in private subnets
```

不要让 DNS 指向 private EC2。

不要用 NAT Gateway 做入站访问。

---

## 3. NAT Gateway

作用：

```text
Private subnet 里的资源主动访问互联网
```

例如：

* 下载补丁
* 调用外部 API
* 访问软件仓库

不能用于：

```text
让互联网主动访问 private EC2
```

记忆：

```text
NAT Gateway 是出去，不是进来
```

---

## 4. VPC Peering

要求：

```text
两个 VPC CIDR 不能重叠
```

且：

```text
不支持 transitive routing
```

VPC CIDR 合法范围：

```text
/16 到 /28
```

所以：

```text
/32 不能作为 VPC CIDR
```

---

## 5. Transit Gateway

适合：

```text
大量 VPC
多账号
集中网络管理
hub-and-spoke
```

看到：

```text
hundreds of AWS accounts
many VPCs
centralized networking account
most operationally efficient
```

选：

```text
AWS Transit Gateway
```

---

# 八、Lambda / API Gateway / Serverless

## 1. API Gateway + Lambda

适合：

```text
HTTPS API endpoint
无服务器
低运维
自动扩展
```

例如 badge reader 通过 HTTPS 上传刷卡事件：

```text
Badge Reader
 ↓
API Gateway
 ↓
Lambda
 ↓
DynamoDB
```

---

## 2. Lambda Provisioned Concurrency vs Reserved Concurrency

| 功能                      | 作用                    |
| ----------------------- | --------------------- |
| Provisioned Concurrency | 预热 Lambda，降低冷启动，保证低延迟 |
| Reserved Concurrency    | 限制/保留并发额度，不解决冷启动      |

看到：

```text
consistently low latency
peak traffic
least operational overhead
```

选：

```text
API Gateway + Lambda Provisioned Concurrency
```

---

## 3. Lambda 访问 VPC / On-premises

Lambda 默认不在你的 VPC 里。

如果 Lambda 要访问：

* 私有 RDS
* 私有 EC2
* On-premises database
* Direct Connect 后面的私有资源

需要：

```text
Configure Lambda to run in VPC
```

然后通过：

```text
VPC route table → VGW/TGW/DX/VPN → on-premises
```

---

# 九、EKS 私有集群

题目：

```text
EKS endpoint private access = true
public access = false
nodes in private subnets
nodes cannot join cluster
```

原因通常是：

```text
节点无法私有访问 EKS control plane / AWS services
```

解决：

```text
Create interface VPC endpoints
```

常见 endpoints：

* EKS
* EC2
* ECR API
* ECR DKR
* STS
* CloudWatch Logs

注意：

```text
Security Group 允许 outbound 不等于网络一定通
```

SG 只是防火墙。

真正还需要：

* Route table
* NAT Gateway
* VPC Endpoints
* DNS resolution

---

# 十、API Gateway 发布新版本

如果要求：

```text
minimal customer impact
minimal data loss
release new API version
```

选：

```text
API Gateway Canary Release
```

可以：

```text
5% traffic → 新版本
95% traffic → 旧版本
```

验证成功后再推广。

不要直接 overwrite production。

---

# 十一、SAA 高频易错对比表

## DNS 类

| 需求           | 选择                           |
| ------------ | ---------------------------- |
| 公网域名托管       | Route 53 Public Hosted Zone  |
| VPC 内私有 DNS  | Route 53 Private Hosted Zone |
| AWS 查询本地 DNS | Resolver Outbound Endpoint   |
| 本地查询 AWS DNS | Resolver Inbound Endpoint    |
| 版权/国家内容控制    | Route 53 Geolocation         |
| 按距离路由        | Route 53 Geoproximity        |

---

## 安全类

| 需求                  | 选择                        |
| ------------------- | ------------------------- |
| SQL Injection / XSS | AWS WAF                   |
| DDoS                | AWS Shield                |
| 出站域名控制              | AWS Network Firewall      |
| 第三方防火墙 appliance    | Gateway Load Balancer     |
| S3 防直接访问            | OAI / OAC + Bucket Policy |
| 大量 IP 白名单保护 ALB     | AWS WAF IP Set            |

---

## 负载均衡类

| 需求                       | 选择                            |
| ------------------------ | ----------------------------- |
| Web/API HTTP/HTTPS       | ALB                           |
| 固定 IP / EIP / UDP        | NLB                           |
| 第三方安全设备流量检查              | GWLB                          |
| EC2 健康检查和避免 unhealthy 实例 | ALB Target Group Health Check |

---

## 全球加速类

| 需求                | 选择                 |
| ----------------- | ------------------ |
| S3 静态内容全球加速       | CloudFront         |
| S3 + ALB 多 origin | CloudFront         |
| TCP/UDP 全球加速      | Global Accelerator |
| 固定 Anycast IP     | Global Accelerator |

---

## Serverless 类

| 需求               | 选择                      |
| ---------------- | ----------------------- |
| HTTPS API 无服务器入口 | API Gateway             |
| 事件处理             | Lambda                  |
| 稳定低延迟 Lambda     | Provisioned Concurrency |
| 控制 Lambda 最大并发   | Reserved Concurrency    |
| 高频事件存储           | DynamoDB                |

---

# 十二、你目前最需要记住的几句口诀

```text
Static data → S3 + CloudFront
Dynamic data → ALB + EC2/ECS/EKS
```

```text
WAF 防 Web 攻击，Shield 防 DDoS
```

```text
NAT Gateway 是 private subnet 出去，不是让外面进来
```

```text
Outbound Resolver：AWS 出去查本地 DNS
Inbound Resolver：本地进来查 AWS DNS
```

```text
NLB 才有固定 IP，ALB 没有 Elastic IP
```

```text
Gateway Load Balancer 用于第三方防火墙 appliance
```

```text
Network Firewall 控制 VPC 出站流量，WAF 控制 Web 请求
```

```text
很多 VPC、多账号互联 → Transit Gateway
```

```text
版权/国家限制 → Route 53 Geolocation
距离/就近访问 → Geoproximity
```

```text
Lambda 访问私有资源 → 放进 VPC
```

```text
EKS 私有节点无法加入 → 检查 VPC Endpoint / NAT / 私有访问路径
```
