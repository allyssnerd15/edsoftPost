import pandas as pd


df = pd.read_csv("arquivos\\arquivo_exemplo.csv", sep=",", encoding="latin1").head()

df.DataFrame()
import pdb; pdb.set_trace()
print(df.head())