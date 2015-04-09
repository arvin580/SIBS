###This is a example of script for using SVDetect

## DATA:
## Illumina 50bp sequencing reads in mate-pair
## Organism : Human
## Sample data: neuroblastoma cell lines
## Reference data: normal cell lines

cd /netshare1/home1/szzhongxin/proj1/hansun/SV/SVDetect/fudan2/10A

#Generation and filtering of links from the sample data
SVDetect linking filtering -conf sample.sv.conf

#Generation and filtering of links from the reference data
#SVDetect linking filtering -conf reference.sv.conf

#Comparison of links between the two datasets
#SVDetect links2compare -conf sample.sv.conf

#Calculation of depth-of-coverage log-ratios
#SVDetect cnv ratio2circos ratio2bedgraph -conf sample.cnv.conf

#Visualization of filtered links and copy-number profiles in Circos
#circos -conf circos/sample.circos.conf
