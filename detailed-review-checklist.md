# AWS SAA-C03 详细复习清单（基于题库 PDF）

> 目标：把 `AWS Certified Solutions Architect Associate SAA-C03.pdf` 的高频考点转化为可执行的复习路径。  
> 使用方式：按周推进，每完成一项就打勾。每周至少完成 2 次计时刷题 + 1 次错题复盘。

## 0. 启动准备（Day 0）

- [ ] 明确考试时间窗口（建议 6-8 周）
- [ ] 创建错题本模板（字段：题号/服务/错因/正确思路/易混点）
- [ ] 在仓库建立 `practice-reflection/weekly-review-01.md`
- [ ] 设置每周固定复盘时间（建议周日）
- [ ] 确认刷题节奏：工作日 20-30 题，周末 60-100 题

## 1. 高频优先级（来自 PDF 题目分布）

### P0（最高优先）

- [ ] Amazon S3（存储类别、生命周期、加密、跨区域、访问控制、静态网站）
- [ ] Amazon EC2 + Auto Scaling + ELB（ALB/NLB、扩缩容策略、高可用）
- [ ] AWS Lambda（并发、异步、与 SQS/SNS/EventBridge 集成）
- [ ] Amazon RDS/Aurora（多可用区、只读副本、备份恢复、连接管理）
- [ ] VPC 基础（公私子网、NAT、路由、SG/NACL、VPC Endpoint）

### P1（第二梯队）

- [ ] DynamoDB（分区键、GSI/LSI、DAX、按需与预置容量）
- [ ] API Gateway + SQS + SNS（解耦、削峰、顺序保证 FIFO）
- [ ] CloudFront + Route 53（缓存、加速、路由策略、故障转移）
- [ ] IAM + KMS + Secrets Manager（最小权限、密钥与凭据轮换）
- [ ] CloudWatch + EventBridge + Config（监控、告警、合规检查）

### P2（补强）

- [ ] EFS/EBS 差异与场景
- [ ] Glue/Athena/Redshift/QuickSight 基础数据分析链路
- [ ] Organizations/多账号治理
- [ ] WAF/Shield/边界防护
- [ ] 成本优化策略（存储分层、计算选型、预留与弹性）

## 2. 六周执行版复习计划

## Week 1：存储 + 数据保护

- [ ] 精读并补充 `notes/s3.md`
- [ ] 梳理 S3 常见陷阱：一致性、访问策略、生命周期最优解
- [ ] 对比 EBS/EFS/S3 适配场景，更新 `service-comparison.md`
- [ ] 刷题 120 题（以 S3/EBS/EFS 为主）
- [ ] 输出错题复盘：`practice-reflection/weekly-review-01.md`

## Week 2：计算 + 弹性架构

- [ ] 精读并补充 `notes/ec2-auto-scaling-elb.md`
- [ ] 完整掌握 ALB/NLB/GLB 使用边界
- [ ] 整理 ASG 策略：目标追踪/步进/预测扩缩容
- [ ] 刷题 120 题（EC2/ASG/ELB/Lambda）
- [ ] 产出一页架构图到 `diagrams/`

## Week 3：数据库 + 缓存

- [ ] 精读并补充 `notes/rds-aurora-dynamodb.md`
- [ ] 建立 RDS/Aurora/DynamoDB/ElastiCache 选型表
- [ ] 高频考点：读写分离、故障切换、容量模型、热点分区
- [ ] 刷题 120 题（RDS/Aurora/DynamoDB）
- [ ] 错题归类：性能瓶颈类 vs 可用性类

## Week 4：网络 + 安全

- [ ] 精读并补充 `notes/vpc-networking.md`
- [ ] 精读并补充 `notes/iam-security.md`
- [ ] 梳理 VPC Endpoint / PrivateLink / TGW / NAT 网关边界
- [ ] 梳理 IAM policy 评估逻辑、跨账号访问、KMS 权限
- [ ] 刷题 150 题（VPC/IAM/KMS/Organizations）

## Week 5：Serverless + 集成 + 监控成本

- [ ] 精读并补充 `notes/serverless.md`
- [ ] 精读并补充 `notes/monitoring-cost-optimization.md`
- [ ] 打通 API Gateway -> SQS/SNS -> Lambda -> DB 的设计题套路
- [ ] 整理 CloudWatch/EventBridge/Config 常见题型
- [ ] 刷题 150 题（Serverless + Ops + Cost）

## Week 6：全真冲刺

- [ ] 完成 2 套全真模拟（严格计时）
- [ ] 每套做完 24 小时内完成错题二次复盘
- [ ] 把所有错题映射到 5 大 Domain
- [ ] 输出 `exam-readiness-checklist.md`（考前一页纸）
- [ ] 最后 3 天只看错题本 + 高频决策树

## 3. 按 Domain 的掌握标准（过线定义）

## Domain 1：Design Resilient Architectures

- [ ] 能判断单点故障并给出多 AZ/多 Region 改造方案
- [ ] 能在备份、恢复、RTO/RPO 约束下选正确服务
- [ ] 相关题正确率 >= 80%

## Domain 2：Design High-Performing Architectures

- [ ] 能针对吞吐、延迟、突发流量给出解耦与缓存方案
- [ ] 能区分读密集/写密集工作负载的数据库选型
- [ ] 相关题正确率 >= 80%

## Domain 3：Design Secure Applications and Architectures

- [ ] 能独立写出最小权限访问思路（身份、资源、网络三层）
- [ ] 熟悉密钥、凭据、日志审计与合规服务协作
- [ ] 相关题正确率 >= 85%

## Domain 4：Design Cost-Optimized Architectures

- [ ] 能解释同一需求下不同服务的成本差异
- [ ] 能给出至少 2 种降本方案并说明副作用
- [ ] 相关题正确率 >= 80%

## 4. 每日复习 SOP（90-120 分钟）

- [ ] 20 分钟：复盘前一天错题
- [ ] 40-60 分钟：专题刷题（20-30 题）
- [ ] 20 分钟：整理决策规则（为什么 A 对、B/C/D 错）
- [ ] 10 分钟：更新错题本和下一次复习队列

## 5. 错题复盘模板（建议复制到 weekly-review）

- [ ] 题目编号：
- [ ] 关联服务：
- [ ] 错因类型：概念混淆 / 审题不清 / 场景判断错误 / 粗心
- [ ] 正确决策关键字：
- [ ] 同类题识别信号：
- [ ] 下次遇到时的 10 秒判断规则：

## 6. 考前 7 天清单

- [ ] 只做高频错题，不再大规模开新题
- [ ] 每天复盘 3 个“高频混淆对”：
- [ ] S3 vs EFS vs EBS
- [ ] SQS vs SNS vs EventBridge
- [ ] RDS Multi-AZ vs Read Replica
- [ ] ALB vs NLB vs API Gateway
- [ ] IAM Policy vs Bucket Policy vs KMS Key Policy
- [ ] 睡眠和考试节奏按正式考试时间对齐

## 7. 与当前仓库的落地任务

- [ ] 新建 `practice-reflection/weekly-review-02.md` 到 `weekly-review-06.md`
- [ ] 为 `notes/` 下每个主题补充“常见错误选项解析”小节
- [ ] 在 `README.md` 增加“Study Roadmap”入口链接
- [ ] 在 `diagrams/` 至少补 3 张架构图（Web 三层、事件驱动、跨区域容灾）

---

如果你愿意，我下一步可以直接把这份清单拆成“明天就能执行的 Day 1- Day 7 打卡版”。
