import pandas as pd

f1 = pd.read_csv('fixtures/pana.csv')
f2 = pd.read_csv('fixtures/panb.csv')

print(f2[~f2.column1.isin(f1.column1)])
