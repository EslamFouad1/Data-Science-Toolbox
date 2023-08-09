# Features (training_df[col]) and target (class)

plt.figure(figsize = (20, 15))
for i in range(8):
    plt.subplot(4,2,i+1)
    tr_d = training_df
    col = tr_d.iloc[:,i]
    sns.barplot(data=training_df, x='Class', y=col)
plt.show()

# Distribution Plot and Checking The Distribution for Normality
plt.figure(figsize = (20, 13))
plt.subplot(2,2,1)
sns.histplot(data=training_df, x=training_df.loc[training_df['Class']==1,'Mean_Integrated'], kde=True)
plt.title('Class 1')
plt.subplot(2,2,2)
st.probplot(training_df.loc[training_df['Class']==1, 'Mean_Integrated'], plot=plt)
plt.title('Class 1')
plt.subplot(2,2,3)
sns.histplot(data=training_df, x=training_df.loc[training_df['Class']==0,'Mean_Integrated'], kde=True)
plt.title('Class 0')
plt.subplot(2,2,4)
st.probplot(training_df.loc[training_df['Class']==0,'Mean_Integrated'], plot=plt)
plt.title('Class 0')
plt.suptitle('Distribution Plot and Checking the Distribution for Normality \n 
 
 
')
plt.tight_layout()
plt.show()
