ouFile = open('HeLa-SNV-INDEL-VIRUS-SV-MGF.mgf','w')
def pep(inF,flag,trypsin):
    inFile = open(inF)
    for line in inFile:
        ouFile.write(line)
    inFile.close()


pep('/netshare1/home1/people/hansun/RNAseqMSMS/5-tandem-snv-indel/output-KR-filter/HeLa-SNV-INDEL-ALT-pep-spec.mgf','SNV-INDEL','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/5-tandem-snv-indel/output2-ED-filter/HeLa-SNV-INDEL-ALT-pep-spec.mgf','SNV-INDEL','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/5-tandem-snv-indel/output3-K-filter/HeLa-SNV-INDEL-ALT-pep-spec.mgf','SNV-INDEL','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output-KR-filter/HeLa-Human-Viruses-pep-spec.mgf','HUMAN-VIRUS','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output2-ED-filter/HeLa-Human-Viruses-pep-spec.mgf','HUMAN-VIRUS','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output3-K-filter/HeLa-Human-Viruses-pep-spec.mgf','HUMAN-VIRUS','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output-KR-filter/HeLa-Viruses-pep-spec.mgf','VIRUS','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output2-ED-filter/HeLa-Viruses-pep-spec.mgf','VIRUS','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/6-tandem-viruses/output3-K-filter/HeLa-Viruses-pep-spec.mgf','VIRUS','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Deletion-pep-spec.mgf','DELETION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Deletion-pep-spec.mgf','DELETION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Deletion-pep-spec.mgf','DELETION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Duplication-pep-spec.mgf','DUPLICATION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Duplication-pep-spec.mgf','DUPLICATION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Duplication-pep-spec.mgf','DUPLICATION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Inversion-pep-spec.mgf','INVERSION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Inversion-pep-spec.mgf','INVERSION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Inversion-pep-spec.mgf','INVERSION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Translocation-pep-spec.mgf','TRANSLOCATION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Translocation-pep-spec.mgf','TRANSLOCATION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Translocation-pep-spec.mgf','TRANSLOCATION','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-SV-Translocation-pep-spec.mgf','TRANSLOCATION','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-SV-Translocation-pep-spec.mgf','TRANSLOCATION','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-SV-Translocation-pep-spec.mgf','TRANSLOCATION','LysC')


pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-Predict-Splicing-pep-spec.mgf','PREDICT-SPLICING','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-Predict-Splicing-pep-spec.mgf','PREDICT-SPLICING','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-Predict-Splicing-pep-spec.mgf','PREDICT-SPLICING','LysC')

pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output-KR-filter/HeLa-Predict-pep-spec.mgf','PREDICT','Trypsin')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output2-ED-filter/HeLa-Predict-pep-spec.mgf','PREDICT','GluC')
pep('/netshare1/home1/people/hansun/RNAseqMSMS/7-tandem-sv/output3-K-filter/HeLa-Predict-pep-spec.mgf','PREDICT','LysC')













