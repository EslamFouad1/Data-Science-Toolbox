# target variable (binary: diagnosis) distribution
print(df.diagnosis.value_counts())
sns.countplot(x = df.diagnosis);
plt.title("Target Distribution")
plt.show()
