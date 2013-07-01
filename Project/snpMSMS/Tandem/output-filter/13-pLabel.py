from pymouse import PyMouse
from pykeyboard import PyKeyboard
from time import sleep
import os
import sys
import shutil

m = PyMouse()
k = PyKeyboard()
DIR = 'S:\\LabSvr\\Pics'

def capture_first(pep,spec,gene,row_no,flag):
    k.press_key(k.pause_key)
    sleep(2)
    n = 0
    Fs = os.listdir(DIR)
    for F in Fs:
        if F.find('screenshot') == 0:
            n += 1
            pic = F
    if n == 1:
        Fname = str(row_no)+'-'+pep+'-'+gene+'-'+spec+'-'+str(flag)+'.png' 
        shutil.move(DIR+os.sep+pic, DIR+os.sep+Fname)
    else:
        print('Warning'+':'+str(row_no)+'-'+pep+'-'+gene+'-'+spec+'-'+str(flag))
        return 

def capture(pep,spec,gene,row_no,flag):
    k.press_key(k.pause_key)
    sleep(2)
    n = 0
    Fs = os.listdir(DIR)
    fs = []
    for x in Fs:
        if x.find('screenshot') == 0:
            fs.append(DIR+os.sep+x)
    fs.sort(cmp=lambda x,y:cmp(os.path.getmtime(x),os.path.getmtime(y)),reverse=True)
    pic = fs[0]
    Fname = str(row_no)+'-'+pep+'-'+gene+'-'+spec+'-'+str(flag)+'.png' 
    shutil.move(pic, DIR+os.sep+Fname)



def pLabel(pep,spec,gene,row_no):
    m = PyMouse()
    k = PyKeyboard()
    # ALL button
    m.click(1243,204)
    sleep(2)
    m.click(362,762)
    sleep(1)
    m.click(362,762)
    sleep(0.3)
    m.click(362,762)
    sleep(1)
    for n in range(30):
        k.press_key(k.backspace_key)
    sleep(1)

    k.type_string(spec)
    sleep(1)
    k.press_key(k.enter_key)
    sleep(1)
    capture(pep,spec,gene,row_no,0)
    sleep(1)
    m.click(609,182)
    sleep(1)
    # peptide
    m.click(132,728)
    sleep(1)
    m.click(132,728)
    sleep(0.3)
    m.click(132,728)
    sleep(1)
    k.press_key(k.backspace_key)
    sleep(1)
    k.type_string(pep)
    sleep(1)
    k.press_key(k.enter_key)
    sleep(1)
    capture(pep,spec,gene,row_no,1)
    sleep(1)






#pLabel('LDPETEPLGTTK','8813.8813.2','TEX264','001')
#pLabel('VVFPSEEVVEQK','22300.22300.2','RNMTL1','002')


def genename(gene):
    G = []
    fds = gene.split(':')
    for fd in fds:
        fs = fd.split('|')
        for y in fs: 
            ys = y.split(';')
            for x in ys: 
                if x !='*' and x!='': 
                    G.append(x)
    return '-'.join(set(G))
        


def readFile(inF):
    inFile = open(inF)
    n = int(sys.argv[1]) - 1
    for line in inFile:
        n += 1
        line = line.rstrip()
        fields = line.split('\t')
        pep = fields[4]
        gene = genename(fields[5])
        if not gene:
            gene = 'Intergenetic-'+str(n)
        spec = fields[6].split('|')[0].upper()
        spec_id = spec
        #spec_id = '.'.join(spec.split('.')[-3:])
        pLabel(pep,spec_id,gene,n)
    
    inFile.close()

readFile('Liver-SNV-INDEL-new-pep-gene-new-pFind3-new_pFind')
