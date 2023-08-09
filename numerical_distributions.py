plt.figure(figsize = (16, 22))
plotnumber = 1

for column in df.loc[:, df.columns != 'diagnosis']:
    if plotnumber <= 30:
        ax = plt.subplot(10, 3, plotnumber)
        sns.distplot(df[column])
        plt.xlabel(column)

    plotnumber += 1

plt.tight_layout()
plt.show()

#Bivariate Distribution
fig = px.violin(df, y="radius_mean", x="diagnosis", box=True, points="all",title="Violin Plot of Radius mean by Diagnosis")

fig.update_layout(
    title_text="Distribution of Radius Mean by Diagnosis",
    xaxis_title_text="Radius Mean",
    yaxis_title_text="Frequency",
    legend_title_text="Diagnosis"
)
fig.show()
