import os


def mk_omssa(Dir):
    N = 50
    n = 0
    m = 1 
    ouFile = open('omssa.'+str(m)+'.sh', 'w')
    ouFile.write('db=/netshare1/home1/people/hansun/StopGainProteomics/4.stopgain/human_uniprot_sprot.digested.stopgain.unique.reverse.fa'+'\n')
    ouFile.write('cd /netshare1/home1/people/hansun/Project/StopGainProteomics/8.omssa'+'\n')
    files = os.listdir(Dir)
    for inF in files:
        if inF[-4:]=='.mgf':
            n += 1
            if n / (N+1) > 0 :
                n = 1
                m += 1
                ouFile = open('omssa.'+str(m)+'.sh', 'w')
                ouFile.write('db=/netshare1/home1/people/hansun/StopGainProteomics/4.stopgain/human_uniprot_sprot.digested.stopgain.unique.reverse.fa'+'\n')
                ouFile.write('cd /netshare1/home1/people/hansun/Project/StopGainProteomics/8.omssa'+'\n')

            ouF = inF[0:-4]+'.out'

            ouFile.write('omssacl -d $db -fm '+ Dir + '/' + inF + ' -oc output/'+ ouF + '\n')


mk_omssa('input/Cell-Line-mzxml-1')
