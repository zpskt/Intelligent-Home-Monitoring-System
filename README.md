# Intelligent-Home-Monitoring-System

智能家庭监控系统

## 项目介绍

智能家庭监控系统是一个集成了前端与后端技术的综合监控平台，旨在为用户提供全方位的家庭安全监控解决方案。系统主要由以下几个模块组成：

1. **前端界面**：
    - 使用Vue框架构建用户界面，提供直观的操作体验。
    - 支持模型管理、检测任务管理、报警事件管理、用户管理和模型训练等功能。
    - 提供用户友好的界面设计，确保用户能够轻松地进行各种操作。
    - 实现响应式设计，支持多种设备访问。
    - 使用Vuex进行状态管理，确保数据的一致性和可维护性。
    - 使用Vue Router进行路由管理，实现页面之间的无缝跳转。

2. **后端服务**：
    - 使用SpringBoot和Django框架构建后端服务，提供高效的数据处理和业务逻辑支持。
    - 包含鉴权模块、日志模块、模型训练管理、模型预测管理、用户管理和检测任务管理等功能。
    - 使用Spring Security进行安全控制，确保系统的安全性。
    - 使用Django的认证系统进行用户管理，支持用户注册、登录和权限控制。
    - 使用RESTful API进行前后端交互，确保数据传输的高效性和安全性。

3. **数据存储**：
    - 使用MySQL数据库存储用户信息、模型信息、检测任务信息、报警事件信息、模型训练信息、模型预测信息和日志信息。
    - 使用Redis存储JWT用于用户鉴权验证。
    - 使用ORM（对象关系映射）进行数据库操作，简化代码并提高可维护性。
    - 使用数据库索引优化查询性能，提高系统的响应速度。

4. **检测模块**：
    - 根据数据库中的参数训练模型。
    - 执行检测任务并生成相应的结果。
    - 支持个性化模型训练，以满足不同用户的需求。
    - 使用PyTorch等深度学习框架进行模型训练和预测。
    - 实现模型的版本控制，确保模型的稳定性和可追溯性。

5. **报警与通知**：
    - 提供多种报警通知方式，包括手机和短信通知、微信公众号通知和邮件通知，确保用户能够及时收到报警信息。
    - 使用第三方服务（如Twilio、WeChat API、SMTP）进行通知发送，确保通知的可靠性和及时性。
    - 实现通知的配置管理，允许用户自定义通知方式和接收人。

6. **负载均衡**：
    - 配置接口路由实现负载均衡，提高系统的响应速度和稳定性。
    - 实现本地图片的高效映射，优化资源管理。
    - 使用Nginx或HAProxy进行负载均衡配置，确保系统的高可用性。

## 技术架构

1. **Vue 前端**：
    - 用户通过 Vue 前端进行操作
    - [x] 模型管理与维护
    - [x] 检测任务管理
    - [x] 报警事件管理与查看
    - [x] 用户管理
    - [x] 模型训练管理
    - [x] 模型预测管理

2. **SpringBoot 后端**：
    - [x] 模型管理与维护
    - [x] 检测任务管理
    - [x] 报警事件管理与查看
    - [x] 用户管理
    - [x] 模型训练管理
    - [x] 模型预测管理
    - [x] 鉴权模块
    - [x] 日志模块

3. **Redis**：
    - [x] 存储 JWT 用于验证。

4. **MySQL 数据库**：
    - [x] 存储用户信息、
    - [x] 模型信息、
    - [x] 检测任务信息
    - [x] 报警事件信息。
    - [x] 存储模型训练信息
    - [x] 模型预测信息。
    - [x] 存储日志信息。

5. **Django 后端**：
    - [x] 鉴权模块
    - [x] 日志模块
    - [x] 模型训练管理
    - [x] 模型预测管理
    - [x] 模型管理与维护
    - [x] 检测任务管理与执行
    - [x] 报警事件管理

6. **检测模块**：
    - [x] 根据数据库中参数训练模型
    - [x] 执行检测任务
    - [x] 个性化模型训练

7. **报警与持久化**：
    - [x] 手机和短信通知
    - [x] 微信公众号通知
    - [x] 邮件通知

8. **负载均衡**：
    - [x] 接口路由配置及负载均衡
    - [x] 本地图片映射

## 任务监控机制

### Spring Boot 后端

- **TaskController**:
  - 提供任务启动和状态更新的API。
  - 使用`TaskStatus`类来存储任务的状态信息。
  - 通过`startTask`方法启动任务，并将任务状态初始化为`PENDING`。
  - 通过`updateTaskStatus`方法更新任务状态。

- **TaskMonitorService**:
  - 定期检查任务状态，每5秒执行一次。
  - 如果任务状态为`RUNNING`且进度未达到100%，则检查任务是否假死。
  - 如果30秒内没有进度更新，则认为任务假死，并采取相应措施（如重启任务或报警）。

### Python 后端

- **app.py**:
  - 提供任务启动的API。
  - 使用多线程来执行任务。
  - 定期报告任务状态给Spring Boot后端。
  - 任务状态包括`PENDING`、`RUNNING`、`COMPLETED`和`FAILED`。
  - 通过`report_task_status`函数将任务状态发送到Spring Boot后端。

## 安全漏洞与风险

1. **输入验证**：
    - 对所有用户输入进行严格的验证和过滤，防止SQL注入、XSS攻击等安全漏洞。
    - 使用正则表达式和数据校验库进行输入验证。

2. **数据加密**：
    - 对敏感数据（如用户密码、JWT等）进行加密存储，确保数据的安全性。
    - 使用HTTPS协议进行数据传输，防止数据在传输过程中被窃取。

3. **权限管理**：
    - 实现细粒度的权限控制，确保用户只能访问其权限范围内的资源。
    - 使用角色基础访问控制（RBAC）进行权限管理。

4. **日志记录**：
    - 记录所有关键操作的日志，便于追踪和审计。
    - 使用日志框架（如Logback、Log4j）进行日志记录。

5. **异常处理**：
    - 对所有可能的异常情况进行处理，防止系统崩溃或泄露敏感信息。
    - 使用try-catch块进行异常处理，并记录异常日志。

6. **第三方服务**：
    - 对所有第三方服务进行安全评估，确保其安全性。
    - 使用安全的第三方服务，并定期更新其版本。

7. **代码审查**：
    - 定期进行代码审查，发现并修复潜在的安全漏洞。
    - 使用静态代码分析工具进行代码审查。

8. **安全培训**：
    - 对开发人员进行安全培训，提高其安全意识。
    - 定期进行安全培训，并进行安全测试。

9. **备份与恢复**：
    - 定期进行数据备份，防止数据丢失。
    - 实现数据恢复机制，确保数据的可用性。

10. **安全更新**：
    - 定期更新所有依赖库和框架，修复已知的安全漏洞。
    - 使用自动化工具进行安全更新，并进行回归测试。