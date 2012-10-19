#!/bin/bash

cd /netshare1/home1/szzhongxin/proj1/hansun
t=`date +%Y%m%d`
git add *.py
git add *.sh
git add *.R
git add *.pbs
git commit -m 'crontab.'${t}

cd /netshare1/home1/people/hansun
t=`date +%Y%m%d`
git add *.py
git add *.sh
git add *.R
git add *.pbs
git add *.pl
git commit -m 'crontab.'${t}
