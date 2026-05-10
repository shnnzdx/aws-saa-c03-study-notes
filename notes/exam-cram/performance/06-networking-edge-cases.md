# Networking Edge Cases（考点速记）

## Ephemeral Ports

- SG 是 stateful：回包自动放行。
- NACL 是 stateless：回包也要显式允许。
- NACL 场景下常见问题：漏放行 ephemeral port range 导致连接失败。

常见范围（题目可能给线索）：

- Linux 常见：32768-61000
- Windows Server 2008+：49152-65535
- ELB/NAT Gateway/Lambda 常见：1024-65535
