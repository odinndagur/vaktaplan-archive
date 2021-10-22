import camelot
import numpy as np
import pandas as pd
import json
from stuff import *

# file = "../input/11okt10nov.pdf"
file ='/Users/odinndagur/Code/Github/vaktaplan/input/11okt10nov.pdf'
cellinfo = []



tables = camelot.read_pdf(file,pages='1-end')
cellinfo = tablestocellinfo(tables)

with open('celldata1.json', 'w') as f:
    json.dump(cellinfo,f)

docs = []

# tables[0].col = tables[0].df.col + 1
# tables[0].row = tables[0].df.row + 2

# tables[1].col = tables[1].df.col + 1
# tables[1].row = tables[1].df.row + 1


cleanuptables(tables,docs)
