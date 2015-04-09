spec = '20090812_Velos1_NaNa_SA_10k_Hela_Trypsin_SECA_SAXpH_05.27842.27842.3'
inFile = open('20090812_Velos1_NaNa_SA_10k_Hela_Trypsin_SECA_SAXpH_05.mgf')
L = inFile.readlines()
s = L.index('TITLE=%s\n'%spec)
e = L[s:].index('END IONS\n')
mgf = L[s-1:e+1]
print(''.join(mgf))
inFile.close()
