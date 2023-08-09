df['lightduty'] = df['lightduty'].apply(lambda x: 0 if x=='No' else 1)

#Convert the relevant variables to a Boolean type.
df_1 = df.copy()   #Work with a new object.
df_1.default.map(dict(yes = 1, no = 0)).astype(bool)
df_1.default.value_counts()

# Do the same thing for other Boolean variables.
bool_vars = ["housing", "loan", "term_deposit"]

for var in bool_vars:
    df_1[var] = df_1[var].map(dict(yes = 1, no = 0)).astype(bool)
    
    print(f"Converted {var} to Boolean.")


# Another way
data['Consumer disputed?'] = np.where(data['Consumer disputed?']== 'Yes', 1, 0)
data['Consumer disputed?'].value_counts()
