#!/bin/bash
echo "安装我们可能会用到的依赖软件包，如果不需要请自己手动删除"
[ !  `rpm -qa  | grep ^net-tools` ]  &&   yum -y install net-tools 
[ !  `rpm -qa  | grep ^make` ]  &&   yum -y install make
[ !   `rpm -qa | grep ^gcc-[0-9]`      ]   &&   yum -y install gcc                       
[ !   `rpm -qa | grep ^gcc-c++ ` ]    &&   yum -y install gcc-c++                       
[ !   `rpm -qa | grep ^lrzsz  `      ]   &&   yum -y install lrzsz                      
[ !   `rpm -qa | grep ^vim-common`      ]   &&   yum -y install vim
[ !   `rpm -qa | grep ^git`      ]   &&   yum -y install git
python ./menu.py
cd .. && rm -rf python_tools