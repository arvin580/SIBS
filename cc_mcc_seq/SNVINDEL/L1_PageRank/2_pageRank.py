def format_ppi_somatic(dict1,dict2) :
    inFile=open('PPI_somatic')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        dict1.setdefault(fields[0],set())
        dict2.setdefault(fields[0],1.0)
        dict1.setdefault(fields[3],set())
        dict2.setdefault(fields[3],1.0)
        dict1[fields[0]].add(fields[3])
        dict1[fields[3]].add(fields[0])
    inFile.close()

def pageRank(dict1,dict2) :
    for key in dict2 :
        dict2[key]=sum([dict2[x]/float(len(dict1[x])) for x in dict1[key]])*0.85+0.15



dict1=dict()
dict2=dict()
format_ppi_somatic(dict1,dict2)

for n in range(1000) :
    pageRank(dict1,dict2)

d=dict2.items()
d.sort(cmp=lambda x,y :cmp(x[1],y[1]),reverse=True)
for item in d :
    print(item[0]+'\t'+str(item[1]))

