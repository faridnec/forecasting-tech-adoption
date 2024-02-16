import pandas as pd

excel_file = 'D:/Liftup/github/data/raw/data.xlsx'
sheets = ['AI', 'Aviation', 'Space', 'Laser', 'Composite']
dfs = []

for sheet in sheets:
    df = pd.read_excel(excel_file, sheet_name=sheet)
    dfs.append(df)

integrated_df = pd.concat(dfs, ignore_index=True)

# Write integrated DataFrame to a new Excel sheet
with pd.ExcelWriter(excel_file, mode='a', engine='openpyxl') as writer:
    integrated_df.to_excel(writer, sheet_name='INTEGRATED_DB', index=False)

# import sys
# print(sys.path)

