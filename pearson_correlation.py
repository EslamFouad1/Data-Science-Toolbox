### Columns with Linear relationship with Target variable
company_corr = pd.DataFrame(company_df.corr(numeric_only=True))
company_corr = pd.DataFrame(company_corr['Bankrupt?'])

# Remove specific indices, all 3 are categorical
indices_to_remove = ['Liability-Assets Flag', 'Net Income Flag','Bankrupt?']
company_corr = company_corr.drop(indices_to_remove)

plt.figure(figsize=(8, 17))
sns.barplot(y=company_corr.index,x=company_corr['Bankrupt?'])
plt.title("Pearson correllation with Bankruptcy")
plt.show()

# Lets see what features has weak correlation to strong correlation (>|0.10|)
temp_corr = company_corr
temp_corr[['Bankrupt?']] = abs(temp_corr[['Bankrupt?']])
print("\nColumns with correlation (>|0.10|) :\n")
for i in temp_corr[(temp_corr["Bankrupt?"] > 0.10)].index:
    print("* "+i+"\t")

# Select above mentioned features to find correlation between each other
correlated_features = list(temp_corr[(temp_corr["Bankrupt?"] > 0.10)].index)+["Bankrupt?"]
corr_test = company_df[correlated_features]

plt.figure(figsize=(15, 15))
corr = corr_test.corr()

sns.heatmap(corr,cmap="crest",annot=True, fmt=".1f")
plt.title("Correlation with Bankruptcy (|>0.10|)")
plt.show()

#Observations :
#* Lets remove columns with correlation with other columns = 1.0, which means both the columns convey same information

# Columns selected based on Linear relationship
selected_columns_set_linear = [
 'ROA(A) before interest and % after tax',
 'Net Value Per Share (A)',
 'Debt ratio %',
 'Working Capital to Total Assets',
 'Current Liability to Current Assets',
 "Net Income to Stockholder's Equity",
 'Operating Gross Margin',
 'Bankrupt?']

plt.figure(figsize=(10, 10))
sns.heatmap(company_df[selected_columns_set_linear].corr(),cmap="crest",annot=True, fmt=".2f")
plt.title("Correlation between selected columns")
plt.show()
