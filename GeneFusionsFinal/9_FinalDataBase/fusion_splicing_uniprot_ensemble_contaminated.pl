open INFILEa,"<exon_fusion_peptide_qc_digestion_qc_comb_reverse";
open INFILEb,"<splicing_exon_peptide_qc_digestion_qc_comb_reverse";
open INFILEc,"<uniprot_human_comb_reverse";
open INFILEd,"<ensembl_protein_comb_reverse";
open INFILEe,"<contaminanted_comb_reverse";
open OUTFILE,">fusion_splicing_uniprot_ensembl_contaminated_final";
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

while($title=<INFILEd>)
{
$seq=<INFILEd>;
chomp($title);
chomp($seq);
$title=~s/\r//;
$seq=~s/\r//;
$len=@{$myhash{$seq}};
$myhash{$seq}[$len]=$title;
}

while($title=<INFILEe>)
{
$seq=<INFILEe>;
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
printf OUTFILE ">$til\n";
printf OUTFILE "$key\n";
#}
}

