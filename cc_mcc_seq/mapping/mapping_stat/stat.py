### python mapping_stat.py . >mapping_stat

import sys
import os
import re

dir=os.listdir(sys.argv[1])
print('%s\t%s\t%s' %('properly paired','mapped - properly paired','unmapped'))

for file in dir :
#for file in sorted(dir) :
    if file.find('.stat')!=-1 :
        inFile1=open(sys.argv[1]+'/'+file,'r')
        for line in inFile1 :
            sea=re.search(r'(\w+).*in total',line)
            if sea :
                total=int(sea.group(1))
            sea=re.search('(\w+).*mapped \(',line)
            if sea :
                mapped=int(sea.group(1))
            sea=re.search('(\w+).*properly paired \(',line)
            if sea :
                paired=int(sea.group(1))
                print('%d\t%d\t%d' %(paired,mapped-paired,total-mapped))
        inFile1.close()
