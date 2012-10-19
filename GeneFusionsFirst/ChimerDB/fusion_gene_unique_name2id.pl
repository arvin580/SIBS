open INFILE,"<Gene_Name_ID_Ensemble";
open INFILEa,"<fusion_gene_unique";
open OUTFILE,">fusion_gene_unique_name2id_maped";
open OUTFILEa,">fusion_gene_unique_name2id_unmaped";
while(<INFILE>)
{
	chomp;
	s/\r$//g;
	@arr=split(/\t+/,$_);
	$hash{$arr[1]}.="$arr[0]&";
}
while(<INFILEa>)
{
	chomp;
	s/\r$//g;
	@arr=split(/\t+/,$_);
	$name1=$arr[0];
	$name2=$arr[1];
	if(exists($hash{$name1}) && exists($hash{$name2}))
	{
		$id1=$hash{$name1};
		$id2=$hash{$name2};
		$id1=~s/&$//g;
		$id2=~s/&$//g;
		@arr1=split(/&/,$id1);
		@arr2=split(/&/,$id2);
		for($i=0;$i<@arr1;$i++)
		{
			for($j=0;$j<@arr2;$j++)
			{
				printf OUTFILE "$arr1[$i]\t$arr2[$j]\n"; 
			}
		}
	}
	else
	{
				printf OUTFILEa "$name1\t$name2\n"; 
	}
}


open INFILEb,"<Gene_Name_ID_IDConverter";
open INFILEc,"<fusion_gene_unique_name2id_unmaped";
open OUTFILEb,">fusion_gene_unique_name2id_unmaped_mapped";
open OUTFILEc,">fusion_gene_unique_name2id_unmaped_nomapped";
while(<INFILEb>)
{
	chomp;
	s/\r$//g;
	@arr=split(/\t/,$_);
	if(!$arr[1]=~/^\s*$/)
	{
	$hash2{$arr[0]}="$arr[1]";
        }
}
while(<INFILEc>)
{
	chomp;
	s/\r$//g;
	@arr=split(/\t+/,$_);
	$name1=$arr[0];
	$name2=$arr[1];
	if(exists($hash2{$name1}) && exists($hash2{$name2}))
	{
		$id1=$hash2{$name1};
		$id2=$hash2{$name2};
				printf OUTFILEb "$id1\t$id2\n"; 
	}
	else
	{
				printf OUTFILEc "$name1\t$name2\n"; 
	}
}
