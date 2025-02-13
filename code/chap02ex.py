"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2

def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    _, value = max([(freq, value) for value, freq in hist.Items()])
    return value


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    return sorted(hist.Items(), key=itemgetter(1), reverse=True)
  

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)
 
    # explore the weight difference between first babies and others
    print('CohenEffectSize of weight: ' + str(thinkstats2.CohenEffectSize(firsts['totalwgt_lb'],
                others['totalwgt_lb']))) 

    # Explore the difference in pregnancy length between first babies and
    # others.
    print('CohenEffectSize of pregnancy length: ' + str(thinkstats2.CohenEffectSize(firsts['prglngth'], others['prglngth'])))  
   
    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)

    # test AllModes
    modes = AllModes(hist)
    assert(modes[0][1] == 4693)

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
