cd /fs01/szzhongxin/proj1/hansun/samtools/CHR20

ICC1A=/fs01/szzhongxin/proj1/hansun/mapping/1A/1A.bam
ICC2A=/fs01/szzhongxin/proj1/hansun/mapping/2A/2A.bam
ICC3A=/fs01/szzhongxin/proj1/hansun/mapping/3A/3A.bam
ICC4A=/fs01/szzhongxin/proj1/hansun/mapping/4A/4A.bam
ICC5A=/fs01/szzhongxin/proj1/hansun/mapping/5A/5A.bam
ICC6A=/fs01/szzhongxin/proj1/hansun/mapping/6A/6A.bam
ICC7A=/fs01/szzhongxin/proj1/hansun/mapping/7A/7A.bam
ICC8A=/fs01/szzhongxin/proj1/hansun/mapping/8A/8A.bam
ICC9A=/fs01/szzhongxin/proj1/hansun/mapping/9A/9A.bam
ICC10A=/fs01/szzhongxin/proj1/hansun/mapping/10A/10A.bam

CHC1A=/fs01/szzhongxin/proj1/hansun/mapping2/1A/1A.bam
CHC2A=/fs01/szzhongxin/proj1/hansun/mapping2/2A/2A.bam
CHC3A=/fs01/szzhongxin/proj1/hansun/mapping2/3A/3A.bam
CHC4A=/fs01/szzhongxin/proj1/hansun/mapping2/4A/4A.bam
CHC5A=/fs01/szzhongxin/proj1/hansun/mapping2/5A/5A.bam
CHC6A=/fs01/szzhongxin/proj1/hansun/mapping2/6A/6A.bam
CHC7A=/fs01/szzhongxin/proj1/hansun/mapping2/7A/7A.bam
CHC8A=/fs01/szzhongxin/proj1/hansun/mapping2/8A/8A.bam
CHC9A=/fs01/szzhongxin/proj1/hansun/mapping2/9A/9A.bam
CHC10A=/fs01/szzhongxin/proj1/hansun/mapping2/10A/10A.bam



chr='chr16'

samtools mpileup -uDf /netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta -r $chr $ICC1A $ICC2A $ICC3A $ICC4A $ICC5A $ICC6A $ICC7A $ICC8A $ICC9A $ICC10A $CHC1A $CHC2A $CHC3A $CHC4A $CHC5A $CHC6A $CHC7A $CHC8A $CHC9A $CHC10A  > tmp.raw.${chr}.bcf
