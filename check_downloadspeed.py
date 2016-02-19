#!/usr/bin/python
from subprocess import Popen, PIPE, STDOUT
import os
import sys

status = { 'OK' : 0, 'WARNING' : 1, 'CRITICAL' : 2, 'UNKNOWN' : 3}
exitCode=3
warn=0
crit=0
downspeed=0

def print_usage():
	print "USAGE: "+sys.argv[0]+" {bandwidth warning} {bandwidth critical}"
	print "Example: "+sys.argv[0]+" 5 1"

def is_not_number(s):
    try:
        float(s)
        return False
    except ValueError:
        return True

def test():

	#run speedtest-cli
	a = os.popen("/usr/local/bin/speedtest-cli --simple").read()
	#split results
	lines = a.split('\n')
	#if test failed set speeds to 0
	if "Cannot" in a:
		exitCode = 2
		p = 100
		d = 0
		u = 0
		sys.stdout.write('Critical: Speedtest could not run |\n')
	else:
		p = lines[0][6:11]
		d = lines[1][10:14]
		u = lines[2][8:12]

		if is_not_number(d):
			exitCode = 3
                	print 'UNKNOWN: Invalid downloadspeed.  '+d+' is not a number'
		else:
			downspeed = float(d)

		if downspeed < crit:
			exitCode = 2
			sys.stdout.write('Critical: '+ str(downspeed) + ' MBPS | DownloadSpeed='+str(downspeed)+'MBPS;'+str(warn)+';'+str(crit)+';'+'0;100\n')
		elif downspeed < warn:
			exitCode = 1
			sys.stdout.write('Warning: '+ str(downspeed) + ' MBPS | DownloadSpeed='+str(downspeed)+'MBPS;'+str(warn)+';'+str(crit)+';'+'0;100\n')
		else:
			exitCode = 0
			sys.stdout.write('OK: '+ str(downspeed) + ' MBPS | DownloadSpeed='+str(downspeed)+'MBPS;'+str(warn)+';'+str(crit)+';'+'0;100\n')
	sys.exit(exitCode)

#MAIN
if len(sys.argv) != 3:
	exitCode = 3
	print_usage()
	sys.exit(exitCode)
else:
	if (is_not_number(sys.argv[1])):
		exitCode = 3
		print 'UNKNOWN: Invalid warning value '+sys.argv[1]+' is not a number'
                sys.exit(exitCode)
	elif (is_not_number(sys.argv[2])):
		exitCode = 3
		print 'UNKNOWN: Invalid critical value '+sys.argv[2]+' is not a number'
                sys.exit(exitCode)
	else:
		warn=float(sys.argv[1])
                crit=float(sys.argv[2])
	if warn < crit:
		exitCode = 3
		print 'UNKNOWN: Warning value must be higher than critical value. '+warn+' is not higher than '+crit
                sys.exit(exitCode)
	else:
		test()	
