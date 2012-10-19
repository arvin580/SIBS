open INFILE1,"SRR040290.sam";
open INFILE2,"SRR040293.sam";
open INFILE3,"SRR040361.sam";
chomp($ARGV[0]);
$a=$ARGV[0];
$a=reverse($a);
$a=~tr/ATCG/TAGC/;
while(<INFILE1>)
{
if(/$ARGV[0]/||/$a/)
{
print;
}
}
while(<INFILE2>||/$a/)
{
if(/$ARGV[0]/)
{
print;
}
}
while(<INFILE3>||/$a/)
{
if(/$ARGV[0]/)
{
print;
}
}

