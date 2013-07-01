import re
def KR(inF):
    inFile = open(inF)
    ouFile = open(inF+'-K','w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            s=re.search('[K](.*[K])',line2)
            if s and len(s.group(1))>=6:
                fields = line1.split(':')
                start = int(fields[6])
                end = int(fields[7])
                st = line2.index(s.group(1))
                ouFile.write(':'.join(fields[0:6])+':'+str(start-st)+':'+str(end-st)+':'+':'.join(fields[8:])+'\n')
                ouFile.write(s.group(1)+'\n')
        else:
            break
    inFile.close()
    ouFile.close()

#KR('split-mapped-deletion-translocation-inversion-duplication')
KR('sum_snv.exome_summary.indel.pep.not-ref-alt.nonstop')
KR('sum_snv.exome_summary.indel.pep.ref-alt.nonstop')
KR('sum_snv.exome_summary.nonsynonymous-splicing.pep.not-ref-alt.nonstop')
KR('sum_snv.exome_summary.nonsynonymous-splicing.pep.ref-alt.nonstop')
