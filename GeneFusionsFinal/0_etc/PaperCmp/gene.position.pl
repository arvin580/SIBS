open INFILE,"/netshare1/home1/people/hansun/Data/Biomart/gene.position";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\s/,$_);
$hash{$a[9]}="$a[9]\t$a[2]\t$a[3]\t$a[4]\t$a[5]";
}
#while(($key,$val)=each %hash)
#{
#print "$val\n";
#}

close INFILE;

open INFILE,"fusion_peptide_symbol";
open OUTFILE,">gene.position";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
@b=split(/:/,$a[0]);
$hash2{$b[0]}++;
$hash2{$b[1]}++;

}
while(($key,$val)=each %hash2)
{
if(exists($hash{$key}))
{
printf OUTFILE "$hash{$key}\n";
}
}
