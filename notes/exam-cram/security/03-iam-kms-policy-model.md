# IAM + KMS Policy Model（考点速记）

## 1. KMS key policy vs IAM trust policy vs identity-based policy

- KMS key policy：挂在 KMS key 上，控制谁可以使用该 key（resource-based）。
- IAM trust policy：挂在 role 上，控制谁能 `sts:AssumeRole`。
- IAM identity-based permissions policy：挂在 user/group/role 上，控制这个身份能做什么操作。

## 2. 高频判断

- 问“谁能 assume role” -> trust policy。
- 问“谁能使用 KMS key” -> key policy。
- 问“该 user/role 能做什么” -> identity-based policy。

## 3. Cross-account role 放置位置

- 角色通常建在被访问资源所在账户（target/trusting account）。
- 访问方账户的主体去 assume 目标账户角色。
- trust policy 决定“谁可进入”，permissions policy 决定“进去后能做什么”。
