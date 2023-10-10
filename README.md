# ABOUT

**【关于我们】**

* [Articulate v1.0](https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q)
* [Articulate v2.0](https://mp.weixin.qq.com/s/V5Axn-ZWi22ubh5Jiocb9g)

[![](https://img.shields.io/badge/GitHub-zrf--rocket-blue?logo=gitpod)](https://github.com/zrf-rocket)
[![](https://img.shields.io/badge/Gitee-SteveRocket-pink)](https://gitee.com/SteveRocket/)
![CTO Plus](https://img.shields.io/badge/微信公众号：CTO%20Plus-8A2BE2) 🥰

<img src="./static/wechat.png" style="width:500px">


**【代码工程系列】**

* [Python和Go的设计模式](https://github.com/zrf-rocket/DesignPattern)
    * GitHub：https://github.com/zrf-rocket/DesignPattern
    * Gitee：https://gitee.com/SteveRocket/design_pattern

* [Python、Go的编码技巧cookbook](https://github.com/zrf-rocket/CookBook)
    * GitHub：https://github.com/zrf-rocket/CookBook
    * Gitee：https://gitee.com/SteveRocket/cook-book

* [Go代码示例](https://github.com/zrf-rocket/PracticeGo)
    * GitHub：https://github.com/zrf-rocket/PracticeGo
    * Gitee：https://gitee.com/SteveRocket/practice_go

* [Python代码示例](https://github.com/zrf-rocket/PracticePython)
    * GitHub：https://github.com/zrf-rocket/PracticePython
    * Gitee：https://gitee.com/SteveRocket/practice_python

* [Python Web框架的示例代码](https://github.com/zrf-rocket/PythonFramework)
    * GitHub：https://github.com/zrf-rocket/PythonFramework
    * Gitee：https://gitee.com/SteveRocket/python_framework

* [Rust代码示例](https://github.com/zrf-rocket/PracticeRust)
    * GitHub：https://github.com/zrf-rocket/PracticeRust
    * Gitee：https://gitee.com/SteveRocket/practice_rust

* [Vue代码示例](https://github.com/zrf-rocket/PracticeVue)
    * GitHub：https://github.com/zrf-rocket/PracticeVue
    * Gitee：https://gitee.com/SteveRocket/practice_vue

* [前端代码示例](https://github.com/zrf-rocket/PracticeFronted)
    * GitHub：https://github.com/zrf-rocket/PracticeFronted
    * Gitee：https://gitee.com/SteveRocket/practice_fronted

* [Python自动化测试框架](https://github.com/zrf-rocket/PythonTestAutomationFramework)
    * GitHub：https://github.com/zrf-rocket/PythonTestAutomationFramework
    * Gitee：https://gitee.com/SteveRocket/python_test_automation_framework

* [Python和Go的算法代码示例](https://github.com/zrf-rocket/Algorithms)
    * GitHub：https://github.com/zrf-rocket/Algorithms
    * Gitee：https://gitee.com/SteveRocket/Algorithms

* [Python和Go的数据结构代码示例](https://github.com/zrf-rocket/DataStructure)
    * GitHub：https://github.com/zrf-rocket/DataStructure
    * Gitee：https://gitee.com/SteveRocket/data_structure

* [编码规范](https://github.com/zrf-rocket/DevGuide)
    * GitHub：https://github.com/zrf-rocket/DevGuide
    * Gitee：https://gitee.com/SteveRocket/develop_guide

* [编码安全规范](https://github.com/zrf-rocket/SecGuide)
    * GitHub：https://github.com/zrf-rocket/SecGuide
    * Gitee：https://gitee.com/SteveRocket/security_guide

**【产品系列】**

* [主机监控系统-日志收集与报警管理系统（SIEM）](https://github.com/zrf-rocket/SIEM)
    * GitHub：https://github.com/zrf-rocket/SIEM
    * Gitee：https://gitee.com/SteveRocket/siem

* [安全运营中心（SOC）-终端侦测与响应系统（EDR）](https://github.com/zrf-rocket/EDR_SOC)
    * GitHub：https://github.com/zrf-rocket/EDR_SOC
    * Gitee：https://gitee.com/SteveRocket/edr_soc

* [DevSecOps-SDLC](https://github.com/zrf-rocket/DevSecOps-SDLC)
    * GitHub：https://github.com/zrf-rocket/DevSecOps-SDLC
    * Gitee：https://gitee.com/SteveRocket/dev-sec-ops-sdlc

* [AI图像识别-智能缺陷检测系统]()
    * [基于AI图像识别的工业缺陷检测应用系统（GPU&FPGA）](https://mp.weixin.qq.com/s/04qefQFg-Pg1Gcqq1vBLQQ)
    * [基于AI图像识别的智能缺陷检测系统，在钢铁行业的应用-技术方案](https://mp.weixin.qq.com/s/dSHbnuOwQZzE4CvPr1JYjg)

# 信息资产采集与安全评估系统（ICSA）、安全分析平台（资产安全管理系统、云资产安全管理平台、云安全监控）

### 概述

Information Collection and Security Assessment（简称：ICSA） 信息资产采集与安全评估系统
同时，应用场景还可以作为

1. 企业安全分析平台、SIEM，系统提供日志、安全事件等多维度信息收集与监控、集中化管理安全事件，以供企业安全部门、安全分析师做安全审计、溯源取证等使用。
2. 资产安全管理系统、CMDB，供运维部门做资产统一监控和管理，以及统一的配置管理。
3. 云资产安全管理平台、云安全监控，供企业管理云上的资产，以及云上的资产安全诊断问题。
4. 等其他使用场景。

### 功能特性

1. 日志审计
    1. syslog
    2. 工业系统MES日志
    3. 应用日志
2. 主机监控
    1. 整合了Zabbix、Prometheus等监控系统，以及告警日志。
    2. 采用自研的探针（Agent）主机性能监控：CPU、内存、磁盘、进程（资源占用）、注册表、网络。
    3. 主机信息监控：主板信息。
    4. Windows安全配置核查、基线核查、安全日志。
    5. Linux安全配置核查、基线核查、日志。
    6. 云资产监测。
    7. 应用监测：应用安装清单、应用性能、应用日志。
    8. 用户登录错误次数过多行为。
    9. 移动介质行为。
3. 主机脆弱性评估与安全监测
    1. 应用安全配置核查。
    2. AD安全监测。
    2. 主机脆弱性评估。
    3. 后门检测。
    4. Webshell检测。
    5. 恶意文件扫描。
4. 自动化运维
    1. 整合ansible批量管理资产。
5. 数据库审计
    1. MySQL日志审计
    2. Redis日志审计
    3. Elasticsearch日志审计
6. 资产管理
    1. 按照资产业务属性、重要性分类管理。
    2. 支持资产的批量导入导出。
    3. 资产的安全等级。
7. 告警
    1. 平台统一告警管理。
    2. 企业微信告警。
    3. 邮箱告警。
8. 超轻量级的Agent
    1. 良好的跨平台性，支持Windows XP以上、Linux、MacOS、云主机、国产操作系统。
    2. 低耗：轻量级的Agent内存占用不到10M、CPU占用不到5%。
    3. 安装包大小不超过50M。
    4. 侵入式无感知无干扰（后台自动化升级、知识库自动同步、系统后台进程）。
9. 支持定制化开发

### 环境版本

平台后端采用最新的Python版本Python3.12，以及Flask+Tornado+MongoDB+Jinjia2+JQuery+Echarts+Nginx+Kafka等技术栈的资产安全分析与管理平台（资产安全管理系统、云资产安全管理平台）。

### 架构

1. 平台端采用前后端不分离模式。
2. 采用C/S、B/S双融合模式，根据实际情况可以选择安装Agent也可以不安装。

#### 组件

1. icsa-platform
   用于平台端提供后台接口服务，用于前端页面展示服务。
2. icsa-ia
   平台后端安全分析服务。
3. icsa-helper
   平台后端定时任务。
4. icsa-service
   后台API服务。
5. icsa-edr
   用于采集和监控主机。

#### 环境部署
参考文档：[开发与生产环境部署说明](icsa-platform/RADEME-dev.md)