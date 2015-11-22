"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    return dct.ReadFixedWidth(dat_file, compression='gzip')

def ValidatePregnum(resp):
    """Validate pregnum in the respondent file.

    resp: respondent DataFrame
    """

    # read the pregnancy frame
    df = nsfg.ReadFemPreg() 

    # make the map from caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(df)

    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.items():

        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if pregnum != len(preg_map[resp.caseid[index]]):
            return False
    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = ReadFemResp()

    assert(len(df) == 7643)
    assert(df.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(df))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
