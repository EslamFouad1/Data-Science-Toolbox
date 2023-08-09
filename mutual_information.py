independent_variable = company_df.drop(['Bankrupt?'], axis=1)
target_variable = company_df[['Bankrupt?']]

importances = mutual_info_classif(independent_variable,pd.Series.ravel(target_variable))
importances = pd.Series(importances,independent_variable.columns[0:len(independent_variable.columns)])
importances = pd.DataFrame({'features':importances.index, 'importance':importances.values})

# Mutual information
plt.figure(figsize=(10, 17))
sns.barplot(data = importances,y = "features", x = "importance",order=importances.sort_values('importance').features)
plt.xlabel("Mutual Importance")
plt.title("Mutual Importance of Columns")
plt.show()

# Lets select top 10 columns for EDA and Modelling
selected_columns_set_non_linear = np.array(importances.nlargest(5,'importance').features)

selected_columns = [*selected_columns_set_linear , *selected_columns_set_non_linear]
selected_columns = np.unique(selected_columns)
