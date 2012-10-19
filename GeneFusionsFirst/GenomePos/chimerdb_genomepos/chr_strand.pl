#perl chr_strand.pl fusion_gene_mapped_pos
open INFILE,"$ARGV[0]";
open OUTFILEa,">$ARGV[0]\_sameChr_sameStr";
open OUTFILEb,">$ARGV[0]\_sameChr_diffStr";
open OUTFILEc,">$ARGV[0]\_diffChr_sameStr";
open OUTFILEd,">$ARGV[0]\_diffChr_diffStr";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
if($a[1] eq $a[4])
{
if($a[3] eq $a[6])
{
printf OUTFILEa "$_\n";
}
else
{
printf OUTFILEb "$_\n";
}

}
else
{
if($a[3] eq $a[6])
{

printf OUTFILEc "$_\n";
}
else
{
printf OUTFILEd "$_\n";
}

}
}
