# Docker

## Docker 源配置 
```bash
cat << EOF > /etc/docker/daemon.json
{
"registry-mirrors": ["https://******.mirror.aliyuncs.com"]
}
EOF
```

## docker 命令  
```bash 
## 查看容器/镜像的元数据信息
docker inspect nginx
## 查看窗口控制台日志
docker logs --tail=20 -f tomcat9
## 保存镜像为tar文件
docker save -o nginx-va01.tar zeimao77/nginx:va01
## 导入镜像
docker load --input nginx-va01.tar
## 创建mdwiki容器
docker run -d -p 8079:80 --network dockernetwork --ip 172.18.0.17 --name mdwiki\
 -v /home/docker/mdwiki/data:/data/ luzifer/mdwiki:latest
## docker 创建网卡
docker network create --gateway 172.18.0.1 --subnet 172.18.0.0/16 --driver bridge dockernetwork 
## docker 网卡帮助信息
docker network --help
## 查看docker信息,镜像源配置
docker info
```

## Dockerfile 
```
## 指定基础镜像
FROM nginx  
## 指定作者信息
MAINTAINER zeimao77<zeimao77@foxmail.com>
## 将key.tar.gz复制并解压到/var/nginx目录
ADD key.tar.gz /var/nginx  
## 复制文件到指定目录
COPY favicon.ico /usr/share/nginx/html  
COPY nginx.conf /etc/nginx/nginx.conf
## 在Docker build时执行某个命令
RUN echo Asia/Shanghai >> /etc/timezone
## 指定环境变量
ENV spring.profiles.active=pro 
ENV CATALINA_HOME /usr/local/tomcat
## 指定工作路径
WORKDIR $CATALINA_HOME
## 申明映射端口
EXPOSE 6379
## 在Docker run命令时启动服务
CMD [ "redis-server","/usr/local/etc/redis/redis.conf" ]
## 申明挂载数据卷，如果启动时不指定数据卷，将挂载到匿名卷，避免数据丢失
VOLUME [/var/lib/mysql]
```
