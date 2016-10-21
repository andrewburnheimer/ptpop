#!/usr/local/bin/python
'''
Console Class
'''
'''
To Do:
    -
'''

from Listener import Listener
import time
import os

# =============================================================================
# Console
# 
# Inheriting from `object` (top-level class)
# =============================================================================
class Console(object):
    def __init__(self, args=None):
        '''
        Console Initialization
        Input Attributes:
        -----------------
        self.args -> argparse.Namespace: object holding attributes set
                                         on command-line.
        '''

        # Default Values
        delay = 3.0
        number = 1 # XXX should be = 0
        command = [ ]
        interface = 'eth0'
        listen = False
        host = 'localhost'
        if args:
            delay = float(args.delay) if args.delay else delay
            number = args.number if (args.number != None) else number
            command = args.command if args.command else command
            interface = args.interface if args.interface else interface
            listen = args.listen if args.listen else listen
            host = args.host if args.host else host

        # Input Checks
        if command != [ ]:
            raise NotImplementedError('Issuing commands to hosts has ' +
                    'not been implemented yet')

        # init ...
        if listen:
            self.listener = Listener(interface)
            key = '''
remote          Dly St Dom Pr1  Cl Acc   Var  Pr2       Uniq       SyncT  DlyT  AnnT
===================================================================================='''.strip()


            while number > 0:
                # Report output directly to console
                fmt='%a %b %d %Y %H:%M:%S'
                t = time.time()
                time_str = time.strftime(fmt, time.localtime(t))
                time_msecs = int((t - int(t)) * 1000)

                print time_str + '.%03d ' % (time_msecs) + time.tzname[0]
                print key

                # output data seen in since last iteration
                neighbor_stats = self.listener.ptp_neighbors
                for neighbor in neighbor_stats:
                    print self.listener.ptp_neighbors[neighbor]

                print
                number -= 1
                if number <= 0:
                    exit(0)
                    # No need to wait after the last iteration
                time.sleep(delay)

            # Enter into the interactive environment, exit when q is
            # issued

        else:
            for supplied_command in command:
                command = supplied_command.lower()

                if command == 'rv' or command == 'readvar':
                    None
                    # Assuming to be similar to NTPQ
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
                    # Assuming to be similar to NTPQ
            #     remote           refid      st t when poll reach   delay   offset  jitter
            #==============================================================================
            #*useclsifl158.tf 3.199.96.254     2 u   14 1024  377    1.582    0.186   0.919
                else:
                    raise NotImplementedError('Unknown command, \'' +
                            command + '\'')

# __main__.py is executed when the package is instantiated
import argparse

def main():
    version = ""
    with open(os.path.join('./', 'VERSION')) as version_file:
        version = version_file.read().strip()

    parser = argparse.ArgumentParser(prog='ptpop', description='Gain ' +
        'insight into the operations of IEEE 1588 Precision Time Protocol ' +
        'domains on a network. Press the \'q\' key to quit.')

    command_choices=['readvar', 'rv', 'peers']
    parser.add_argument('host', type=str, nargs='?', help='each of the ' +
                        'commands will be sent to the PTP servers ' +
                        'running on the host provided, localhost by ' +
                        'default.')
    parser.add_argument('-c', '--command', type=str, action='append',
                        help='a command to run on the provided host, ' +
                        'i.e. ' + str(command_choices) + ', \'readvar\' ' +
                        'by default. Multiple commands can be issued.')
    parser.add_argument('-i', '--interface', type=str,
                        help='interface to issue commands on or to ' +
                        'observe on in listen mode.')
    parser.add_argument('-l', '--listen', action='store_true',
                        help='don\'t contact any PTP servers, but ' +
                        'report on any services currently observed ' +
                        'on the network, instead.')
    parser.add_argument('-d', '--delay', metavar='SECS.TENTHS', type=str,
                        help='Specifies the delay between screen ' +
                        'updates when interactive. Can be changed while ' +
                        'running using the \'d\' key. Negative ' +
                        'numbers are not allowed. Setting this value ' +
                        'to 0 is the same as issuing the \'-n 1\' ' +
                        'option.')
    parser.add_argument('-n', '--number', metavar='COUNT', type=int,
                        help='Specifies the maximum number of iterations ' +
                        'in interactive mode before ending.')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + version)

    args = parser.parse_args()
    try:
        c = Console(args)

    except Exception as e:
        print type(e).__name__ + ": " + str(e.message)
        exit(-1)

if __name__ == '__main__':
    main()
