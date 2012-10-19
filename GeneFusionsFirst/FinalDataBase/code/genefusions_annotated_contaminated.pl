open INFILEa,"<$ARGV[0]";
open INFILEb,"<uniprot_sprot_comb_reverse";
open INFILEc,"<contaminanted_comb_reverse";
#@f=split(/\_/,$ARGV[0]);
#open OUTFILEb,">genefusions_annotated_contaminated_reverse_final_$f[-1]";
open OUTFILEb,">genefusions_annotated_contaminated_reverse_final";
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
#@arr=split(/\s+/,$seq);
#$title=$arr[0];
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

