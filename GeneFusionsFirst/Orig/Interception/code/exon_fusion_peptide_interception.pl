open INFILE,"<../Translate/exon_fusion_peptide";
open OUTFILE,">exon_fusion_peptide_interception";
while($title=<INFILE>)
{
$sequence=<INFILE>;
chomp($title);
chomp($sequence);
$title=~s/\r//;
$sequence=~s/\r//;
@tit=split(/\|/,$title);
$point=$tit[2];
$first=undef;
$second=undef;
$firstlen=undef;
$secondlen=undef;
if($point<=30)
{
$first=substr($sequence,0,$point);
$firstlen=$point;
}
else
{
$first=substr($sequence,$point-30,30);
$firstlen=30;
}
$tmp=length($sequence)-$point;
if($tmp<=30)
{
$second=substr($sequence,$point,$tmp);
$secondlen=$tmp;
}
else
{
$second=substr($sequence,$point,30);
$secondlen=30;
}
$title_out="$title$firstlen|$secondlen";
$sequence_out=$first.$second;
printf OUTFILE "$title_out\n";
printf OUTFILE "$sequence_out\n";
}
