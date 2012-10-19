open INFILE,"<Gene_Name_ID_IDConverter";
open INFILEa,"<fusion_gene_unique";
open OUTFILE,">fusion_gene_unique_ID";
open OUTFILEa,">fusion_gene_unique_ID_error_1";
open OUTFILEb,">fusion_gene_unique_ID_error_2";
while(<INFILE>)
{
	chomp;
	s/\r$//g;
	@arr=split(/\t+/,$_);
	$up=uc($arr[0]);
	$hash{$arr[0]}=$arr[1];
	$hash_up{$up}=$arr[1];
}

while(<INFILEa>)
{
	chomp;
        s/\r$//g;
	@arr=split(/\t+/,$_);
	$up_0=uc($arr[0]);
	$up_1=uc($arr[1]);
	if(exists($hash{$arr[0]}) && exists($hash{$arr[1]}))
	{
		if($hash{$arr[0]}=~/^\s*$/ || $hash{$arr[1]}=~/^\s*$/)
		{
		printf OUTFILEa "$arr[0]\t$arr[1]\n";
	        }
		else
		{
		printf OUTFILE "$hash{$arr[0]}\t$hash{$arr[1]}\n";
		}
	}
	elsif(exists($hash_up{$up_0}) && exists($hash_up{$up_1}))
	{
           	if($hash_up{$up_0}=~/^\s*$/ || $hash_up{$up_1}=~/^\s*$/)
		{
		printf OUTFILEa "$arr[0]\t$arr[1]\n";
	        }
		else
		{
		printf OUTFILE "$hash{$arr[0]}\t$hash{$arr[1]}\n";
		}

	
	}
	else
	{
		printf OUTFILEb "$arr[0]\t$arr[1]\n";
	}


}

#keys %hash;
#while(($key,$val)=each %hash)
#{
#	$num++;
#}
#print "$num\n";

