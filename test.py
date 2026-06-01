import pandas as pd

df = pd.read_excel(
    r"C:\Users\LENOVO\excel_automate\TSECL_1001101_F004_202506.xlsx",
    engine="openpyxl"
)

print(df.head())
print(df.shape)