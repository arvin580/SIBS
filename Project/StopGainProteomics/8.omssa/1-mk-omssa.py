import os
def mk_omssa(Dir):
    files = os.listdir(Dir)
    for inF in files:
        if inF[-4:]=='.mgf':
            ouF = inF[0:-4]+'.out'

            print('db=/netshare1/home1/people/hansun/StopGainProteomics/4.stopgain/human_uniprot_sprot.digested.stopgain.unique.reverse.fa')

            print('cd /netshare1/home1/people/hansun/Project/StopGainProteomics/8.omssa')

            print('omssacl -d $db -fm '+ Dir + '/' + inF + ' -oc output/'+ ouF + '\n')


mk_omssa('input/Cell-Line-mzxml-1')
