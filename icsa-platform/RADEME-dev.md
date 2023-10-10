# 信息资产采集与安全评估系统（ICSA）

## 平台后端服务组件


* static为flask工程的静态目录，包括：字体、CSS、JavaScript及其他第三方JavaScript库
* templates为flask工程的模板文件目录
* utils为系统工具库
* views下面的模块分别为
  1. 系统日志icsa_log
  2. 系统任务icsa_action
  3. 系统策略icsa_benchmarks
  4. 系统插件icsa_plugins
  5. 资产assets
  6. 仪表盘dashboard
  7. 部门管理department_manager
  8. 数据分析ueba
  9. 资产监控monitor
  10. 系统用户users
  11. 角色管理roles
  12. 系统报表icsa_reports
  13. 系统文件icsa_staticfiles
  14. 系统组件icsa_components

### 开发环境部署

如果你使用了虚拟环境，则进入虚拟环境，关于Python虚拟环境的使用请参考文章：  
* [Python3的虚拟环境管理和包管理器PIP的详细介绍和使用](https://mp.weixin.qq.com/s/sq7hWN0OnjPkYse_798soQ)  
* [Python3的虚拟环境管理神器之pipenv、virtualenv、virtualenvwrapper详解](https://mp.weixin.qq.com/s/v6KuQj_OqCdPUpVGvf87Uw)  

1.生成依赖库列表
(python -m) pip freeze > requirements.txt

2.安装依赖库
(python -m) pip install -r requirements.txt


#### 代码规范和编排工具

这里使用了Python的代码规范检查工具以及代码编排工具：flake8、black、isort、autopep8，具体使用参考下面的文章
* [Python代码扫描：Python代码规范与错误检查的利器-flake8详解与实践](https://mp.weixin.qq.com/s/-ksoeCDJrrJ8togcGTOIGg)
* [Python代码扫描：一键格式化Python代码的黑魔法-black使用教程](https://mp.weixin.qq.com/s/Ib2iihh1s3YTfJrGYiROVQ)
* [Python代码扫描：导入语句自动排序工具-isort使用指南与示例](https://mp.weixin.qq.com/s/f_iFjSGVTC_3hNAvy6Q-Vg)
* [Python代码扫描：自动化修复Python代码风格的工具-autopep8详解与实例](https://mp.weixin.qq.com/s/ywE-12KYI-mj6p-G5HN6Vg)

### 生产环境部署

生产环境可以直接使用CentOS系统进行安装部署，但是，这里我在生产环境使用Docker部署，首先做成一个包含了ICSA系统的镜像，然后每次在需要部署的机器上安装好docker服务，然后加载镜像，启动容器即可。这样就避免了每次安装Python、项目依赖包、数据库服务等繁琐的操作。关于Docker的安装和使用请参考以下文章：
* [一、Docker：Linux/Windows在线安装Docker与命令大全总结](https://mp.weixin.qq.com/s/nRFy6K0RDvg2l6C8yM6SUQ)
* [二、Docker：Dockerfile的使用、指令详解和示例](https://mp.weixin.qq.com/s/KkJR2TaXMuNfLXsEO1qc0g)
* [三、Docker：Compose安装、使用、文件结构、配置参数与命令详解](https://mp.weixin.qq.com/s/xWfdYlHcc0YTyksedwBP2A)
* [十二、云主机-生产环境下离线安装Docker与应用部署](https://mp.weixin.qq.com/s/keGWRXxCeD9XZPiL-uaO4A)

#### 启动容器服务
每次启动服务器时启动docker服务  
service docker start/stop/status

运行容器  
docker run -i -t -p 8082:8082 -p 27019:27019 -p 80:80 -p 8087:8087 -p 8080:8080 -p 8086:8086 -p 9000:9000 -p 9191:9191 -p 9092:9092 --name jz_cec /bin/bash

如果已经运行，后面每次只需要执行启动命令即可  
docker start icsa

进入容器  
docker exec -it icsa /bin/bash

#### 认证方式启动MongoDB服务

mongod --auth -f /etc/mongod.conf

#### 启动各后端服务组件

* 进入目录icsa-api执行以下目录  
  python main.py "icsa-service"

* 进入目录icsa-platform执行以下目录  
  python main.py "icsa-platform"

* 进入目录icsa-ia执行以下目录  
  python main.py "icsa-ia"

* 进入目录icsa-helper执行以下目录  
  python main.py "icsa-helper"
