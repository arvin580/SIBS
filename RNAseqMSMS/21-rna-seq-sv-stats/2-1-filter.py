def num(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF + '.filtered', 'w')
    ouFile2 = open(inF + '.not.filtered', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')

        ch = fields[3]
        query_start1 = int(fields[8])
        query_end1 = int(fields[9])
        query_start2 = int(fields[20])
        query_end2 = int(fields[21])

        subject_start1 = int(fields[10])
        subject_end1 = int(fields[11])
        subject_start2 = int(fields[22])
        subject_end2 = int(fields[23])

        '''
        if (query_start1 + query_end1) <= (query_start2 + query_end2):
            if 1 <= query_start1 <= 10 and 34 <= query_end1  <= 46 \
                    and 35 <= query_start2 <= 46 and 65 <= query_end2 <= 76:
                ouFile.write(line + '\n')
            else:
                ouFile2.write(line + '\n')
        else:
            if 35 <= query_start1 <= 46 and 65 <= query_end1  <= 76 \
                    and 1 <= query_start2 <= 10 and 34 <= query_end2 <= 46:
                ouFile.write(line + '\n')
            else:
                ouFile2.write(line + '\n')
        '''
        if (query_start1 + query_end1) <= (query_start2 + query_end2):
            if 1 <= query_start1 <= 5 and 35 <= query_end1  <= 45 \
                    and 35 <= query_start2 <= 45 and 72 <= query_end2 <= 76:
                ouFile.write(line + '\n')
            else:
                ouFile2.write(line + '\n')
        else:
            if 35 <= query_start1 <= 45 and 72 <= query_end1  <= 76 \
                    and 1 <= query_start2 <= 5 and 35 <= query_end2 <= 45:
                ouFile.write(line + '\n')
            else:
                ouFile2.write(line + '\n')

    ouFile.close()
    ouFile2.close()

num('split-mapped-inversion.normal.seq')
num('split-mapped-duplication.normal.seq')
num('split-mapped-deletion.normal.seq')
num('split-mapped-translocation.normal.seq')
