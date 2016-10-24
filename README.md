# PTPop

PTPop provides a dynamic, real-time view of IEEE 1588 Precision Time
Protocol domains operating on a network. The name is yet another, more
playful, variant of other popular monitoring tools (e.g. top, ntop, htop,
etc.)

Another tool that provides this sort of functionality in a graphical
form-factor is the Meinberg PTP Monitor, available at
http://www.meinbergglobal.com/english/sw/#ptp-mon .


## License

The user of this software is free to use it for any purpose, to
distribute it, to modify it, and to distribute modified versions of the
software, under the terms of the *Apache License 2.0* contained in
LICENSE.txt, without concern for royalties.


## Pre-Requisites

Install the `libpcap` development resources (headers, etc.) accordingly
for your operating system, e.g.:

```
$ sudo apt-get install libpcap-dev python-dev
```

The following command will automatically handle the remainder of the
installation:

```
$ sudo pip install ptpop
Downloading/unpacking ptpop
  Downloading ptpop-1.0.2.tar.gz
  Running setup.py (path:/tmp/pip_build_root/ptpop/setup.py) egg_info for package ptpop

Downloading/unpacking pypcap (from ptpop)
  Downloading pypcap-1.1.5.tar.gz (44kB): 44kB downloaded
  Running setup.py (path:/tmp/pip_build_root/pypcap/setup.py) egg_info for package pypcap
    Found pcap headers in /usr/include/pcap/pcap.h
    Found libraries in /usr/lib/x86_64-linux-gnu/libpcap.a
    No pcap-int.h found
    found pcap_setdirection
    found pcap_setnonblock
    found pcap_compile_nopcap function
    found pcap_file function

Installing collected packages: ptpop, pypcap
  Running setup.py install for ptpop

    Installing ptpop script to /usr/local/bin
  Running setup.py install for pypcap
    Found pcap headers in /usr/include/pcap/pcap.h
    Found libraries in /usr/lib/x86_64-linux-gnu/libpcap.a
. . .
Successfully installed ptpop pypcap
Cleaning up...
```


## Usage

For use in your application:

```
# python
Python 2.7.9 (default, Mar  8 2015, 00:52:26)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pcap
>>> from ptpop import *
>>> def handle(ts, pkt):
...     print str(ts) + ": " + str(PtpPacket(pkt))
...
>>> pc = pcap.pcap("eth0")
>>> pc.setfilter('dst port 319 or dst port 320')
>>> pc.loop(5, handle)
1477337497.62: <ptp announce ID: 0x0050b6fffe5d3bd3 169.254.134.126 -> 224.0.1.129 seq: 5729>
1477337497.62: <ptp follow-up ID: 0x0050b6fffe5d3bd3 169.254.134.126 -> 224.0.1.129 seq: 11459>
1477337498.62: <ptp sync ID: 0x0050b6fffe5d3bd3 169.254.134.126 -> 224.0.1.129 seq: 11460>
1477337498.62: <ptp follow-up ID: 0x0050b6fffe5d3bd3 169.254.134.126 -> 224.0.1.129 seq: 11460>
1477337514.62: <ptp sync ID: 0x0050b6fffe5d3bd3 169.254.134.126 -> 224.0.1.129 seq: 11476>
```

For command line usage, see usage document with:

```
$ ptpop -h
```

### Example

Run the following as the `root` user:

```
$ sudo -s
# ptpop -n 4 -l
Fri Oct 21 2016 07:26:47.385 UTC
remote          Dly St Dom Pr1  Cl Acc   Var  Pr2       Uniq       SyncT  DlyT  AnnT
====================================================================================

Fri Oct 21 2016 07:26:50.392 UTC
remote          Dly St Dom Pr1  Cl Acc   Var  Pr2       Uniq       SyncT  DlyT  AnnT
====================================================================================
169.254.134.126 E2E  - 129 128  13 0xfe 28768 128 0050b6fffe5d3bd3   -     -     -

Fri Oct 21 2016 07:26:53.406 UTC
remote          Dly St Dom Pr1  Cl Acc   Var  Pr2       Uniq       SyncT  DlyT  AnnT
====================================================================================
169.254.134.126 E2E  - 129 128  13 0xfe 28768 128 0050b6fffe5d3bd3  1.00   -    2.00

Fri Oct 21 2016 07:26:56.417 UTC
remote          Dly St Dom Pr1  Cl Acc   Var  Pr2       Uniq       SyncT  DlyT  AnnT
====================================================================================
169.254.134.126 E2E  - 129 128  13 0xfe 28768 128 0050b6fffe5d3bd3  1.00   -    2.00
```


## Contribute

Please fork the GitHub project (http://github.com/andrewburnheimer/ptpop),
make any changes, commit and push to GitHub, and submit a pull request.


### Develop

Use a Python environment manager, such as http://virtualenv.pypa.io :

1. Run the following once, `virtualenv ~/.venvs/ptpop`

2. Use `source ~/.venvs/ptpop/bin/activate` to enter the environment to
run the application, continue development, or test.

3. Execute tests with commands like `python ptpop/AnnounceMessage.py` or
with the PyZen continuous test runner: `pyzen ptpop/PtpNeighbor.py`


## Contact

This project was initiated by Andrew Burnheimer.

* Email:
  * andrew.burnheimer@nbcuni.com
* Twitter:
  * @aburnheimer
* Github:
  * http://github.com/andrewburnheimer
