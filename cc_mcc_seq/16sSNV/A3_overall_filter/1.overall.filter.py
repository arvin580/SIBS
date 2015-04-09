import re

d=20
D=500
Q=10

def dp_stat(iFile):
    dp = []
    inFile = open(iFile)
    ouFile = open(iFile + '.overall.filter','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        s = re.search('DP=(\d+);', fields[33])
        if s:
            DP=int(s.group(1))
            if d<=DP<=D and float(fields[31])>=Q:
                ouFile.write(line + '\n')
    inFile.close()
    ouFile.close()


dp_stat('sum_snv16s.exome_summary')
dp_stat('sum_snv16s.genome_summary')
