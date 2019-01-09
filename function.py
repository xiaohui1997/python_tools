#!/usr/bin/python
#_*_coding=utf8_*_
import subprocess
import time
import os
from menu import menu
def returns(str,code):
    import subprocess
    menu()
    if code != 0:
	print('\033[1;37;42m%s\033[0m' % (str+",本次程序终止！！") )

def inputs(title):
	print(title)
        select = str(input("请选择:1/0>>>"))
        if select == "1":
		return True
	else:
		return False
	
def subpro(keyword,tishi):
	retu_code=subprocess.call(keyword,shell=True)
	returns(tishi,retu_code)

def install(bag, erro, names,names_1="1"):
    returnCode = subprocess.call("which "+names, shell=True)
    if returnCode != 0:
        print("""该系统没有%s环境,是否安装%s?
            1/安装
            0/退出""" % (names,names))
        select = str(input("请选择:1/0>>>"))
        if select == "1":
            print("开始安装%s" % (names))
            subpro(bag, erro)
            print("""是否启动%s
                     1/启动
                     0/不启动""" % (names))
            select = str(input("0/1>>>"))
            if select == "1":
		if names_1=="1":
                	subpro("systemctl restart "+names, "启动"+names+"失败")
		else:
			subpro("systemctl restart "+names_1, "启动"+names_1+"失败")
                print("%s启动成功" % (names))
            print("%s安装成功" % (names))
            pass   
        else:
            print("Bye")
    else:
        print("该系统环境有：%s,可以使用该程序！" % (names))

def update_ssh():
    print("当前ssh端口号为：")
    subpro("ss -nutlp |grep sshd |awk '{print $5}' |head -n1|awk -F ':' '{print $2}'","获取ssh端口失败")
    port=input("请输入需更改后的ssh端口：>>>")
    subpro("sed -i '/Port/d' /etc/ssh/sshd_config && sed -i '$aPort '"+str(port)+" /etc/ssh/sshd_config && iptables -C INPUT -p tcp --dport "+str(port)+" -j ACCEPT || iptables -I INPUT -p tcp --dport "+str(port)+" -j ACCEPT &&  systemctl restart sshd","更改ssh端口为"+str(port)+"失败")
    print("更改ssh端口号为"+str(port)+"成功")    

def update_mysql():
    subpro("ps -ef|grep mysqld|grep -v grep","获取mysql端口失败，mysql必须在运行状态才能获取端口号")
    print("当前mysql端口号为：")

    subpro("ss -nutlp |grep mysqld |awk '{print $5}' | awk -F ':' '{print $4}'","获取mysql端口失败")
   
    re_num=input("请输入更改mysql端口号>>>")
    subpro("sed -i '/port/d' /usr/my.cnf && sed -i '7iport='"+str(re_num)+" /usr/my.cnf","更改mysql端口失败")
    re_num=inputs("""是否重启mysql使端口生效？
	    1/重启
	    2/退出""")
    if re_num:
	subpro("systemctl restart mysql","重启mysql失败")

def zabbix():
    subpro("wget --no-check-certificate https://www.ttl178.com/tools/zabbix-4.0.1.tar.gz","安装zabbix软件失败")
    subpro("tar -xf zabbix-4.0.1.tar.gz","解压失败，请稍后重试")
    subpro("useradd -s /sbin/nologin  zabbix","创建用户zabbix失败了")
    os.chdir("zabbix-4.0.1")
    subpro("yum -y install pcre*","预防出错信息的下载,失败了就自己去找原因哦")
    subpro("./configure --enable-agent","加载模块失败咯")
    subpro("make && make install","源码编译失败咯")
    os.chdir("../")
    print('\033[1;37;42m%s\033[0m' % ("恭喜你zabbix安装成功,现在可以开始你的骚操作了"))
   
def httpd():
    install("yum install httpd -y","httpd安装失败","httpd")
def install_mysql():
        print('\033[1;37;32m%s\033[0m' %("请等待系统检测是否安装mysql5.6.41"))
	subpro("[ ! `which mysqld` ]","mysql5.6.4.1已经安装请慎重！！！")
	subpro("wget https://cdn.mysql.com/archives/mysql-5.6/MySQL-5.6.41-1.el7.x86_64.rpm-bundle.tar","mysql数据库安装失败")
	subpro("tar -xf MySQL-5.6.41-1.el7.x86_64.rpm-bundle.tar ","解压mysql数据库失败")
	subpro("rm -rf /etc/my.cnf && rm -rf /var/lib/mysql && rm -rf /usr/my.cnf","环境比较干净")
	subpro("yum -y remove mariadb*   &&   yum -y install autoconf perl-JSON","mysql数据库的依赖包下载失败，系统没得这个包")
	subpro("rpm -ivh *.rpm","安装失败")
	print('\033[1;37;32m%s\033[0m' % ("恭喜你mysql数据库安装成功,请去上面看初始密码,上面有提示"))
	subpro("systemctl start mysql","启动数据库失败")
	subpro("systemctl enable mysql","设置开机自启失败")
