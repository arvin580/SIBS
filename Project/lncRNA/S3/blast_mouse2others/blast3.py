import commands

file=['lncdb.mouse.mouse.out','lncdb.mouse.rat.out','lncdb.mouse.human.out','lncdb.mouse.chimpanzee.out','lncdb.mouse.cow.out','lncdb.mouse.dog.out','lncdb.mouse.elephant.out','lncdb.mouse.opossum.out','lncdb.mouse.platypus.out','lncdb.mouse.chicken.out','lncdb.mouse.xenopus.out','lncdb.mouse.fugu.out','lncdb.mouse.tetraodon.out','lncdb.mouse.zebrafish.out']

def grep(lncRNA) :
    ouFile=open(lncRNA+'.grep','w')
    for item in file :
        status,out=commands.getstatusoutput('grep '+lncRNA+' '+item)
        if len(out) >0 :
            row=out.split('\n')
            for r in row :
                fields=r.split('\t')
                ouFile.write(lncRNA+'\t'+item.split('.')[2]+'\t'+fields[6]+'\t'+fields[7]+'\t'+fields[1]+'\t'+fields[8]+'\t'+fields[9]+'\n')
    ouFile.close()



grep('NR_004444')
grep('NR_003270')
grep('NR_033616')
