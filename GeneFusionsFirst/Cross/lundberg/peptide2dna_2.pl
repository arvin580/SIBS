open INFILE,"peptide_complete_c";
open OUTFILE,">peptide_complete_c_title";
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
