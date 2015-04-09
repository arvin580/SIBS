###  python ctx_sample.py 

files=['/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/10A/10A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/1A/1A.bam.predSV.txt.ctx.genelevel', 
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/2A/2A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/3A/3A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/4A/4A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/5A/5A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/6A/6A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/7A/7A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/8A/8A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan/9A/9A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/10A/10A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/1A/1A.bam.predSV.txt.ctx.genelevel.tmp',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/2A/2A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/3A/3A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/4A/4A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/5A/5A.bam.predSV.txt.ctx.genelevel.tmp',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/6A/6A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/7A/7A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/8A/8A.bam.predSV.txt.ctx.genelevel',
        '/netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/9A/9A.bam.predSV.txt.ctx.genelevel.tmp']


ouFile=open('ctx_gene_pair_sample','w')
dict1=dict()
for f,file in enumerate(files) :
    inFile1=open(file)
    for line in inFile1 :
        line=line.strip('\r\n')
        fields=line.split('\t')
        if fields[3]!='' or fields[7]!='' :
            key1=fields[3]+':'+fields[7]
            dict1.setdefault(key1,[0]*20)
            dict1[key1][f]+=1

items=dict1.items()
for item in sorted(items,key=lambda x:sum(x[1]),reverse=True):
    ouFile.write(item[0]+'\t'+'\t'.join([str(i) for i in item[1]])+'\n')

#ouFile1=open('ctx_sample1','w')
#ouFile2=open('ctx_sample2','w')

#for item in sorted(dict1.items(),key=lambda x:x[0]):
#    ouFile2.write(item[0]+'\t'+str(item[1][0])+'\n')
#for item in sorted(dict1.items(),key=lambda x:x[1],reverse=True):
#    ouFile1.write(item[0]+'\t'+str(item[1][0])+'\n')

#ouFile1.close()
#ouFile2.close()

   


