ouFile = open('split-mapped-deletion-translocation-inversion-duplication', 'w')

D = {}
inFile = open('split-mapped-deletion.gene')
for line in inFile:
    line = line.strip()
    fields = line.split(':')
    if len(fields)>3:
        k = fields[0]+':'+fields[1]+':'+fields[2]
        D[k]= fields[3]
inFile.close()

inFile = open('split-mapped-deletion')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        k1 = fields[3] + ':' + fields[10] + ':' +fields[11]
        k2 = fields[15] + ':' + fields[22] + ':' +fields[23]
        if k1 in D and k2 in D:
            ouFile.write(line1 + '\t' + D[k1] +'\t'+D[k2]+'\t'+'Deletion'+'\n')
            ouFile.write(line2+'\n')
        elif k1 in D and k2 not in D:
            ouFile.write(line1 + '\t' + D[k1] +'\t'+'*'+'\t'+'Deletion'+'\n')
            ouFile.write(line2+'\n')
        elif k1 not in D and k2 in D:
            ouFile.write(line1 + '\t' + '*' +'\t'+D[k2]+'\t'+'Deletion'+'\n')
            ouFile.write(line2+'\n')
        else:
            ouFile.write(line1 + '\t' + '*'+ '\t'+'*'+'\t' + 'Deletion'+'\n')
            ouFile.write(line2+'\n')

    else:
        break
    
inFile.close()


D = {}
inFile = open('split-mapped-translocation.gene')
for line in inFile:
    line = line.strip()
    fields = line.split(':')
    if len(fields)>3:
        k = fields[0]+':'+fields[1]+':'+fields[2]
        D[k]= fields[3]
inFile.close()

inFile = open('split-mapped-translocation')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        k1 = fields[3] + ':' + fields[10] + ':' +fields[11]
        k2 = fields[15] + ':' + fields[22] + ':' +fields[23]
        if k1 in D and k2 in D:
            ouFile.write(line1 + '\t' + D[k1] +'\t'+D[k2]+'\t'+'Translocation'+'\n')
            ouFile.write(line2+'\n')
        elif k1 in D and k2 not in D:
            ouFile.write(line1 + '\t' + D[k1] +'\t'+'*'+'\t'+'Translocation'+'\n')
            ouFile.write(line2+'\n')
        elif k1 not in D and k2 in D:
            ouFile.write(line1 + '\t' + '*' +'\t'+D[k2]+'\t'+'Translocation'+'\n')
            ouFile.write(line2+'\n')
        else:
            ouFile.write(line1 + '\t' + '*'+ '\t'+'*'+'\t' + 'Translocation'+'\n')
            ouFile.write(line2+'\n')

    else:
        break
    
inFile.close()



D = {}
inFile = open('split-mapped-inversion.gene')
for line in inFile:
    line = line.strip()
    fields = line.split(':')
    if len(fields)>3:
        k = fields[0]+':'+fields[1]+':'+fields[2]
        D[k]= fields[3]
inFile.close()

inFile = open('split-mapped-inversion')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        k1 = fields[3] + ':' + fields[10] + ':' +fields[11]
        k2 = fields[15] + ':' + fields[22] + ':' +fields[23]
        if k1 in D and k2 in D:
            ouFile.write(line1 + '\t' + D[k1] +'\t'+D[k2]+'\t'+'Inversion'+'\n')
            ouFile.write(line2+'\n')
        elif k1 in D and k2 not in D:
            ouFile.write(line1 + '\t' + D[k1] +'\t'+'*'+'\t'+'Inversion'+'\n')
            ouFile.write(line2+'\n')
        elif k1 not in D and k2 in D:
            ouFile.write(line1 + '\t' + '*' +'\t'+D[k2]+'\t'+'Inversion'+'\n')
            ouFile.write(line2+'\n')
        else:
            ouFile.write(line1 + '\t' + '*'+ '\t'+'*'+'\t' + 'Inversion'+'\n')
            ouFile.write(line2+'\n')

    else:
        break
    
inFile.close()



D = {}
inFile = open('split-mapped-duplication.gene')
for line in inFile:
    line = line.strip()
    fields = line.split(':')
    if len(fields)>3:
        k = fields[0]+':'+fields[1]+':'+fields[2]
        D[k]= fields[3]
inFile.close()

inFile = open('split-mapped-duplication')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        k1 = fields[3] + ':' + fields[10] + ':' +fields[11]
        k2 = fields[15] + ':' + fields[22] + ':' +fields[23]
        if k1 in D and k2 in D:
            ouFile.write(line1 + '\t' + D[k1] +'\t'+D[k2]+'\t'+'Duplication'+'\n')
            ouFile.write(line2+'\n')
        elif k1 in D and k2 not in D:
            ouFile.write(line1 + '\t' + D[k1] +'\t'+'*'+'\t'+'Duplication'+'\n')
            ouFile.write(line2+'\n')
        elif k1 not in D and k2 in D:
            ouFile.write(line1 + '\t' + '*' +'\t'+D[k2]+'\t'+'Duplication'+'\n')
            ouFile.write(line2+'\n')
        else:
            ouFile.write(line1 + '\t' + '*'+ '\t'+'*'+'\t' + 'Duplication'+'\n')
            ouFile.write(line2+'\n')

    else:
        break
    
inFile.close()
