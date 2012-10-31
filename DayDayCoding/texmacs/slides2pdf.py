import os
import sys
import time

t = 1

def page_numbering(n):
    os.system('xdotool key shift+p')
    time.sleep(t)
    os.system('xdotool key a')
    time.sleep(t)
    os.system('xdotool key g')
    time.sleep(t)
    os.system('xdotool key e')
    time.sleep(t)
    os.system('xdotool key period')
    time.sleep(t)
    for x in str(n)+'/'+sys.argv[2]:
        if x == '/':
            os.system('xdotool key slash')
        else:
            os.system('xdotool key %s'%x)
        time.sleep(t)
    os.system('xdotool key Return')
    time.sleep(t)

def make_pdf(n):
    os.system('xdotool key shift+p')
    time.sleep(t)
    os.system('xdotool key d')
    time.sleep(t)
    os.system('xdotool key f')
    time.sleep(t)
    os.system('xdotool key period')
    time.sleep(t)
    tmpfile.append('tmp'+str(n)+'.pdf')
    for x in 'tmp'+str(n):
        os.system('xdotool key %s'%x)
        time.sleep(t)
    os.system('xdotool key Return')
    time.sleep(t*3)

def quit():
    os.system('xdotool key ctrl+q')
    time.sleep(t)
    os.system('xdotool key Right')
    time.sleep(t)
    os.system('xdotool key Return')
    time.sleep(t)

def remove_tmp():
    for x in tmpfile:
        os.remove(x)



os.system('texmacs %s &'%sys.argv[1])
#os.system('xdotool windowactivate `xdotool search %s | head -1`'%sys.argv[1])
time.sleep(t*3)

filename = sys.argv[1].split('.tm')[0]
tmpfile = []
for n in range(int(sys.argv[2])):
    if n == 0:
        os.system('xdotool key F9')
    else :
        os.system('xdotool key F11')
    time.sleep(t)

    page_numbering(n+1)
    make_pdf(n+1)

quit()
os.system('gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=%s.pdf -dBATCH %s'%(filename,' '.join(tmpfile)))
remove_tmp()
