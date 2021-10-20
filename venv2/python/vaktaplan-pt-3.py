import camelot
import numpy as np
import pandas as pd
import json

# file = "../input/11okt10nov.pdf"
file ='/Users/odinndagur/Code/Github/vaktaplan/input/11okt10nov.pdf'
global cellinfo

tables = camelot.read_pdf(file,pages='1-end')
# for i in range(tables.n):
#     table = tables[i]
#     for j in range(len(table.cells)):
#         col = table.cells[j]
#         for ii in range(len(col)):
#             cell = col[ii]
#             temp = (cell.text,cell.x1-1,cell.y1-1,cell.x2+1,cell.y2+1,i,j,ii,-1,-1,-1)
#             cellinfo.append(temp)
#             # print(temp)
with open('celldatawcolors.json') as f:
    cellinfo = [tuple(x) for x in json.load(f)]
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



for i in range(0, tables.n, 2):
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



    for cell in cellinfo:
        if cell[5] == i:
            text = cell[0]
            tablenumber = cell[5]
            colnumber = cell[6]
            rownumber = cell[7]
            r = cell[8]
            g = cell[9]
            b = cell[10]
            # if r > 0:
                # print(tables[tablenumber].cells[colnumber][rownumber].text, "tables i")
                # print(df.iloc[colnumber-2][rownumber-1], "df i")
                # df.iloc[colnumber-2][rownumber-1] += str(int(r*255)) + str(int(g*255)) + str(int(g*255))
                # print(tablenumber,colnumber,rownumber)
                # print(df.iloc[colnumber-2][rownumber-1])
        if cell[5] == i+1:
            text = cell[0]
            tablenumber = cell[5]
            colnumber = cell[6]
            rownumber = cell[7]
            r = cell[8]
            g = cell[9]
            b = cell[10]
            if r > 0 or g > 0 or b > 0:
                print(tablenumber,colnumber,rownumber)
                print(tables[tablenumber].cells[colnumber][rownumber].text, "tables i+1")
                print(df.iloc[colnumber-1][rownumber], "df i+1")
                # df.iloc[colnumber-2][rownumber-1] += str(int(r*255)) + str(int(g*255)) + str(int(g*255))
                # print(tablenumber,colnumber,rownumber)
                # print(df.iloc[colnumber-2][rownumber-1])



def colortoname(r,g,b):
    if r == 128 and g == 0 and b == 255:
        return "LRL"
    # if(r,g,b) == (128, 0, 255):
    #     return "LRL"
out = '/Users/odinndagur/Code/Github/vaktaplan/output'
# for i in range(0,tables.n, 2):
#     first = i
#     second = i+1
#     df = tables[i].df #even
#     df2 = tables[i+1].df #odd

#     df2 = df2.iloc[:,1:]
#     df2.iloc[0,0] = "Starfsmaður"
#     headers = df2.iloc[0]
#     # headers.to_csv(out + "headers" + str(i+1) + ".csv")

#     df = df.iloc[2: , 1:]
#     df2 = df2.iloc[1: , :]

#     df.index = df.index - 1

#     df.columns = headers
#     df2.columns = headers

    
        # temp = (cell.text,cell.x1-1,cell.y1-1,cell.x2+1,cell.y2+1,i,j,ii,-1,-1,-1)



    # df.dropna(how='all',axis=1)
    # df2.dropna(how='all',axis=1)
    # first = 0
    # second = 1
# for cell in cellinfo:
#     if cell[5] == 0:
#         text = cell[0]
#         tablenumber = cell[5]
#         colnumber = cell[6]
#         rownumber = cell[7]
#         r = cell[8]
#         g = cell[9]
#         b = cell[10]
#         if r > 0:
#             print(tablenumber,colnumber,rownumber)
            # if(rownumber <= 10 or colnumber <= 10):
        # print("lol")
            # print(rownumber,colnumber)
            # print(df[colnumber-2][rownumber-1])
                # df.iloc[rownumber][colnumber] = text + str(colortoname(int(r * 255),int(g*255),int(b*255)))
        # tables[tablenumber].cells[rownumber-1][colnumber-1]

    # total = df.append(df2, ignore_index = True)
    # total.to_csv(out + "vaktaplan" + str(int(i/2)) + ".csv")
    # docs.append(total)

# first = docs[0]
# for i in range(len(docs)):
#     if(i != 0):
#         temp = docs[i].iloc[:,1:]
#         first = pd.concat([first, temp], axis=1)

# first.to_csv(out + "ALLT.csv")