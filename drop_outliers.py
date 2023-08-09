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