#安装宝塔面板
def install_bt():
	subpro('[ ! -d "/www/server" ]',"请注意该系统已经存在宝塔面板")
	print('\033[1;37;32m%s\033[0m' %("开始安装宝塔面板5.9,严禁在已经装了宝塔的环境上面再次安装宝塔！！！"))
	subpro("rm -rf tmp_bag","删除软件下载目录失败")
	subpro("mkdir tmp_bag","创建软件下载目录失败")
	os.chdir("tmp_bag")
	subpro("yum install -y wget && wget -O install.sh http://download.bt.cn/install/install.sh && sed -ic 's/^.*Do you want to install Bt-Panel to the.*/go='y'/' install.sh && bash install.sh","下载宝塔面板失败")
	subpro("rm -rf tmp_bag","删除软件目录失败")
	print('\033[1;37;32m%s\033[0m' % ("宝塔面板安装成功，请使用 bt default 获取账号密码"))

#检测服务器硬件信息
def check():
	print('\033[1;37;32m%s\033[0m' %("开始检测服务器硬件信息。。。。。"))
	subpro("bash check.sh","执行硬件检测脚本失败！！")


def nginx_code():
	subpro("[ ! -d '/usr/local/nginx' ]","检测到本机好像安装了nginx了")
	subpro("rm -rf tmp_bag","删除软件下载目录失败")
        subpro("mkdir tmp_bag","创建软件下载目录失败")
        os.chdir("tmp_bag")
	subpro("wget http://nginx.org/download/nginx-1.14.0.tar.gz","下载nginx源码包失败")
	subpro("tar -xvf nginx-1.14.0.tar.gz","解压nginx失败")
	subpro("yum install gcc gcc-c++ libpcre3 libpcre3-dev openssl libssl-dev perl libperl-dev pcre-devel zlib zlib-devel -y ","安装nginx依赖失败")
	os.chdir("nginx-1.14.0")
	subpro("useradd -m -s /sbin/nologin  nginx","创建nginx用户失败")
	subpro("./configure --prefix=/usr/local/nginx --user=nginx --group=nginx --with-stream","配置nginx失败")
	subpro("make && make install","nginx编译安装失败")
	os.chdir("../../")
	subpro("rm -rf tmp_bag","删除软件目录失败")
	print('\033[1;37;32m%s\033[0m' % ("nginx-->安装成功"))
	re_num=inputs("""是否启动nginx?
		1/启动
		0/退出""")
	if re_num:
		subpro("/usr/local/nginx/sbin/nginx","启动nginx失败")
		print('\033[1;37;32m%s\033[0m' % ("nginx启动成功"))

def install_redis():
	subpro("[ ! `which redis-cli` ]","redis好像已经在本系统之上了！！！")
	subpro("rm -rf tmp_bag","删除软件下载目录失败")
	subpro("mkdir tmp_bag","创建软件下载目录失败")
	os.chdir("tmp_bag")
	subpro("wget http://download.redis.io/releases/redis-5.0.0.tar.gz","下载redis源码包失败")
	subpro("tar -xvf redis-5.0.0.tar.gz","解压redis源码包失败")
	os.chdir("redis-5.0.0")
	subpro("make && make install","编译redis失败")
	print('\033[1;37;42m%s\033[0m' % ("请手动进行redis初始化...."))
	subprocess.call("./utils/install_server.sh")
	print('\033[1;37;32m%s\033[0m' % ("初始化成功"))
	print('\033[1;37;32m%s\033[0m' % ("redis安装成功,redis默认启动成功"))
	os.chdir("../../")
	subpro("rm -rf tmp_bag","删除软件下载目录失败")


def returns(str,code):
    import subprocess
    if code != 0:
	print('\033[1;37;42m%s\033[0m' % (str+"，本次程序终止"))
	menu()

def subpro(keyword,tishi):
        retu_code=subprocess.call(keyword,shell=True)
        returns(tishi,retu_code)

def python3_install():
    import time
    import os
    subpro("rm -rf tmp_bag","删除软件下载目录失败")
    subpro("mkdir tmp_bag","创建软件下载目录失败")
    os.chdir("tmp_bag")
    subpro("wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz","下载Python3失败,请检测网络是否联通")
    subpro("tar -zxvf Python-3.5.0.tgz","解压Python3失败,请检测安装包是否完整！")
    os.chdir("Python-3.5.0")
    subpro("yum install gcc unzip gcc-c++ -y","安装gcc失败")
    subpro('./configure',"配置python3失败！！")
    subpro("make && make install","编译安装python3失败！！")
    print('\033[1;37;32m%s\033[0m' % ("python3 安装成功"))
    time.sleep(3)
    print('\033[1;37;32m%s\033[0m' % ("现在开始安装pip"))
    time.sleep(3)
