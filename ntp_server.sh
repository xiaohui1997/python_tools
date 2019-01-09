#!/bin/bash
rpm -q chrony && echo '系统已经安装了ntp服务,请检查！' && exit
#安装ntp服务
yum -y install chrony
#检查是否安装成功
(rpm -q chrony && echo ntp服务端安装成功) || (echo 'ntp服务端安装失败' && exit)
#设置系统时区
(timedatectl |grep Shanghai && exit) || (timedatectl set-timezone Asia/Shanghai && echo '时区已经切换到亚洲上海')
#写服务端配置文件
cat >/etc/chrony.conf <<EOF
#服务端指向上层NTP服务器
server 0.centos.pool.ntp.org iburst

driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
#允许哪个ip段同步本服务器时间
allow 192.168.0.0/16
#设置ntp服务器的层级数量
local stratum 10
#设置日志存放目录
logdir /var/log/chrony 
EOF
(systemctl start chronyd && echo 'ntp服务启动成功') || (echo 'ntp启动失败！！！' && exit )
