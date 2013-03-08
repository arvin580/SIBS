import sys

def viruse(v):
    D = {}
    inFile = open('ERR0498-04-05.unmapped.unique.human-viruse')
    ouFile1 = open('ERR0498-04-05.unmapped.unique.human-viruse.'+v, 'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split()
            if (fields[3].find('chr')==0 and fields[15].find(v) == 0) or \
                (fields[15].find('chr')==0 and fields[3].find(v) == 0):
                D.setdefault(fields[3], 0)
                D.setdefault(fields[15], 0)
                D[fields[3]]+=1
                D[fields[15]]+=1
        else:
            break
    
    inFile.close()
    
    d = D.items()
    d.sort(cmp=lambda x,y:cmp(x[1],y[1]))
    
    for item in d:
        ouFile1.write(item[0] + '\t' + str(item[1]) + '\n')
    ouFile1.close()

viruse('NC_001357.1')
viruse('NC_003225.1')
