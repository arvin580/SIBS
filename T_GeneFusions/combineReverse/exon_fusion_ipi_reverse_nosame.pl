open INFILEa,"<exon_fusion_peptide_interception_qc_comb_reverse";
open INFILEb,"<ipi.HUMAN.v3.80.fasta_comb_reverse";
open INFILEc,"<contaminated_comb_reverse";
open OUTFILEb,">interception_ipi_contaminated_reverse_unique";
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
while($title=<INFILEb>)
{
$seq=<INFILEb>;
chomp($title);
chomp($seq);
$title=~s/\r//;
$seq=~s/\r//;
$len=@{$myhash{$seq}};
$myhash{$seq}[$len]=$title;
}
while($title=<INFILEc>)
{
$seq=<INFILEc>;
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
#if(@val==1)
#{
#printf OUTFILEa "$val[0]\n"; 
#printf OUTFILEa "$key\n"; 
#}
#else
#{
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
#}
}

