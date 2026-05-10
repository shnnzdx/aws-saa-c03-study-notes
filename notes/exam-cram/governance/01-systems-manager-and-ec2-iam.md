# Systems Manager + EC2 IAM（考点速记）

## 1. Run Command

- 用途：在 managed nodes 上远程批量执行命令，不需要 SSH/RDP。
- 典型关键词：批量执行脚本、远程执行命令、不登录实例、审计命令记录。
- 前提：SSM Agent 运行正常；实例是 managed instance；IAM 权限到位。
- 易混淆：
- Run Command：批量命令执行
- Session Manager：交互式登录
- Patch Manager：补丁管理
- State Manager：持续配置状态

## 2. Default Host Management Configuration

- 作用：让 Systems Manager 自动管理 EC2，减少逐台配置 instance profile 的工作。
- 特点：Region 级开启；依赖 SSM Agent；常见默认角色为 `AWSSystemsManagerDefaultEC2InstanceManagementRole`。
- 常见考法：大规模 EC2 纳管、减少手工挂 SSM 权限。

## 3. EC2 Instance Profile / IAM Role 限制

- 一个 EC2 同时只能关联一个 instance profile。
- 一个 instance profile 只能包含一个 IAM role。
- 不能同时给一台 EC2 挂两个 IAM roles。
- 要扩权限：改现有 role policy 或替换 role/profile。
