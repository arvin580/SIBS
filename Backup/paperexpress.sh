#!/bin/bash

cd /netshare1/home1/people/hansun/DayDayCoding/PaperExpress

rsp=`ps aux| grep "PaperExpress"|grep -v "grep"|wc -l` 

if [ $rsp -eq 0 ]
then
echo 'restart' >>PaperExpress.restart.log
/netshare1/home1/people/hansun/MySoft/Python/Python-2.7.3/python PaperExpress.v0.2.py >>PaperExpress.run1.log 2>>PaperExpress.run2.log
fi



