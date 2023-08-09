variance_thresh = 0.9
features = ['texture_mean', 'smoothness_mean', 'compactness_mean',
       'concavity_mean', 'concave points_mean', 'symmetry_mean',
       'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se',
       'area_se', 'smoothness_se', 'compactness_se', 'concavity_se',
       'concave points_se', 'symmetry_se', 'fractal_dimension_se',
       'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']
X = df[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=X_scaled.shape[1])
pca.fit(X_scaled)
ratios = pca.explained_variance_ratio_
for i in range(np.cumsum(ratios).shape[0]):
    num_pca = i + 1
    print(f"Variance explained by component {num_pca}: {ratios[i]*100}")
    if np.cumsum(ratios)[i] >= variance_thresh:
        txt = f"{num_pca} number of principle components explains {variance_thresh*100} % of the data's variance"
        break
    else:
        continue
x = np.arange(X_scaled.shape[1])
plt.plot(x, np.cumsum(ratios))
plt.xlabel("Number of PCA's")
plt.ylabel("Cumulated Sum of Explained Variance")
plt.title("Variance of data Explained by PCA's",fontsize=20)
plt.figtext(0.5, -0.1, txt, wrap=True, horizontalalignment='center', fontsize=12)
plt.show()

# Visualizing the dataset using PCA
#We will apply threshold on the number of components to visualise the data.
pca = PCA(n_components=3) #We can also just use 2 components, incase there is no plan for 3-D plots
pca_data = pca.fit_transform(X_scaled)
df_pc = pd.DataFrame(pca_data)
df_pc['diagnosis'] = df.diagnosis.values
df_pc.columns = ['pc1','pc2','pc3','diagnosis']
plt.figure()
sns.scatterplot(data=df_pc, x="pc1", y="pc2", hue="diagnosis")
plt.show()
plt.close('all')
