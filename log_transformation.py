# Log transform to remove skews

target = bankruptcy_subdf3['bankrupt_']
bankruptcy_subdf4 = bankruptcy_subdf3.drop(["bankrupt_"],axis=1)

def log_trans(data):
    for col in data:
        skew = data[col].skew()
        if skew>=0.5 or skew<=0.5:
            data[col] = np.log1p(data[col])
        else:
            continue
    return data

bankruptcy_subdf4_log = log_trans(bankruptcy_subdf4)
bankruptcy_subdf4_log.head()

# Box Plot of Log Transformed Data
plt.figure(figsize=(30,20))
boxplot=sns.boxplot(data=bankruptcy_subdf4_log,orient="h")
boxplot.set(xscale="log")
plt.show()

# Distribution of Log Data Visualise
# Visualisation of distributions after sub-sampling after outlier removal and log transform
compare_subdf2 = bankruptcy_subdf2.drop(["bankrupt_"],axis=1)

cols = list(bankruptcy_subdf4.columns)
ncols = 8
nrows = math.ceil(len(cols) / ncols)

fig, ax = plt.subplots(nrows, ncols, figsize = (4.5 * ncols, 4 * nrows))
for i in range(len(cols)):
    sns.kdeplot(bankruptcy_subdf4_log[cols[i]], ax = ax[i // ncols, i % ncols],fill=True,color="red")
    sns.kdeplot(bankruptcy_subdf2[cols[i]], ax = ax[i // ncols, i % ncols],color="green")
    if i % ncols != 0:
        ax[i // ncols, i % ncols].set_ylabel(" ")
plt.tight_layout()
plt.show()
print("Red represents distributions after log transforms, green represents before log transform")
