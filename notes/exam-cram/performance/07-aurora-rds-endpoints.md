# Aurora / RDS Endpoints（考点速记）

- Writer/Cluster endpoint：写请求（INSERT/UPDATE/DELETE/DDL）。
- Reader endpoint：只读查询，分担读流量。
- Instance endpoint：连接某一台特定实例。
- Custom endpoint：自定义实例组给特定 workload。

题目关键词：

- 写入主库 -> writer endpoint
- 扩展读查询 -> reader endpoint
- 运维排障指定实例 -> instance endpoint
- 特定实例组业务隔离 -> custom endpoint
