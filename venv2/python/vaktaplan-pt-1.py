import camelot
import numpy as np
import pandas as pd
import json

# file = "../input/11okt10nov.pdf"
file ='/Users/odinndagur/Code/Github/vaktaplan/input/11okt10nov.pdf'
cellinfo = []

tables = camelot.read_pdf(file,pages='1-end')
for i in range(tables.n):
    table = tables[i]
    for j in range(len(table.cells)):
        col = table.cells[j]
        for ii in range(len(col)):
            cell = col[ii]
            temp = (cell.text,cell.x1-1,cell.y1-1,cell.x2+1,cell.y2+1,i,j,ii,-1,-1,-1)
            cellinfo.append(temp)
            # print(temp)
with open('celldata1.json', 'w') as f:
    json.dump(cellinfo,f)
# for table in tables:
#     for col in table.cells:
#         for cell in col:
#             temp = (cell.text,cell.x1,cell.y1,cell.x2,cell.y2,i,j,ii)
#             print(temp)

docs = []
# out = "../output/"

# tables[0].col = tables[0].df.col + 1
# tables[0].row = tables[0].df.row + 2

# tables[1].col = tables[1].df.col + 1
# tables[1].row = tables[1].df.row + 1



out = '/Users/odinndagur/Code/Github/vaktaplan/output'
for i in range(0,tables.n, 2):
    df = tables[i].df #even
    df2 = tables[i+1].df #odd

    df2 = df2.iloc[:,1:]
    df2.iloc[0,0] = "Starfsmaður"
    headers = df2.iloc[0]
    # headers.to_csv(out + "headers" + str(i+1) + ".csv")

    df = df.iloc[2: , 1:]
    df2 = df2.iloc[1: , :]

    df.index = df.index - 1

    df.columns = headers
    df2.columns = headers

    # df.dropna(how='all',axis=1)
    # df2.dropna(how='all',axis=1)

    total = df.append(df2, ignore_index = True)
    total.to_csv(out + "vaktaplan" + str(int(i/2)) + ".csv")
    docs.append(total)

first = docs[0]
for i in range(len(docs)):
    if(i != 0):
        temp = docs[i].iloc[:,1:]
        first = pd.concat([first, temp], axis=1)

first.to_csv(out + "ALLT.csv")