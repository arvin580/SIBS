import os
for item in os.listdir('.') :
    if item.find('.pdf') !=-1 :
        png=os.path.splitext(item)[0]+'.png'
        os.system('convert %s %s'%(item,png))

