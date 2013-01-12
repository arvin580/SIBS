def uniprot():
    inFile = open('/netshare1/home1/people/hansun/StopGainProteomics/2.uniprot/human_uniprot_sprot.fa')
    D = {}
    while True:
        head = inFile.readline().strip()
        seq = inFile.readline().strip()
        if head:
            name = head.split('|')[1]
            D[name]=seq
        else:
            break
    inFile.close()
    return D

D = uniprot()

def  pep2protein():
    files = os.listdir('.')
    for inF in files:
        if inF[-7:]=='stop2-2':
            pass
