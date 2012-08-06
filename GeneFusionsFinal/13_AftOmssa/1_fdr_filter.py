import csv
FDR=0.001

def fdr(iFile) : 
    dict1=dict()
    inFile=open(iFile)
    csvFile=csv.reader(inFile)
    head=csvFile.next()
    for fields in csvFile :
        line='\t'.join(fields)
        dict1[line]=float(fields[3])
    inFile.close()
    
    d1=dict1.items()
    d1.sort(cmp=lambda x,y:cmp(x[1],y[1]))
    
    ouFile=open('FDR/'+iFile.split('/')[1]+'_fdr','w')
    decoy=0
    target=0
    for item in d1 :
        fields=item[0].split('\t')
        if fields[9].find('REVERSE')!=-1 :
            decoy+=1
        else :
            target+=1
        if 2*decoy/float(decoy+target)<=FDR :
            ouFile.write(item[0]+'\n')
    
    ouFile.close()

import os
inputDir='output'
files=os.listdir(inputDir)
for item in files :
    if item.find('.out')!=-1 :
        fdr(inputDir+'/'+item)
