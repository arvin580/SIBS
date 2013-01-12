db=/netshare1/home1/people/hansun/StopGainProteomics/4.stopgain/human_uniprot_sprot.digested.stopgain.unique.reverse.fa
cd /netshare1/home1/people/hansun/Project/StopGainProteomics/8.omssa
omssacl -d $db -fm input/Cell-Line-mzxml-4/LM3-5-07.mgf -oc output/LM3-5-07.out
omssacl -d $db -fm input/Cell-Line-mzxml-4/LM3-5-08.mgf -oc output/LM3-5-08.out
omssacl -d $db -fm input/Cell-Line-mzxml-4/LM3-5-09.mgf -oc output/LM3-5-09.out
