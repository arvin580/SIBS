cd /netshare1/home1/szzhongxin/proj1/hansun/16sSV/invy


hg19=/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta

ICC4A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/4A/4A.bam
ICC5A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/5A/5A.bam
ICC9A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/9A/9A.bam
ICC10A=/netshare1/home1/szzhongxin/proj1/hansun/mapping/10A/10A.bam

CHC5A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/5A/5A.bam
CHC6A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/6Ax/6A.bam
CHC7A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/7Ax/7A.bam
CHC10A=/netshare1/home1/szzhongxin/proj1/hansun/mapping2/10Ax/10A.bam


ICC4B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/4B/4B.bam
ICC5B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/5B/5B.bam
ICC9B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/9B/9B.bam
ICC10B=/netshare1/home1/szzhongxin/proj1/hansun/mapping3/10B/10B.bam

CHC5B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/5B/5B.bam
CHC6B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/6B/6B.bam
CHC7B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/7B/7B.bam
CHC10B=/netshare1/home1/szzhongxin/proj1/hansun/mapping4/10B/10B.bam

SampleID=ICC5A

invy -z . -p -g $hg19 -i ${SampleID} -b ${SampleID}.inv.br.txt -o ${SampleID}.inv.txt -r ${SampleID}.inv_merge.txt -k ${SampleID}.inv.br_merge.txt $ICC5A 
