open INFILE,"fusion_gene_unique";
open OUTFILE,">gene_unique";

while(<INFILE>)
{
	chomp;
	s/\r$//g;
	@a=split(/\t/,$_);
	$hash{$a[0]}++;
	$hash{$a[1]}++;
}
keys %hash;
while(($key,$val)=each %hash)
{
	printf OUTFILE "$key\n";
}

open INFILEa,"exon_line";
open OUTFILEa,">gene_exon";
while($title=<INFILEa>)
{
	$seq=<INFILEa>;
	chomp($title);
	chomp($seq);
	$title=~s/\r$//g;
	$seq=~s/\r$//g;
	@a=split(/\|/,$title);
	$genename=$a[5];
	$num=@{$hash2{$genename}[0]};
	$hash2{$genename}[0][$num]=$title;
	$hash2{$genename}[1][$num]=$seq;
}
keys %hash2;
while(($key,$val)=each %hash2)
{
	@v=@{$val};
	printf OUTFILEa "#$key\n";
	for($i=0;$i<@{$v[0]};$i++)
	{
		printf OUTFILEa "$v[0][$i]\n";
		printf OUTFILEa "$v[1][$i]\n";

	}
}

open OUTFILEb,">gene_notfind";
open OUTFILEd,">gene_find";
open OUTFILEc,">splicing_exon";
keys %hash;
while(($key,$val)=each %hash)
{
	if(exists($hash2{$key}))
	{
		printf OUTFILEd "$key\n"; 

		@v=@{$hash2{$key}};
		for($i=0;$i<@{$v[0]};$i++)
		{
			$x=$v[0][$i];
			@a=split(/\|/,$x);
			$xstrand=$a[4];
			$xstart=$a[1];
			$xend=$a[2];
		    for($j=0;$j<@{$v[0]};$j++)
		    {
			$y=$v[0][$j];
                        @a=split(/\|/,$y);
			$ystrand=$a[4];
			$ystart=$a[1];
			$yend=$a[2];
			if($xstrand == 1)
			{
				if($ystart>=$xend)
				{
                                        @ax=split(/\|/,$x); 
                                        @ay=split(/\|/,$y); 
                                        $xl=length($v[1][$i]);
                                        $yl=length($v[1][$j]);
					$title=">splicing:$ax[5]:$ay[5]:$ax[3]:$ay[3]:$xl:$yl";
					$splicing="$v[1][$i]$v[1][$j]";
					printf OUTFILEc "$title\n";
					printf OUTFILEc "$splicing\n";
				}
			}
			elsif($xstrand == -1)
			{
				if($yend<=$xstart)
				{

                                        @ax=split(/\|/,$x); 
                                        @ay=split(/\|/,$y); 
                                        $xl=length($v[1][$i]);
                                        $yl=length($v[1][$j]);
					$title=">splicing:$ax[5]:$ay[5]:$ax[3]:$ay[3]:$xl:$yl";
					$splicing="$v[1][$i]$v[1][$j]";
					printf OUTFILEc "$title\n";
					printf OUTFILEc "$splicing\n";
				}
			}


		    }
		}
		
	}
	else
	{
		printf OUTFILEb "$key\n"; 
	}
}
