#!/usr/bin/env python
# coding=utf-8
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import h5py
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymongo
import seaborn as sns
from IPython.display import display
from matplotlib import cm
import gridfs
import bson
import json
import itertools as it

from topsacred.nbtools import (PANDAS_STYLE, sacred_stats, get_db_stats,
                               get_results)

# Pretty Pandas Dataframes
display(PANDAS_STYLE)
mpl.rcParams['savefig.pad_inches'] = 0
mpl.rcParams['savefig.bbox'] = 'tight'

__all__ = ['np', 'pd', 'pymongo', 'sns', 'plt', 'mpl', 'cm', 'h5py', 'gridfs',
           'sacred_stats', 'get_db_stats', 'get_results']
