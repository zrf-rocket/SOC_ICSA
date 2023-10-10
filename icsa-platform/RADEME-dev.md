# 信息资产采集与安全评估系统（ICSA）

## 平台后端服务组件




### 开发环境部署

1.生成支持库列表
(python -m) pip freeze > requirements.txt

2.安装支持库
(python -m) pip install -r requirements.txt

### 生产环境部署

service docker start/stop/status

#### 启动容器服务
docker run -i -t -p 8082:8082 -p 27019:27019 -p 80:80 -p 8087:8087 -p 8080:8080 -p 8086:8086 -p 9000:9000 -p 9191:9191 -p 9092:9092 --name jz_cec /bin/bash

docker exec -it icsa /bin/bash

#### 认证方式启动MongoDB服务
mongod --auth -f /etc/mongod.conf

#### 启动各后端服务组件
* 进入目录icsa-api执行以下目录  
python main.py "icsa-api"

* 进入目录icsa-platform执行以下目录  
python main.py "icsa-platform"

* 进入目录icsa-ia执行以下目录  
python main.py "icsa-ia"

* 进入目录icsa-helper执行以下目录  
python main.py "icsa-helper"
