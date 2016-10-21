# PTPop

PTPop provides a dynamic, real-time view of IEEE 1588 Precision Time
Protocol domains operating on a network. The name is yet another, more
playful variant of other popular monitoring tools (e.g. top, ntop, htop,
etc.)

Another tool that provides this sort of functionality in a graphical
form-factor is the Meinberg PTP Monitor, available at
http://www.meinbergglobal.com/english/sw/#ptp-mon .


## License

Commercial and private use are permitted. Distribution, modification,
and sublicensing at the moment are all forbidden. Specific copyright
details T.B.D, and will be provided in the file LICENSE.md.


## Pre-Requisites

Maintained in the `setup.py` file. The following command will
automatically handle their installation.

```
pip install pypcap
```


## Usage

For use in your application, import the library with `import ptpop`.

For command line usage, see usage document with:

```
(ptpop)root@raspberrypi:~/ptpop# python -m ptpop.Console -h
```

### Example

```
(ptpop)root@raspberrypi:~/ptpop# python -m ptpop.Console -n 4 -l
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
