open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_mapped";
while(<INFILE>)
{
@a=split(/\t/,$_);
if($a[1] != 4)
{
printf OUTFILE $_;
}
}
