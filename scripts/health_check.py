#!/usr/bin/env python3

import psutil
import email_health_check

cpu_usage = psutil.cpu_percent(5)
disk_space = psutil.disk_usage('/')
memory_usage = psutil.virtual_memory()

print(cpu_usage)
if(cpu_usage>80):
	Subject = "Error - CPU usage is over 80%"
	email_health_check.send_mail(Subject)
	
print(disk_space)
print(memory_usage)