#-----------------------------------------------------------------
    os.chdir("../")
    subpro("wget https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26","下载setuptools失败")
    subpro("tar -zxvf setuptools-19.6.tar.gz","解压setuptools失败")
    os.chdir("setuptools-19.6")
    subpro("yum install zlib-devel zlib openssl-devel openssl -y","安装zlib/openssl依赖失败")
    subpro("python3 setup.py build","编译setuptools失败")
    subpro("python3 setup.py install","安装setuptools失败")
#-------------------------------------------------------------------------
    os.chdir("../")
    subpro("wget https://pypi.python.org/packages/source/p/pip/pip-8.0.2.tar.gz#md5=3a73c4188f8dbad6a1e6f6d44d117eeb","下载pip失败")
    subpro("tar -zxvf pip-8.0.2.tar.gz","解压pip失败")
    os.chdir("pip-8.0.2")
    subpro("python3 setup.py build","编译pip失败")
    subpro("python3 setup.py install","安装pip失败")
    os.chdir("../Python-3.5.0")
    subpro("make & make install","重新编译python3失败")
    subpro("ln -s /usr/local/python3.5/bin/pip3 /usr/bin/pip3","软链pip3失败")
    subpro("pip3 list","pip3 异常")
    os.chdir("../../")
    subpro("rm -rf tmp_bag","删除tmp_bag目录失败")
    print('\033[1;37;32m%s\033[0m' % ("python3-->pip3 安装成功"))

def python3_jiance():
    returnCode=subprocess.call("which python3",shell=True)
    if returnCode != 0:
        print("""该系统没有python3环境,是否安装python3?
        1/安装
        0/退出""")
        select=str(input("请选择:1/0>>>"))
        if select=="1":
    		print('\033[1;37;32m%s\033[0m' % ("开始安装python3"))
                python3_install()
        else:
    		print('\033[1;37;32m%s\033[0m' % ("Bye"))
                exit()
    else:
    	print('\033[1;37;32m%s\033[0m' % ("该系统python环境为：python3,可以使用该程序！"))


#部署zabbix mysql监控
def zabbix_mysql():
	print('\033[1;37;32m%s\033[0m' %("请等待系统检测是否安装zabbix"))
	subpro("[  `which zabbix_agentd` ]","zabbix没有安装请安装后重试！！！")
	os.chdir("/root")
	os.chdir("/usr/local/etc/zabbix_agentd.conf.d/")
	subpro("wget --no-check-certificate https://www.ttl178.com/tools/zabbix_mysql.tar.gz",'下载zabbix_mysql失败')
	subpro("tar -xvf zabbix_mysql.tar.gz","解压zabbix_mysql.tar.gz失败")
	subpro("rm -rf zabbix_mysql*","删除垃圾文件失败")
	os.chdir('../')
	subpro("wget --no-check-certificate   https://www.ttl178.com/tools/chk_mysql.tar.gz",'下载chk_mysql.tar.gz失败')
	subpro("tar -xvf chk_mysql.tar.gz",'解压chk_mysql.tar.gz失败')
	subpro('rm -rf chk_mysql.tar.gz','删除chk_mysql.tar.gz失败')
	print('\033[1;37;32m%s\033[0m' % ("脚本配置成功"))	
	print('\033[1;37;32m%s\033[0m' % ("恭喜你，所有脚本全部配置成功！！"))
	print( '\033[5;31;40m%s\033[0m ' % ("请将Include=/usr/local/etc/zabbix_agentd.conf.d/ 添加到客户端的配置文件中"))
	print('\033[5;31;40m%s\033[0m ' %("请配置/usr/local/etc/chk_mysql.sh 的数据库信息"))
	print( '\033[5;31;40m%s\033[0m ' %  ( "请配置/usr/local/etc/zabbix_agentd.conf.d/mysql.ping 的数据库信息"))
	print(  '\033[5;31;40m%s\033[0m ' % ( "请配置/usr/local/etc/zabbix_agentd.conf.d/mysql.replication 的数据库信息"))
        print( '\033[5;31;40m%s\033[0m ' %("最后需要重启zabbix_agentd")) 
#---------------------------------------------------------------------------------------------------------------------------
#部署NTP服务端
def ntp_server():
        print('\033[1;37;32m%s\033[0m' %("开始部署NTP服务端。。。。。"))
        subpro("bash ntp_server.sh","执行部署NTP服务端脚本失败！！")
#部署NTP客户端
def ntp_agent():
        print('\033[1;37;32m%s\033[0m' %("开始部署NTP客户端。。。。。"))
        subpro("bash ntp_agent.sh","执行部署NTP客户端脚本失败！！")
