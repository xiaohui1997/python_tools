#!/usr/bin/python
from function import *
def select(num):
    names = {"3": zabbix,"5":python3_jiance,
	     "6": install_mysql,"7":nginx_code,
	     "8": install_redis,"10": install_bt,"11":check}
    names[num]()
