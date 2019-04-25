#!/usr/bin/env python3
"""tests for max_rep.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string
import max_rep

prg = "./max_rep.py"

# --------------------------------------------------
def test_usage():
    """usage"""
    rv1, out1 = getstatusoutput(prg)
    assert rv1 > 0
    assert re.match("usage", out1, re.IGNORECASE)

    rv2, out2 = getstatusoutput("{} -w 275 -r foo".format(prg))
    assert rv2 > 0
    assert re.match("usage", out2, re.IGNORECASE)


