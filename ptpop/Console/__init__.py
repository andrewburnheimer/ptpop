#!/usr/local/bin/python
'''
Console Class
Informative Notes T.B.D...
'''
__version__ = '$Id$'
'''
To Do:
    -
'''

#import inspect
import argparse

# =============================================================================
# Console
# 
# Inheriting from `object` (top-level class)
# =============================================================================
class Console(object):
    #def __init__(self, assign_input={}, *optional_value_input, **optional_dict_input):
    def __init__(self, args=None):
        '''
        Console Initialization
        Keyword Arguments:
        ------------------
        T.B.D.

        Input Attributes:
        -----------------
        self.args -> argparse.Namespace: object holding attributes set
                                         on command-line.

        Additional Attributes:
        ----------------------
        T.B.D.

        '''

        # Default Values
        delay = 3.0
        number = 0
        if args:
            delay = float(args.delay) if args.delay else delay
            number = args.number if args.number else number

        # Input Checks
        if args.commands == [ ]:
            raise NotImplementedError('Interactive mode has not been ' +
                    'implemented yet')

        # init ...
        for supplied_command in args.commands:
            command = supplied_command.lower()

            if command == 'rv':
                None
                # "To do RV"
        # root@raspberrypi:/home/puppet# ntpq -n -c rv -c peers
        #associd=0 status=0615 leap_none, sync_ntp, 1 event, clock_sync,
        #version="ntpd 4.2.6p5@1.2349-o Mon Nov  2 04:29:47 UTC 2015 (1)",
        #processor="armv6l", system="Linux/4.1.17+", leap=00, stratum=3,
        #precision=-20, rootdelay=2.916, rootdisp=60.561,
        #refid=3.44.174.43,
        #reftime=da7f3666.54078831  Mon, Feb 29 2016 21:28:06.328,
        #clock=da7f38cd.57a72dc6  Mon, Feb 29 2016 21:38:21.342,
        #peer=7185, tc=8,
        #mintc=3, offset=9.208, frequency=-48.954, sys_jitter=0.000,
        #clk_jitter=16.919, clk_wander=4.216
            elif command == 'peers':
                None
                # "To do Peers"
        #     remote           refid           st t when poll reach delay   offset  jitter
        #     ==============================================================================
        #     *3.44.174.43     3.199.96.254     2 u   90  256  377  1.558    9.208   4.993
            else:
                raise NotImplementedError('Unknown command: ' + command)



#    def __Private_Method(self):
#        '''
#        Private Module
#        '''
        # Inputs
        # Module Code
        # Output

#    def Public_Method(self):
#        '''
#        Private Module
#        '''
        # Inputs
        # Module Code
        # Output

#    def Public_Static_Method():

#    def Public_Class_Method(cls):


# =============================================================================
# Private Module Functions
# =============================================================================
#def __Private_Function(inputs):
#        '''
#        Private Function
#        '''
#        # Inputs
#        # Function code ...
#        return outputs

# =============================================================================
# Public Module Functions
# =============================================================================
#def Public_Function(inputs):
#        '''
#        Public Function
#        '''
#        # Inputs
#        # Function code ...
#        return outputs

#==============================================================================
# Class Test
#==============================================================================
if __name__ == '__main__':
    # Test class
    pass

def main():
    parser = argparse.ArgumentParser(prog='ptpop', description='Gain ' +
        'insight into the operations of IEEE 1588 Precision Time Protocol ' +
        'domains on a network. Press the \'q\' key to quit.')

    command_choices=['rv', 'peers']
    parser.add_argument('commands', metavar='command', type=str, nargs='*',
                        help='a command to run, then exit when finished: '
                        + str(command_choices) + '. Otherwise, run ' +
                        'interactively.')
    parser.add_argument('-d', '--delay', metavar='secs.tenths', type=str,
                        help='Specifies the delay between screen ' +
                        'updates, can be changed using the \'d\' key in ' +
                        'the interactive mode. Negative numbers are not ' +
                        'allowed. Setting this value to 0 is the same ' +
                        'as issuing the \'-n 1\' option.')
    parser.add_argument('-n', '--number', metavar='count', type=int,
                        help='Specifies the maximum number of iterations, ' +
                        'before ending')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s $Id$')

    args = parser.parse_args()
    try:
        c = Console(args)
    #    break
    except Exception as e:
        print type(e).__name__ + ": " + str(e.message)
        exit(-1)
        #print "Oops! " + str(inspect.getmembers(e))
