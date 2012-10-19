#!/bin/bash

cd /netshare1/home1/people/hansun/.crontab

t=`date "+%y.%m.%d"`
h=/netshare1/home1/people/hansun
h2=/netshare1/home1/szzhongxin/proj1/hansun

find $h2 -name '*.pl' >tar.file
find $h2 -name '*.py' >>tar.file
find $h2 -name '*.R' >>tar.file
find $h2 -name '*.pbs' >>tar.file
find $h2 -name '*.sge' >>tar.file
find $h2 -name '*.cpp' >>tar.file
find $h2 -name '*.h' >>tar.file


find $h -name '*.pl' >>tar.file
find $h -name '*.py' >>tar.file
find $h -name '*.R' >>tar.file
find $h -name '*.pbs' >>tar.file
find $h -name '*.sge' >>tar.file
find $h -name '*.cpp' >>tar.file
find $h -name '*.h' >>tar.file
tar -cvzf mycode.$t.tar.gz --files-from tar.file --exclude=$h/Perl --exclude=$h/R --exclude=$h/MySoft --exclude=$h/
