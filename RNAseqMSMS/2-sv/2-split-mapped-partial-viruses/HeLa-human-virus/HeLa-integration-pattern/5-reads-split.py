inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-motif','w')

D = {}
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        ch1 = fields[3]
        ch2 = fields[15]
        pos1_query = int(fields[8])
        pos2_query = int(fields[9])
        pos3_query = int(fields[20])
        pos4_query = int(fields[21])
        pos1_subject = int(fields[10])
        pos2_subject = int(fields[11])
        pos3_subject = int(fields[22])
        pos4_subject = int(fields[23])
        if (pos1_query+pos2_query) < (pos3_query+pos4_query):
            motif = pos3_query - pos1_query
            D.setdefault(motif,[])
            D[motif].append(line1)
        else:
            motif = pos1_query - pos4_query
            D.setdefault(motif,[])
            D[motif].append(line1)
    else:
        break
inFile.close()

d = D.items()
d.sort(cmp = lambda x,y:cmp(len(x[1]),len(y[1])),reverse= True)
for item in d:
    print(item[0])
    print(len(item[1]))
