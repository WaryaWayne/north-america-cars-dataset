import pandas as pd

df = pd.read_csv('removed_duplicates.csv')
vclass_counts = df['VClass'].value_counts()
print("Counts of each value in VClass field:")
print(vclass_counts)
