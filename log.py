import os,re,sys
if len(sys.argv)<3:
    print("you must input your log file and anystr")
else:
    if os.path.isfile(sys.argv[1]):
        logfile=open(sys.argv[1],'r')
        alog=None
        if len(sys.argv)==4:
            alog=open(sys.argv[3],'w')
        for line in logfile:
            if re.findall(r''+sys.argv[2]+'',line):
                print(line)
                if alog:
                    alog.write(line)
        if alog:
            alog.close()
        logfile.close()
    else:
        print("no log file")
