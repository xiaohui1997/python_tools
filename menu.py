#_*_coding=utf8_*_
def menu():
    from selects import select
    while True:
        info="""请选择功能:
        1 安装NTP服务端
        2 安装NTP客户端
        3 安装zabbix(这里是客户端,请谨慎选择)
        4 安装apache(yum)
	5 安装python3
	6 安装mysql.5.6.41
	7 源码编译安装nginx
	8 源码编译安装redis 5.0
	9 部署zabbix mysql监控脚本
	10 安装宝塔面板(版本:5.9)
	11 检测服务器硬件信息
        12 退出程序"""
        print(info)
        print("""
        
        """)
	try:
            select_num=str(input("删除使用:ctrl+backspace 请选择>>>> "))
        except: 
	     print('\n''\033[1;37;42m%s\033[0m' % ("异常操作导致程序无法运行,稍后重试"))
	   
	    
        if select_num=="12": print("Bye") ;exit()
        select(select_num)

if __name__ == '__main__':
    menu()
