cd /netshare1/home1/people/hansun/RNAseqMSMS/2-sv/3-unmapped 
#ls *.blated |xargs -n 1 python  1-unmapped.py
#ls *.unmapped |xargs -n 1 python six-frame-translation.py
#ls *.pep |xargs -n 1 python 2-nonstop.py
#ls *.nonstop |xargs -n 1 python 3-digestion.py
#ls *.digested |xargs -n 1 python 4-len.py
ls *.6acid |xargs -n 1 python 5-unique.py

