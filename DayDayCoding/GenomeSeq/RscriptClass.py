import time
import os

class Rscript :

    def __init__(self,cmd='') :

        tmpFile='tmp.'+str(time.time())+'.R'
        ouFile=open(tmpFile,'w')
        ouFile.write(cmd.strip())
        ouFile.close()
        os.system('Rscript '+tmpFile)
        os.remove(tmpFile)

    
