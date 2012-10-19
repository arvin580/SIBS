# perl pep2dna_12.pl fusion_point_3_2_complete_c_title2_orig3 /netshare1/home1/people/hansun/GeneFusions/AftTandem/FDR

open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_view";
while(<INFILE>)
{
chomp;
%hash=undef;
@a=split(/\t/,$_);
$seq=$a[3];
printf OUTFILE "$_\t";
opendir DIR,"$ARGV[1]";
foreach $filename(readdir DIR)
{
open INFILEa,"$ARGV[1]/$filename";
while($s=<INFILEa>)
{
@b=split(/\t/,$s);
if(index($seq,$b[9],0)!=-1)
{
$hash{$b[9]}++;
}
}
close INFILEa;
}
keys %hash;
while(($key,$val)=each %hash)
{
printf OUTFILE "$key\t";
}
printf OUTFILE "\n";
close DIR;
}
