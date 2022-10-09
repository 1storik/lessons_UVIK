import pandas as pd

df = pd.read_csv('C:\\Users\\prova\\PycharmProjects\\pre-interview-master\\task_1\\data.csv')
print(df['person'].tolist())
print(df['country'].unique().tolist())
for s in range(len(df['person'].tolist())):
    df['person'].loc[s] = df['person'].loc[s] + ' '
counrty = df.groupby(['country']).sum()
group_by_count1 = df.groupby(['country']).count()
group_by_count1.rename(columns={'person': 'count'}, inplace=True)

print(pd.merge(counrty, group_by_count1, how='inner', on='country'))











