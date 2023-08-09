# Features (training_df[col]) and target (class)

plt.figure(figsize = (20, 15))
for i in range(8):
    plt.subplot(4,2,i+1)
    tr_d = training_df
    col = tr_d.iloc[:,i]
    sns.barplot(data=training_df, x='Class', y=col)
plt.show()
