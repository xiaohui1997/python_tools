#!/usr/bin/python
from function import *
def select(num):
    names = {"1": ntp_server,"2": ntp_agent,
             "3": zabbix,"4":httpd,"5":python3_jiance,
	     "6": install_mysql,"7":nginx_code,
	     "8": install_redis,"9":zabbix_mysql,
	     "10": install_bt,"11":check}
    names[num]()
