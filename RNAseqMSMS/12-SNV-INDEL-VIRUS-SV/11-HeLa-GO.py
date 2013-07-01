viral_reproductive=['MAGI3','DDX3X','TCEB1','SIRT1','DDB1','TRIM25','COBRA1','PVR','KDM4A','NMT1','NACA','NUP210','PLCG1','KPNA2','KPNB1','EIF4G3','RPL35A','RPL37A','CXCR7','RPL30','USP7','PSMB2','VIM','NUP133','NFX1','CFLAR','EIF4G1','PSMC3','RPL18','UBN1','ISG15','RPL14','SRCAP','KRT19','RPS11','RHOA','ITGAV','LTBR','NUP205','RPLP2','KRT7','RAN','SSRP1','POLR2E','HTATIP2','POLR2A','XRCC5','RB1','BIN1','TGFB1','DAG1','CUL7','CAV1','SF3B2','TPR','UBR4','HCFC1','RPS23','FBLN1','SND1']

virus_host_interaction=['MAGI3','UBN1','DDX3X','ISG15','SRCAP','TCEB1','KRT19','SIRT1','DDB1','TRIM25','ITGAV','RHOA','PVR','LTBR','KDM4A','NACA','KRT7','RAN','POLR2E','HTATIP2','KPNA2','PLCG1','KPNB1','XRCC5','RB1','EIF4G3','BIN1','TGFB1','DAG1','CUL7','CAV1','CXCR7','USP7','SF3B2','UBR4','PSMB2','VIM','NFX1','HCFC1','CFLAR','EIF4G1','PSMC3','FBLN1','SND1']

cell_death=['MAGI3','OPA1','LGALS1','DIDO1','OPTN','BRCA1','ESPL1','ATN1','PRUNE2','GSN','ANO10','CLUL1','SMNDC1','RRAGC','PEG10','DNAJA3','KIF1B','NMT1','DPP6','TRIO','LMNA','KPNB1','SOS1','PLEC','PRKD2','HEXA','PSMD6','PUF60','PSMB2','VIM','CFLAR','EIF4G1','AKT1','PSMC3','PSMG2','GATAD2A','ALMS1','TAOK2','PSMD3','TP53BP2','PSME3','ATXN2','CIB1','TRAF7','H1F0','RHBDD1','GLI2','IGHMBP2','UNC5A','BAD','PSMD9','PSMD12','ACIN1','ITSN1','NOP56','RAD21','PKM2','DHCR24','SLC9A3R1','LTBR','BIRC6','PLEKHG2','GNB1','PRKDC','HTATIP2','SIK1','STEAP3','DYNC1H1','BUB1B','RB1','TGFB1','PSME4','ROBO2','HTT','UBA1','TREX1','DBNL','SPTAN1','C5AR1','L1CAM','SYNE1','C8orf4','FAF1','PARP4'] 

cell_circle_checkpoint=['TAOK2','PSMD3','PSME3','MCM4','CASC5','BRCA1','PSMD9','PSMD12','MCM6','DDB1','CDC16','RPA1','ORC4','TTK','DTL','BUB1B','ANAPC5','RB1','E2F1','CDKN1A','TGFB1','PSME4','KNTC1','MAD2L2','TPR','PSMD6','CCNA2','PSMB2','MBD4','ZWINT','PSMC3','PSMG2'] 


inFile = open('HeLa-SNV-INDEL-VIRUS-SV-pep-new-pFind3-new_pFind')
ouFile = open('HeLa-SNV-INDEL-VIRUS-SV-pep-new-pFind3-new_pFind-GO','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[7]
    fds = gene.split(':')
    D = {}
    for fd in fds:
        fs = fd.split('|')
        for y in fs: 
            ys = y.split(';')
            for x in ys: 
                if x !='*' and x!='': 
                    if x in viral_reproductive:
                        D['viral_reproductive']=1
                    if x in virus_host_interaction:
                        D['virus_host_interaction']=1
                    if x in cell_death:
                        D['virus_host_interaction']=1
                    if x in cell_circle_checkpoint:
                        D['cell_circle_checkpoint']=1
    ouFile.write(';'.join(D)+'\t'+line+'\n')
inFile.close()
ouFile.close()

