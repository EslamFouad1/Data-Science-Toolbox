df['lightduty'] = df['lightduty'].apply(lambda x: 0 if x=='No' else 1)

#Convert the relevant variables to a Boolean type.
df_1 = df.copy()   #Work with a new object.
df_1.default.map(dict(yes = 1, no = 0)).astype(bool)
df_1.default.value_counts()
