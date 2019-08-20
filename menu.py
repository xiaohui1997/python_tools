# _*_coding=utf8_*_
def menu():
    from selects import select
    while True:
        info = """请选择功能:
        3 安装zabbix4.2.5(客户端)
	5 安装python3.5
	6 安装5.7.26
	7 源码编译安装nginx1.14
	8 源码编译安装redis 5.0
	10 安装宝塔面板(版本:5.9)
	11 检测服务器硬件信息
        12 退出程序"""
        print(info)
        print("""
        
        """)
        try:
            select_num = str(input("删除使用:ctrl+backspace 请选择>>>> "))
        except:
            print('\n''\033[1;37;42m%s\033[0m' % ("异常操作导致程序无法运行,稍后重试"))

        if select_num == "12": print("Bye");exit()
        select(select_num)


if __name__ == '__main__':
    menu()
