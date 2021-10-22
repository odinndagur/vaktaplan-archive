import pandas as pd
file = '/Users/odinndagur/Code/Github/vaktaplan/drasl/ALLT.csv'

plan = pd.read_csv(file)
# print(plan)
df = plan.dropna(axis='columns', how='all')

# print(df)
days = []

# for col in df.columns[1:]:
#     day = df[col].name
#     print(df[col])
#     for cell in df[col]:
#             print(cell)

for ind, column in enumerate(df.columns):
    day = column
    cell = str(df[column][ind])
    if cell[0].isdigit():
        # print(df[column][ind])
        lol = []
        lol = cell.split('\n')
        # print(cell)
        shift = {'time' : lol[0], 'type' : lol[1]}
        print(shift)
    # print(ind, column)
