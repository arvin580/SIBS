1.is_repeat.py $1
2.sort.py $1.not.repeat
3.merge.py $1.not.repeat.sorted
4.recurrent.py $1.not.repeat.sorted.merged
