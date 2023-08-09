scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
tsne = TSNE(n_components=3, verbose=1, random_state=123)
z = tsne.fit_transform(X_scaled)
df_tsne = pd.DataFrame(z)
df_tsne.columns=['tsne1','tsne2','tsne3']
df_tsne['diagnosis'] = df['diagnosis'].values
plt.figure()
sns.scatterplot(data=df_tsne, x="tsne1", y="tsne2", hue="diagnosis")
plt.show()
plt.close('all')
