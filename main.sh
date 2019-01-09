#!/bin/bash
aa(){
    systemctl stop firewalld
    setenforce 0
    iptables-restore < /etc/sysconfig/iples || echo '导入防火墙防火墙规则规则失败失败'
    chmod 777 /etc/rc.d/rc.local 
}
echo "保存防火墙规则请使用：iptables-save > /etc/sysconfig/iptables"
echo "在/etc/rc.local 中添加 iptables-restory < /etc/sysconfig/iptables"
echo "安装我们可能会用到的依赖软件包，如果不需要请自己手动删除"
[ !  `rpm -qa  | grep ^net-tools` ]  &&   yum -y install net-tools 
[ !  `rpm -qa  | grep ^make` ]  &&   yum -y install make
[ !   `rpm -qa | grep ^gcc-[0-9]`      ]   &&   yum -y install gcc                       
[ !   `rpm -qa | grep ^gcc-c++ ` ]    &&   yum -y install gcc-c++                       
[ !   `rpm -qa | grep ^lrzsz  `      ]   &&   yum -y install lrzsz                      
[ !   `rpm -qa | grep ^vim-common`      ]   &&   yum -y install vim                      
python ./menu.py
cd .. && rm -rf hui_tools
