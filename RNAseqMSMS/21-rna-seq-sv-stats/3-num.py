def num(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.num','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')

        ch1 = fields[3]
        ch2 = fields[15]
        query_start1 = int(fields[8])
        query_end1 = int(fields[9])
        query_start2 = int(fields[20])
        query_end2 = int(fields[21])

        subject_start1 = int(fields[10])
        subject_end1 = int(fields[11])
        subject_start2 = int(fields[22])
        subject_end2 = int(fields[23])

        if (query_start1 + query_end1) <= (query_start2 + query_end2):
            #point = subject_end1
            k1 = ch1 + ':' + str(subject_end1) + ':' + ch2 + ':' + str(subject_start2)
            k2 = ch2 + ':' + str(subject_start2) + ':' + ch1 + ':' + str(subject_end1)  
        else:
            #point = subject_end2
            k1 = ch1 + ':' + str(subject_start1) + ':' + ch2 +':'+ str(subject_end2)
            k2 = ch2 +':'+ str(subject_end2) + ':' + ch1 + ':' + str(subject_start1) 
        #k = ch2 + ':' + str(point)
        if k1 not in D and k2 not in D:
            D.setdefault(k1, [])
            D[k1].append(line)
        elif k1 in D:
            D.setdefault(k1, [])
            D[k1].append(line)
        elif k2 in D:
            D.setdefault(k2, [])
            D[k2].append(line)

    inFile.close()
    d = D.items()
    d.sort(cmp = lambda x,y:cmp(len(x[1]), len(y[1])),reverse = True)
    for item in d:
        ouFile.write(item[0] + '\t'+ str(len(item[1])) +'\t'+ '|'.join(item[1])+'\n')
    ouFile.close()

num('split-mapped-deletion.normal.seq.filtered')
num('split-mapped-inversion.normal.seq.filtered')
num('split-mapped-duplication.normal.seq.filtered')
num('split-mapped-translocation.normal.seq.filtered')
