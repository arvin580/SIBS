open INFILE,"exon_phase";
open OUTFILE,">exon_phase_id";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
$hash{$a[2]}.=$a[-1];
}
while(($key,$val)=each %hash)
{
if($val=~/^1+$/||$val=~/^2+$/||$val=~/^0+$/||$val=~/^(-1)+$/)
{
printf OUTFILE "$key\t$val\n";
}
else
{
print "$key\t$val\n";
}
}
