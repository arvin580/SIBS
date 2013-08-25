D = {}
inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-mc')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if int(fields[1]) > 1:
        D[fields[0]] = line
inFile.close()
print(len(D))

def num(inF):
    inFile = open(inF)
    ouFile = open(inF+'-more_than_one','w')
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
        if k1 in D or k2  in D:
            ouFile.write(line+ '\n')
    inFile.close()
num('ERR0498-04-05.unmapped.unique.human-viruse-checked')
