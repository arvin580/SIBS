''' python id2symbol2.py

one kegg id to many gene symbols which are seped by : '''



inFile1=open('/netshare1/home1/people/hansun/Data/GeneID/gene_info_9606_symbol','r')
dict1=dict()
for line in inFile1 :
    fields=line.split()
    dict1[fields[0]]=':'.join(fields[1:])

inFile1.close()

dict2=dict()
inFile3=open('kegg_pathway','r')
for line in inFile3 :
    line=line.strip()
    fields=line.split('\t')
    dict2[fields[0].split(':')[1]]=fields[1]

inFile3.close()

inFile2=open('kegg_gene','r')
ouFile1=open('kegg_gene_symbol2','w')
for line in inFile2 :
    fields=line.split()
    ouFile1.write(fields[0])
    for item in fields[1:] :
        if item in dict1 :
            ouFile1.write('\t'+dict1[item])
        else :
            ouFile1.write('\t'+item)
            print(item)
    ouFile1.write('\n')



inFile2.close()
ouFile1.close()
