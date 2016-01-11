'''
Created on Jun 13, 2014

@author: raniba
'''

import os
import component_ui


from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    Align two fastq files and generate a sam file
    '''
    def __init__(self, component_name='run_bwa', component_parent_dir=None, seed_dir=None):
       self.version = "0.0.1"

        ## initialize ComponentAbstract
       super(Component, self).__init__(component_name, component_parent_dir, seed_dir)


    def make_cmd(self):
        '''
        Align Fastq Files and generate a Bam file
        '''


        bwa_runner = os.path.join(self.seed_dir,'run_bwa_backtrack.sh')
        bwa_path = self.requirements['bwa']
        samtools_path = self.requirements['samtools']

        #seq1 = self.args.seq1
        #seq2 = self.args.seq2

        seq1 = "/share/lustre/raniba/miseq_analysis_pipeline/fastq/SA495/SA495-Normal_S8_L001_R1_001.fastq"
        seq2 = "/share/lustre/raniba/miseq_analysis_pipeline/fastq/SA495/SA495-Normal_S8_L001_R2_001.fastq"


        #reference = self.args.reference
        reference = "/share/lustre/raniba/miseq_analysis_pipeline/reference/GRCh37-lite.fa"
        #outfile = self.args.outfile
        outfile = "test.bam"
        #seq1_base = os.path.basename(seq1)
        #seq2_base = os.path.basename(seq2)



        cmd = 'sh'
        cmd_args = [
            bwa_runner,
            reference,
            seq1,
            seq2,
            outfile,
            bwa_path,
            samtools_path
        ]

        return cmd, cmd_args


# to run as stand alone
#def _main():
#    '''main function'''
rehead = Component()
#rehead.args = component_ui.args
rehead.run()

#if __name__ == '__main__':

#    import component_ui

#    _main()
