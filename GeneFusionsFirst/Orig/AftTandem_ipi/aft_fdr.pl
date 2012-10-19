#$ARGV[0]:input dir	$ARG[1]:output file	$ARGV[2]:aa beside fusion point
#perl FDR_fusions fusion_point_3 3
opendir DIR,"$ARGV[0]";
open OUTFILE,">$ARGV[1]";
open OUTFILEa,">$ARGV[2]";
foreach $filename(readdir DIR)
{
if($filename=~/validated/)
{
open INFILE,"<$ARGV[0]/$filename";
while(<INFILE>)
{
chomp;
s/\r$//g;
@line=split(/\t/,$_);
$hash{$line[9]}.=$_;
}
close(INFILE);
}
}
while(($key,$val)=each %hash)
{
printf OUTFILE ">$key\n$val\n";
printf OUTFILEa "$key\n";

}
close OUTFILE;
