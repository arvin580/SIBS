import os
import sys
import time
os.system('texmacs %s &'%sys.argv[1])
#os.system('xdotool windowactivate `xdotool search %s | head -1`'%sys.argv[1])
time.sleep(3)

filename = sys.argv[1].split('.tm')[0]
tmpfile = []
for n in range(int(sys.argv[2])):
    if n == 0:
        os.system('xdotool key F9')
    else :
        os.system('xdotool key F11')
    time.sleep(1)
    os.system('xdotool key shift+p')
    time.sleep(1)
    os.system('xdotool key d')
    time.sleep(1)
    os.system('xdotool key f')
    time.sleep(1)
    tmpfile.append(filename+str(n+1)+'.pdf')
    for x in filename+str(n+1):
        os.system('xdotool key %s'%x)
        time.sleep(1)
    os.system('xdotool key Return')
    time.sleep(2)
#os.system('xdotool key period')
os.system('xdotool key ctrl+q')
time.sleep(1)
os.system('xdotool key Right')
time.sleep(1)
os.system('xdotool key Return')
os.system('gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=%s.pdf -dBATCH %s'%(filename,' '.join(tmpfile)))
for x in tmpfile:
    os.remove(x)
