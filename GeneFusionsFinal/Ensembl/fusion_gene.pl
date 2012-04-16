###  perl fusion_gene.pl fusion_gene_unique_chimerdb

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

#open INFILE,"fusion_gene_unique";
open INFILE,"$ARGV[0]";
open OUTFILEb,">$ARGV[0]_unmapped";
open OUTFILEc,">exon_fusion_$ARGV[0]";
open OUTFILEd,">$ARGV[0]_mapped";
#while(($key,$val)=each %hash)
while(<INFILE>)
{
        chomp;
        s/\r$//g;
        @gene=split(/\s+/,$_);
        if(exists($hash2{"$gene[0]"})&& exists($hash2{"$gene[1]"}))
	{
                printf OUTFILEd "$gene[0]\t$gene[1]\n";
		@v=@{$hash2{$gene[0]}};
		@w=@{$hash2{$gene[1]}};
		for($i=0;$i<@{$v[0]};$i++)
		{
			$x=$v[0][$i];
			@a=split(/\|/,$x);
			$xstrand=$a[4];
			$xstart=$a[1];
			$xend=$a[2];
			for($j=0;$j<@{$w[0]};$j++)
			{
				$y=$w[0][$j];
				@a=split(/\|/,$y);
				$ystrand=$a[4];
				$ystart=$a[1];
				$yend=$a[2];
				@ax=split(/\|/,$x); 
				@ay=split(/\|/,$y); 
				$xl=length($v[1][$i]);
				$yl=length($w[1][$j]);
				$title=">genefusions:$ax[5]:$ay[5]:$ax[3]:$ay[3]:$xl:$yl";
				$splicing="$v[1][$i]$w[1][$j]";
				printf OUTFILEc "$title\n";
				printf OUTFILEc "$splicing\n";
                                $title=">genefusions:$ay[5]:$ax[5]:$ay[3]:$ax[3]:$yl:$xl";
				$splicing="$w[1][$j]$v[1][$i]";
				printf OUTFILEc "$title\n";
				printf OUTFILEc "$splicing\n";



			}
		}
		
	}
	else
	{
                printf OUTFILEb "$gene[0]\t$gene[1]\n";

	}
}
