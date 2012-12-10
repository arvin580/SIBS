cd /netshare1/home1/szzhongxin/proj1/hansun/16sTranslocation
python 1.is_repeat.py $1
python 2.sort.py $1.not.repeat
python 3.merge.py $1.not.repeat.sorted
python 4.recurrent.py $1.not.repeat.sorted.merged
