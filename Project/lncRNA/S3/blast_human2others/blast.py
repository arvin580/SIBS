dict1=dict()
def resultStat(fileList) :
    for i,item in enumerate(fileList) :
        inFile1=open(item,'r')
        for line in inFile1 :
            fields=line.split()
            dict1.setdefault(fields[0],[-1,-1,-1]*14)
            if dict1[fields[0]][3*i]==-1 :
                dict1[fields[0]][3*i]=fields[3]
                dict1[fields[0]][3*i+1]=fields[2]
                dict1[fields[0]][3*i+2]=fields[10]
        inFile1.close()

file=['lncdb.human.rat.out','lncdb.human.mouse.out','lncdb.human.human.out','lncdb.human.cow.out','lncdb.human.dog.out','lncdb.human.elephant.out','lncdb.human.opossum.out','lncdb.human.platypus.out','lncdb.human.chicken.out','lncdb.human.xenopus.out','lncdb.human.fugu.out','lncdb.human.tetraodon.out','lncdb.human.zebrafish.out','lncdb.human.chimpanzee.out']
file2=['/netshare1/home1/people/hansun/Project/lncRNA/S3/blast_human2others/'+i for i in file]

resultStat(file2)

ouFile1=open('blast_result1','w')
ouFile2=open('blast_result2','w')

ouFile2.write('\t'.join(['lncRNA.NR','rat','mouse','human','cow','dog','elephant','opossum','platypus','chicken','xenopus','fugu','tetraodon','zebrafish','chimpanzee'])+'\n')

for key in dict1 :
    ouFile1.write(key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')
for key in dict1 :
    ouFile2.write(key+'\t'+'\t'.join([str(dict1[key][i]) for i in range(2,len(dict1[key]),3)])+'\n')

ouFile1.close()
ouFile2.close()
