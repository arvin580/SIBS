ouFile = open('HeLa-SNV-INDEL-VIRUS-SV-MGF.note','w')
def pep(inF,flag,trypsin):
    inFile = open(inF)
    for line in inFile:
        ouFile.write(line)
    inFile.close()


pep('/netshare1/home1/people/hansun/RNAseqMSMS/5-tandem-snv-indel/output-KR-filter/HeLa-SNV-INDEL-ALT-pep-spec.note','SNV-INDEL','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/5-tandem-snv-indel/output2-ED-filter/HeLa-SNV-INDEL-ALT-pep-spec.note','SNV-INDEL','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/5-tandem-snv-indel/output3-K-filter/HeLa-SNV-INDEL-ALT-pep-spec.note','SNV-INDEL','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output-KR-filter/HeLa-Human-Viruses-pep-spec.note','HUMAN-VIRUS','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output2-ED-filter/HeLa-Human-Viruses-pep-spec.note','HUMAN-VIRUS','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output3-K-filter/HeLa-Human-Viruses-pep-spec.note','HUMAN-VIRUS','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output-KR-filter/HeLa-Viruses-pep-spec.note','VIRUS','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output2-ED-filter/HeLa-Viruses-pep-spec.note','VIRUS','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output3-K-filter/HeLa-Viruses-pep-spec.note','VIRUS','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Deletion-pep-spec.note','DELETION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Deletion-pep-spec.note','DELETION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Deletion-pep-spec.note','DELETION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Duplication-pep-spec.note','DUPLICATION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Duplication-pep-spec.note','DUPLICATION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Duplication-pep-spec.note','DUPLICATION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Inversion-pep-spec.note','INVERSION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Inversion-pep-spec.note','INVERSION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Inversion-pep-spec.note','INVERSION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Translocation-pep-spec.note','TRANSLOCATION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Translocation-pep-spec.note','TRANSLOCATION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Translocation-pep-spec.note','TRANSLOCATION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Translocation-pep-spec.note','TRANSLOCATION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Translocation-pep-spec.note','TRANSLOCATION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Translocation-pep-spec.note','TRANSLOCATION','LysC')


pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-Predict-Splicing-pep-spec.note','PREDICT-SPLICING','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-Predict-Splicing-pep-spec.note','PREDICT-SPLICING','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-Predict-Splicing-pep-spec.note','PREDICT-SPLICING','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-Predict-pep-spec.note','PREDICT','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-Predict-pep-spec.note','PREDICT','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-Predict-pep-spec.note','PREDICT','LysC')













