import itertools
import os
from pprint import pprint
from warnings import filterwarnings

import ccal
import numpy as np
import pandas as pd
import plotly as pl

filterwarnings('ignore')

pl.offline.init_notebook_mode(connected=True)
