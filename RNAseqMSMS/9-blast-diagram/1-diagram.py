def diagram(inF):
    inFile = open(inF)
    L0 = [0]*76
    L1 = [0]*76
    L2 = [0]*76
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            for i in range(len(line2)):
                L0[i] = line2[i]

            ch1 = fields[3]
            start1 = int(fields[10])
            end1 = int(fields[11])
            start1_query = int(fields[8])
            end1_query = int(fields[9])
            ch2 = fields[15]
            start2 = int(fields[22])
            end2 = int(fields[23])
            start2_query= int(fields[20])
            end2_query=int(fields[21])
    
            seq1 = seq(ch1,start1, end1)
            seq2 = seq(ch2,start2, end2)

        else:
            break
    inFile.close()
    print(L0)

diagram('ha')
