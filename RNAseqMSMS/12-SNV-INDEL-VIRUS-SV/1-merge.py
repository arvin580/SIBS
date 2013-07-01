ouFile = open('HeLa-SNV-INDEL-VIRUS-SV-pep','w')
def pep(inF,flag,trypsin):
    if flag == 'SNV-INDEL':
        inFile = open(inF)
        for line in inFile:
            fields = line.split('\t')
            if fields[3].find('SNV')!=-1:
                ouFile.write(trypsin+'\t'+'SNV'+'\t'+line)
            elif fields[3].find('INDEL')!=-1:
                ouFile.write(trypsin+'\t'+'INDEL'+'\t'+line)
        inFile.close()
    else:
        inFile = open(inF)
        for line in inFile:
            ouFile.write(trypsin+'\t'+flag+'\t'+line)
        inFile.close()


pep('/netshare1/home1/people/hansun/RNAseqMSMS/5-tandem-snv-indel/output-KR-filter/HeLa-SNV-INDEL-ALT-pep.gene','SNV-INDEL','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/5-tandem-snv-indel/output2-ED-filter/HeLa-SNV-INDEL-ALT-pep.gene','SNV-INDEL','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/5-tandem-snv-indel/output3-K-filter/HeLa-SNV-INDEL-ALT-pep.gene','SNV-INDEL','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output-KR-filter/HeLa-Human-Viruses-pep.gene','HUMAN-VIRUS','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output2-ED-filter/HeLa-Human-Viruses-pep.gene','HUMAN-VIRUS','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output3-K-filter/HeLa-Human-Viruses-pep.gene','HUMAN-VIRUS','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output-KR-filter/HeLa-Viruses-pep.gene','VIRUS','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output2-ED-filter/HeLa-Viruses-pep.gene','VIRUS','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output3-K-filter/HeLa-Viruses-pep.gene','VIRUS','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Deletion-pep.gene','DELETION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Deletion-pep.gene','DELETION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Deletion-pep.gene','DELETION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Duplication-pep.gene','DUPLICATION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Duplication-pep.gene','DUPLICATION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Duplication-pep.gene','DUPLICATION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Inversion-pep.gene','INVERSION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Inversion-pep.gene','INVERSION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Inversion-pep.gene','INVERSION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Translocation-pep.gene','TRANSLOCATION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Translocation-pep.gene','TRANSLOCATION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Translocation-pep.gene','TRANSLOCATION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Translocation-pep.gene','TRANSLOCATION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Translocation-pep.gene','TRANSLOCATION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Translocation-pep.gene','TRANSLOCATION','LysC')


pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-Predict-Splicing-pep.gene','PREDICT-SPLICING','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-Predict-Splicing-pep.gene','PREDICT-SPLICING','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-Predict-Splicing-pep.gene','PREDICT-SPLICING','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-Predict-pep.gene','PREDICT','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-Predict-pep.gene','PREDICT','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-Predict-pep.gene','PREDICT','LysC')













