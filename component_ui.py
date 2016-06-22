# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:34:48 2013

@author: jtaghiyar
"""
import argparse

mutationSeq_version="4.3.6"

#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(prog='mutationSeq',
                                 description = '''mutationSeq: a feature-based classifier
                                 for somatic mutation detection in
                                 tumour-normal paired sequencing data''')

mandatory_options = parser.add_argument_group("required arguments")

exgroup = parser.add_mutually_exclusive_group()

parser.add_argument("--tumour",
                    help='path to the input file')
parser.add_argument("--normal",
                    help='path to the input file')
parser.add_argument("--reference",
                    required=True,
                    help='path to the input file')
parser.add_argument("--model",
                    required=True,
                    help='path to the input file')

## mandatory options
mandatory_options.add_argument("-c", "--config",
                               default=None,
                               #required=True,
                               help='''specify the path/to/metadata.config file used to add
                               meta information to the output file''')

exgroup.add_argument("-f", "--positions_file",
                     default=None,
                     help='''input a file containing a list of positions each of which in
                     a separate line, e.g. chr1:12345\nchr2:23456''')

parser.add_argument("-e" , "--export_features",
                    default=None,
                    help='''save exported feature vector to the specified path''')

parser.add_argument("-l", "--log_file",
                    default="mutationSeq_run.log",
                    help='''specify name or path of the log file''')

mandatory_options.add_argument("-o", "--out",
                               default=None,
                               #required=True,
                               help='''specify the path/to/out.vcf to save output to a file''')

## optional arguments
parser.add_argument("-a", "--all",
                    default=False, action="store_true",
                    help= '''force to print out even if the predicted probability of the
                    candidate position(s) is(are) less than the specified threshld.''')

parser.add_argument("-b", "--buffer_size",
                    default="2G",
                    help='''specify max amount of memory usage''')

parser.add_argument("--coverage",
                    default=4,
                    type=int,
                    help='''specify min depth (coverage) to be considered''')

parser.add_argument("-d", "--deep",
                    default=False, action="store_true",
                    help='''deepseq data analysis''')

exgroup.add_argument("-i", "--interval",
                     default=None,
                     help='''specify an interval "chr[:start-stop]"''')

parser.add_argument("--no_filter",
                    default=False, action="store_true",
                    help= '''force to print out even if the position(s) does(do) not satisfy
                    the initial criteria for Somatic call''')

parser.add_argument("-n", "--normalized",
                    default=False, action="store_true",
                    help='''If you want to test with normalized features
                    (the number of features are also different from non-deep)''')

parser.add_argument("--normal_variant",
                    default=25,
                    type=int,
                    help='''specify the max variant percentage in the normal bam file''')

parser.add_argument("-p", "--purity",
                    default=70,
                    type=int,
                    help='''pass sample purity to features''')

parser.add_argument("-q", "--mapq_threshold",
                    default=20,
                    type=int,
                    help='''set threshold for the mapping quality''')

parser.add_argument( "--baseq_threshold",
                    default=10,
                    type=int,
                    help='''set threshold for the base quality''')

parser.add_argument("--indl_threshold",
                    default=0.05, type=float,
                    help='''set threshold for INDL call''')

parser.add_argument("--manifest",
                    help='''path to the manifest file''')

parser.add_argument("-s", "--single",
                    default=False, action="store_true",
                    help='''single sample analysis''')

parser.add_argument("-t", "--threshold",
                    default=0.5, type=float,
                    help='''set threshold for positive call''')

parser.add_argument("--tumour_variant",
                    default=2,
                    type=int,
                    help='''specify the min number of variants in the tumour bam file''')

parser.add_argument("--features_only",
                    default=False, action="store_true",
                    help='''if true, only extracted features are exported''')

parser.add_argument("-v", "--verbose",
                    action="store_true", default=False,
                    help='''verbose''')

parser.add_argument( "--titan_mode",
                    action = 'store_true',
                    help='''runs preprocess.py (titan preprocessing mode)''')


args, unknown  = parser.parse_known_args()
