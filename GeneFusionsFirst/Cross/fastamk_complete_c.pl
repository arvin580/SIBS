#perl fastamk_complete_c.pl fusion_point_3_2_complete_c fusion_point_3_0
#perl fastamk_complete_c.pl splicing_point_3_2_complete_c splicing_point_3_0  
open INFILEa,"$ARGV[1]";
while(<INFILEa>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
$hash{$a[0]}=$a[1];
}

open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_peptide";
while(<INFILE>)
{
chomp;
s/\r$//g;
if(/^#/)
{
s/^#//g;
printf OUTFILE "$_\t$hash{$_}\n";
}
}
close INFILE;
close OUTFILE;




open INFILE,"$ARGV[0]";
open OUTFILEa,">$ARGV[0]\_peptide.fasta";
$n=0;
while($line1=<INFILE>)
{
if($line1=~/^#/)
{
$line2=<INFILE>;
$line3=<INFILE>;
chomp($line1);
$line1=~s/\r$//g;
chomp($line2);
$line2=~s/\r$//g;
chomp($line3);
$line3=~s/\r$//g;

$n++;
printf OUTFILEa ">peptide$n\n$line3\n";
}
}
close INFILE;
close OUTFILEa;

open INFILE,"$ARGV[0]";
open OUTFILEa,">$ARGV[0]\_peptide_short.fasta";
$n=0;
while($line1=<INFILE>)
{
chomp($line1);
$line1=~s/\r$//g;
if($line1=~/^#/)
{
$n++;
$line1=~s/^#//g;
printf OUTFILEa ">peptide$n\n$line1\n";
}
}
close INFILE;
close OUTFILEa;


