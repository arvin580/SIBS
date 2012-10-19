open INFILE,"<$ARGV[0]";
open OUTFILE,">$ARGV[0]_comb_reverse";
$num=0;
while(<INFILE>)
{
chomp;
s/\r//;
s/^>/>contaminated:/g;
if(/^>/)
{
$num++;
if($num==1)
{
$title=$_;
}
else
{
$seq_out=uc $seq;
printf OUTFILE "$title\n";
printf OUTFILE "$seq_out\n";
$title=~s/^>//;
$seq_out_rev=reverse $seq_out;
printf OUTFILE ">REVERSE_$title\n";
printf OUTFILE "$seq_out_rev\n";

$seq=undef;
$title=$_;
}
}
else
{
$seq.=$_;
}

}
$seq_out=uc $seq;
printf OUTFILE "$title\n";
printf OUTFILE "$seq_out\n";
$title=~s/^>//;
$seq_out_rev=reverse $seq_out;
printf OUTFILE ">REVERSE_$title\n";
printf OUTFILE "$seq_out_rev\n";

