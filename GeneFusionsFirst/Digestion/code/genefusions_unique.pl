open INFILEa,"<exon_fusion_peptide_qc_digestion_qc";
open OUTFILEb,">exon_fusion_peptide_qc_digestion_qc_unique";
while($title=<INFILEa>)
{
$seq=<INFILEa>;
chomp($title);
chomp($seq);
$title=~s/\r//;
$seq=~s/\r//;
$len=@{$myhash{$seq}};
$myhash{$seq}[$len]=$title;
}
keys %myhash;
while(($key,$tmp)=each %myhash)
{
@val=@{$myhash{$key}};
$tmp=undef;
$til=undef;
for($i=0;$i<@val;$i++)
{
	$tmp=$val[$i];
	$tmp=~s/^>//;
	$til.="$tmp&";
}
$til=~s/&$//;
printf OUTFILEb ">$til\n";
printf OUTFILEb "$key\n";
}

