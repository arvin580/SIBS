seq=[
'/netshare1/home1/szzhongxin/proj1/fudan5/4A/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan5/4A/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan5/5A/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan5/5A/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan5/9A/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan5/9A/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan5/10A/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan5/10A/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan7/4B/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan7/4B/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan7/5B/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan7/5B/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan7/9B/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan7/9B/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan7/10B/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan7/10B/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan6/5A/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan6/5A/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan6/6A/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan6/6A/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan6/7A/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan6/7A/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan6/10A/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan6/10A/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan8/5B/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan8/5B/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan8/6B/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan8/6B/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan8/7B/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan8/7B/read_q20w5m35.2.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan8/10B/read_q20w5m35.1.fq.del.seq',
'/netshare1/home1/szzhongxin/proj1/fudan8/10B/read_q20w5m35.2.fq.del.seq'
]


ouFile = open('16sExome.seq.name.merged','w')

for i in range(0,len(seq),2):
    inFile = open(seq[i])
    reads1 = inFile.readlines()
    inFile.close()
    inFile = open(seq[i+1])
    reads2 = inFile.readlines()
    inFile.close()
    for x in range(0,len(reads1),3):
        ouFile.write(reads1[x])
        ouFile.write(reads1[x+1])
        ouFile.write(reads1[x+2])
        ouFile.write(reads2[x])
        ouFile.write(reads2[x+1])
        ouFile.write(reads2[x+2])
