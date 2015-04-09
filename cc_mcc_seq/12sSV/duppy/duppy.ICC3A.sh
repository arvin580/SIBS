cd /netshare1/home1/szzhongxin/proj1/hansun/12sSV/duppy


hg19=/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta

ICC1A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/1A/1A.bam
ICC2A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/2A/2A.bam
ICC3A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/3A/3A.bam
ICC4A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/4A/4A.bam
ICC5A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/5A/5A.bam
ICC6A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/6A/6A.bam
ICC7A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/7A/7A.bam
ICC8A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/8A/8A.bam
ICC9A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/9A/9A.bam
ICC10A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/10A/10A.bam

CHC1A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/1A/1A.bam
CHC2A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/2A/2A.bam
CHC3A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/3A/3A.bam
CHC4A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/4A/4A.bam
CHC5A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/5A/5A.bam
CHC6A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/6A/6A.bam
CHC7A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/7A/7A.bam
CHC8A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/8A/8A.bam
CHC9A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/9A/9A.bam
CHC10A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/10A/10A.bam


ICC4B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/4B/4B.bam
ICC5B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/5B/5B.bam
ICC9B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/9B/9B.bam
ICC10B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/10B/10B.bam

CHC5B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/5B/5B.bam
CHC6B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/6B/6B.bam
CHC7B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/7B/7B.bam
CHC10B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/10B/10B.bam

SampleID=ICC3A

duppy -z . -p -g $hg19 -i ${SampleID} -b ${SampleID}.br.txt -o ${SampleID}.dup.txt  $ICC3A

