# Args:
#   [1] : REF_GENOME - Path to reference genome BAM file was aligned to
#   [2] : FASTQ_1 - First FASTQ with paired end data
#   [3] : FASTQ_2 - Second FASTQ with paired end data
#   [4] : OUT_FILE - Path where output will be written in BAM format

version='1.0.0'
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

$bwa aln -t 8  $REF_GENOME $FASTQ_1 > $reads_1_base.fai
$bwa aln -t 8  $REF_GENOME $FASTQ_2 > $reads_2_base.fai

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
