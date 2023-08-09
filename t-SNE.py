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

import plotly.express as px
fig = px.scatter(df_tsne, x="tsne1", y="tsne2", color="diagnosis"
                 #size='petal_length', hover_data=['petal_width']
                )
fig.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for diagnosis in df_tsne.diagnosis.unique():
    ax.scatter(df_tsne.tsne1[df_tsne.diagnosis==diagnosis],df_tsne.tsne2[df_tsne.diagnosis==diagnosis],df_tsne.tsne3[df_tsne.diagnosis==diagnosis],label=diagnosis)
ax.set_xlabel('tsne1')
ax.set_ylabel('tsne2')
ax.set_zlabel('tsne3')
ax.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()
plt.close('all')
