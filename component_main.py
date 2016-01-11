'''
Created on Jun 13, 2014
Last update July 3 2014
@author: raniba
'''

import os

from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    Align two fastq files and generate a sam file
    '''
    def __init__(self, component_name='run_bwa',
                 component_parent_dir=None, seed_dir=None):
        self.version = "1.0.4"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name,
                                        component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        '''
        Align Fastq Files and generate a Bam file
        '''

        bwa_runner = os.path.join(self.seed_dir, "run_bwa_backtrack.sh")

        bwa_path = self.requirements['bwa']
        samtools_path = self.requirements['samtools']

        seq1 = self.args.seq1
        seq2 = self.args.seq2

        reference = self.args.reference
        outfile = self.args.outfile

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
def _main():
    '''main function'''
    align_bwa_pe = Component()
    align_bwa_pe.args = component_ui.args
    align_bwa_pe.run()

if __name__ == '__main__':
    import component_ui
    _main()
