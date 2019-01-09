#!/bin/bash
rpm -q chrony && echo '系统已经安装了ntp服务,请检查！' && exit
#安装ntp服务
yum -y install chrony
#检查是否安装成功
(rpm -q chrony && echo ntp客户端安装成功) || (echo 'ntp客户端安装失败' && exit)
#获取ntp服务端ip
read -t 1000 -p "请输入ntp服务端内网ip:" ips
#写服务端配置文件
cat >/etc/chrony.conf <<EOF
#客户端指向上层NTP服务器（服务端）
server ${ips} iburst

driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
#设置日志存放目录
logdir /var/log/chrony 
EOF
(systemctl start chronyd && echo 'ntp服务启动成功') || (echo 'ntp启动失败！！！' && exit )
