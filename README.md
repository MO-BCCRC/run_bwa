#run_bwa : Paired Ends Alignment using BWA


```
Development information

date created : Jun 13 2014
last update  : Oct 6  2014
Developer    : Rad Aniba (raniba@bccrc.ca)
Input        : Fastq files (R1 and R2), reference genome
Output       : Bam file
Seed used    : BWA

```


###Usage
This component is using BWA to do a paired end reads alignment, for more information about the command called you can refer to the seed or to the component_main.py of this repo

###Dependencies

- BWA
- python
- samtools


###Example

Calling the component is easy. The seed is a simple shell script that takes 2 fastq files and a reference geneome file, produces a sam files and convert the sam file into a bam file using samtools

```
# Args:
#   [1] : REF_GENOME - Path to reference genome BAM file was aligned to
#   [2] : FASTQ_1 - First FASTQ with paired end data
#   [3] : FASTQ_2 - Second FASTQ with paired end data
#   [4] : OUT_FILE - Path where output will be written in BAM format


REF_GENOME=$1

FASTQ_1=$2

FASTQ_2=$3

OUT_FILE=$4

bwa=$5
samtools=$6

#bwa mem $REF_GENOME $FASTQ_1 $FASTQ_2 | samtools view -bS - > $OUT_FILE


reads1=${FASTQ_1##*/}
reads_1_base=${reads1%.*}

reads2=${FASTQ_2##*/}
reads_2_base=${reads2%.*}


#echo $filename

$bwa aln -t 8 $REF_GENOME $FASTQ_1 > $reads_1_base.fai
$bwa aln -t 8 $REF_GENOME $FASTQ_2 > $reads_2_base.fai

$bwa sampe $REF_GENOME $reads_1_base.fai $reads_2_base.fai $FASTQ_1 $FASTQ_2 > $reads_1_base$reads_2_base.sam
$samtools view -bSh -o $OUT_FILE $reads_1_base$reads_2_base.sam

if [ -f $reads_1_base.fai ]
then
 rm $reads_1_base.fai
fi

if [ -f $reads_2_base.fai ]
then
 rm $reads_2_base.fai
fi

if [ -f $reads_1_base$reads_2_base.sam ]
then
  rm $reads_1_base$reads_2_base.sam
fi

```


###Known issues

- Job lost when submitted to the cluster on rocks (date of issue reporting : Jul 2nd 2014, Jira Ticket : PFD-150 )

###Last updates



### test data
Reference : /share/lustre/raniba/miseq_analysis_pipeline/reference/GRCh37-lite.fa   
seq1 : /share/lustre/raniba/miseq_analysis_pipeline/fastq/SA495/SA495-Normal_S8_L001_R1_001.fastq   
seq2 : /share/lustre/raniba/miseq_analysis_pipeline/fastq/SA495/SA495-Normal_S8_L001_R2_001.fastq   
outfile : test.bam   

bwa path : /share/lustre/raniba/miseq_analysis_pipeline/miseq-pipeline/software/bwa-0.7.5a/bwa   
samtools path : /share/lustre/raniba/miseq_analysis_pipeline/miseq-pipeline/software/samtools-0.1.19/samtools  


