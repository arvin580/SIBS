D = {}

def unique(inF,flag=''):
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip('>\n')
        line2 = inFile.readline().strip()
        if line1:
            D.setdefault(line2,[])
            line1 = ':'.join(line1.split('\t'))
            if flag:
                D[line2].append(flag+':'+line1)
            else:
                D[line2].append(line1)
        else:
            break
    inFile.close()

unique('Homo_sapiens.GRCh37.70.pep.all.fa.fa')
unique('Homo_sapiens.GRCh37.70.pep.abinitio.fa.fa')
unique('sum_snv.exome_summary.nonsynonymous-splicing.pep.ref-alt.nonstop-K','SNV')
unique('sum_snv.exome_summary.nonsynonymous-splicing.pep.not-ref-alt.nonstop-K','SNV')
unique('sum_snv.exome_summary.indel.pep.ref-alt.nonstop-K','INDEL')
unique('sum_snv.exome_summary.indel.pep.not-ref-alt.nonstop-K','INDEL')
unique('split-mapped-deletion-translocation-inversion-duplication-K','SV')
unique('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.splicing.not_known-predict-K','PREDICT-SPLICING')
unique('ERR0498-04-05.unmapped.unique.human-viruse.pep-K','HUMAN-VIRUS')
unique('unmapped-blated-viruses-90-60.seq.pep-K','VIRUS')

ouFile = open('HeLa_known-predicted-snv-indel-sv-virus-K.fasta','w')
for k in D:
    ouFile.write('>'+'|'.join(D[k])+'\n')
    ouFile.write(k+'\n')
    #ouFile.write('>REVERSE:'+'|'.join(D[k])+'\n')
    #ouFile.write(k[::-1]+'\n')

ouFile.close()

