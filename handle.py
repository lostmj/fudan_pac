#!/usr/bin/python
# encoding=utf-8
# isInNet(rip,"127.0.0.0","255.0.0.0") ||
import string
f = open("edu_free_ip.txt")             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
start_flag = 1
fconf = open("edu_free_ip.conf",'w')             # 返回一个文件对象
ip_num=0
while (line != ''):
    # print line
    if  ( start_flag):
        if (line.startswith('-')):
            start_flag = 0
        print "This line is not normal and jump to next."
        line = f.readline()
        continue
    else:
        # print line,                 # 后面跟 ',' 将忽略换行符
        line_str = line.split()
        # print line_str
        if (len(line_str)):
            fconf.write("isInNet(rip,\""+line_str[0]+'","'+line_str[2]+'") ||\n')
            if line_str[2]=='255.255.255.255':
                ip_num=ip_num+1
    line = f.readline()
print "Work finished"
print ip_num
f.close()
fconf.close()
