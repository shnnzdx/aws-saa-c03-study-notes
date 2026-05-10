# S3 Data Protection（考点速记）

## 1. Versioning

- 价值：误删恢复、误覆盖恢复、保留历史版本。
- 删除未指定 version ID 时，常见行为是插入 delete marker。
- 与 Object Lock / MFA Delete / Lifecycle 经常组合考。

## 2. KMS Encryption + SSE-KMS

- 解决：数据保密性（confidentiality）、密钥控制、审计。
- 不解决：防删、防覆盖、替代 versioning。
- 下载 SSE-KMS 对象常需 `kms:Decrypt` 权限。

## 3. S3 可用性与持久性

- S3 Standard 常见指标：11 个 9 持久性，99.99% 可用性。
- 适合 object storage，不是 EBS 块存储，不是 EFS 共享文件系统。

## 4. 高频选择题映射

- 误删恢复 -> S3 Versioning
- 防篡改/合规保留 -> S3 Object Lock
- 删除需要额外验证 -> MFA Delete
- 数据静态加密 -> SSE-S3 / SSE-KMS
