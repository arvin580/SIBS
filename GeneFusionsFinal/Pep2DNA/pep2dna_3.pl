#perl pep2dna_3.pl fusion_point_3_2_complete_c 
#perl pep2dna_3.pl splicing_point_3_2_complete_c 
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_title";
while($peptide=<INFILE>)
{
$num++;
if($peptide=~/^\#/)
{
$title=<INFILE>;
$num++;
if($title=~/^>/)
{
$title=~s/^>//g;
@a=split(/\|/,$title);
printf OUTFILE "$peptide$a[0]\n";
}
else
{
print "ERROR:$num\n";
}

}
}
