cd /netshare1/home1/szzhongxin/proj1/hansun/SV/CREST
nohup gfServer  start 127.0.0.1 77777 ucsc.hg19.2bit &

cd /netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/fudan2/1A
nohup perl /netshare1/home1/people/hansun/MySoft/CREST/CREST.pl -f 1A.bam.cover -d /netshare1/home1/szzhongxin/proj1/hansun/mapping2/1A/1A.bam --ref_genome  /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta -t /netshare1/home1/szzhongxin/proj1/hansun/SV/CREST/ucsc.hg19.2bit --blatserver 127.0.0.1  --blatport 77777  >crest.out1 2>crest.out2 &