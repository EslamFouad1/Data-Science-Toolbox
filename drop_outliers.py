quartile1 = bankruptcy_subdf2.quantile(q=0.25,axis=0)
# display(quartile1)
quartile3 = bankruptcy_subdf2.quantile(q=0.75,axis=0)
# display(quartile3)
IQR = quartile3 -quartile1
lower_limit = quartile1-1.5*IQR
upper_limit = quartile3+1.5*IQR

lower_limit = lower_limit.drop(["bankrupt_"])
upper_limit = upper_limit.drop(["bankrupt_"])
# print(lower_limit)
# print(" ")
# print(upper_limit)

bankruptcy_subdf2_out = bankruptcy_subdf2[((bankruptcy_subdf2<lower_limit) | (bankruptcy_subdf2>upper_limit)).any(axis=1)]
display(bankruptcy_subdf2_out.shape)
display(bankruptcy_subdf2.shape)

bankruptcy_subdf3 = bankruptcy_subdf2_out.copy()
bankruptcy_subdf3


# Another way
def remove_outliers(data,outlier_cols,k=1.5):
  df = data.copy()
  for col in outlier_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1 # inter quartile range
    # ~ is used to inversing boolean (bitwise not)
    df = df.loc[~((df[col] < (q1 - (k * iqr))) | (df[col] > (q3 + (k * iqr))))]
  return df

has_outliers = ["depth","x","y","z"]
diamonds_cleaned = remove_outliers(diamonds,has_outliers)
diamonds_cleaned.head()
