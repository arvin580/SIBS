inFile = open('20091123_Velos1_NaNa_SA_10k_run2_Trypsin_SECG_SAX_pH04.2013_11_13_02_28_39.t.xml.txt')
for line in inFile:
    fields = line.split('\t')
    if len(fields) > 4:
        pass
    else:
        print(line),
inFile.close()
