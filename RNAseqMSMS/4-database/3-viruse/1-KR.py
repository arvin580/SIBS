import re
def KR(inF):
    inFile = open(inF)
    ouFile = open(inF+'-KR','w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            s=re.search('[K|R](.*[K|R])',line2)
            if s and len(s.group(1))>=6:
                ouFile.write(line1+'\n')
                ouFile.write(s.group(1)+'\n')
        else:
            break
    inFile.close()
    ouFile.close()

#KR('split-mapped-deletion-translocation-inversion-duplication')
#KR('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.splicing.not_known-predict')
KR('ERR0498-04-05.unmapped.unique.human-viruse.pep')
KR('unmapped-blated-viruses-90-60.seq.pep')
