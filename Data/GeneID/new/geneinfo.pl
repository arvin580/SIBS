open INFILE,"gene_info";
open OUTFILE,">gene_info\_$ARGV[0]";
while(<INFILE>)
{
@a=split(/\t/,$_);
if($a[0] eq $ARGV[0])
{
printf OUTFILE "$_";
}
}
