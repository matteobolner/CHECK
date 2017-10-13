#
# CHECK
#
# @authors : Eric Pascolo
#

import argparse

####--------------------------------------------------------------------------------------------------------------

def cl_parser():
    """
    Parsing command line pars with argparse module
    """
    
    parser = argparse.ArgumentParser(description = '''
    CHECK : Cluster Health and Environment ChecKing system''',
    formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(   '--master', 
                            action = 'store_true' ,
                            required = False,
                            help = 'Master/slave flag')

    parser.add_argument(   '--install', 
                            action = 'store_true' ,
                            required = False,
                            help = 'Install checktest')

    # parser.add_argument(   '--daemon', 
    #                             type = str,
    #                             required = False,
    #                             choices=['start', 'submit', 'status','kill'],
    #                             help = 'Daemon command')
                                
    parser.add_argument(   '--check', '-ct',
                                type = str,
                                nargs='+',
                                required = False,
                                default = "-999",
                                help = 'List of check')                            

    parser.add_argument(   '--configuration', 
                                type = str,
                                required = False,
                                
                                help = 'Input file')

    parser.add_argument(   '--analysis', 
                                type = str,
                                required = False,
                                help = 'kind of analysis')
   
    parser.add_argument(   '--loglevel', 
                                type = str,
                                required = False,
                                help = 'Input file')
    
    parser.add_argument(   '--logfile', 
                                type = str,
                                required = False,
                                help = 'Input file')

    parser.add_argument(   '--checktest_directory', '-checkTD', 
                                type = str,
                                required = False,
                                help = 'check test directory')
    
    parser.add_argument(   '--hostlist', '-hpc', 
                                type = str,
                                required = False,
                                help = 'List of Hostname to Master submission')
    
    return parser.parse_args()

####--------------------------------------------------------------------------------------------------------------

def cl_convert_to_dict(args):
    """
    Convert args object in dictionary
    """

    convdict = vars(args)
    newdict =   dict([(vkey, vdata) for vkey, vdata in convdict.iteritems() if(vdata) ])
  
    return newdict

####--------------------------------------------------------------------------------------------------------------