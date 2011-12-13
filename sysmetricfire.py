#!/usr/bin/python

# This is an early version of a script, developed under the BSD 
# license. 
#
# FRLinux - frlinux@frlinux.net
#
# you need psutil v0.4 or above - http://code.google.com/p/psutil/
#
# v0.1 - 13/12/11 - basic metrics feeding to metricfire

import time
import psutil
import metricfire

# send key to server
# add key here in the form of /key
metricfire.init("")

# cpu
cputimes =  psutil.cpu_times()
#print type(cputimes),dir(cputimes)
cpus= ['user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq']

for cpu in cpus:
	metric = getattr(cputimes,cpu)
   	metricfire.send("cpu." + cpu, str(metric))
	
# memory
phymemusage = psutil.phymem_usage()
virtmemusage = psutil.virtmem_usage()
mems = ['total', 'used', 'free', 'percent' ]

for mem in mems:
	metric = getattr(phymemusage,mem)
   	metricfire.send("phymem." + mem, str(metric))
	metric = getattr(virtmemusage,mem)
   	metricfire.send("virtmem." + mem, str(metric))

