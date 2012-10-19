open INFILE1,"../../Data/Lundberg/SRR040290_atcg.fastq";
open INFILE2,"../../Data/Lundberg/SRR040293_atcg.fastq";
open INFILE3,"../../Data/Lundberg/SRR040361_atcg.fastq";
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

