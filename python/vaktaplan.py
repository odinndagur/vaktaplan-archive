import camelot
import numpy as np
file = "../input/11okt10nov.pdf"

# tables = camelot.read_pdf(file)
tables = camelot.read_pdf(file,pages='1-end')
# tableDf = [] 
# for i in range(tables.n):
#     tableDf[i] = tables[i].df
# # df = tables[0].df
docs = []
out = "../output/"
for i in range(0,tables.n, 2):
    df = tables[i].df #even
    df2 = tables[i+1].df #odd
    # print(headers)
    df2 = df2.iloc[:,1:]
    headers = df2.iloc[0]
    # headers.to_csv(out + "headers" + str(i+1) + ".csv")
    # keys = df2.iloc[:,0]


    df = df.iloc[2: , 1:]
    df2 = df2.iloc[1: , :]

    df.index = df.index - 1

    df.columns = headers
    df2.columns = headers

    df.dropna(how='all',axis=1)
    df2.dropna(how='all',axis=1)

    # df.index = keys
    # df2.index = keys

    total = df.append(df2, ignore_index = True)
    total.to_csv(out + "vaktaplan" + str(int(i/2)) + ".csv")
    docs.append(total)

# print("docs: ")
# for i in range(len(docs)):
    # print(docs[i])
# print(total)
first = docs[0]
first.merge(docs[1],how='left')
# for i in range(len(docs)):
    # if(i != 0):
        # temp = docs[i].iloc[:,1:]
        # first.merge(temp)

df = docs[len(docs)-1]
# print("empty?")
# empty = [col for col in df.columns if not df[col].empty]
# print(empty)
# df.drop(empty,axis=1,inplace=True)
print(df)

first.to_csv(out + "ALLT.csv")


    # print("df columns: " + str(len(df.columns)))
    # print("df2 columns: " + str(len(df2.columns)))
    # print("headers: " + str(len(headers)))
    # headers.to_csv(str(i+1) + "headers.csv")

    # df.columns = headers
    # df2.columns = headers

    # df.drop(df.columns[[0]], axis=1)
    # df = df.iloc[1: ,1:]
    # if(i % 2 == 0): # even
    #     print("lol")
    #     # df = df.iloc[1: ,:]
    #     # df.columns = tables[i-1].df.iloc[0]
    # if(i % 2 != 0): # odd
    #     df = df.iloc[1: ,3:]
        # df.columns = df.iloc[0]

    # df.columns = df.iloc[0]
    # df = df.iloc[1: ,1:]
    # df.to_csv(str(i) + ".csv")
    # df2.to_csv(str(i+1) + ".csv")

# print(len(tables[0].df.columns))
# print(len(tables[1].df.columns))
 


# for row in tables[0].cells:
#     for cell in row:
#         print(cell.x1,cell.y1,cell.x2,cell.y2)




# print(tableDf[1])
    # df = tables[1].df
    # df = df.drop(df.columns[[0]], axis=1)  # df.columns is zero-based pd.Index

    # print(df)
# print(type(tables))
# files = []
# for i in range(tables.n):
#     name = 'vaktaplan_' + str(i) + '.csv'
#     files.append(name)
#     tables[i].to_csv(name)


# tableArray = []

# for i in range(1):
#     print(i)
#     with open(files[i]) as file_name:
#         tableArray[i] = np.loadtxt(file_name,delimiter=",")
#     print(tableArray[i])


# tables.export("l.csv", f="csv")