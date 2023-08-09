def target_mean(data,feature,target,decimal=2):
    sns.countplot(data=data, y=feature, order = data[feature].value_counts().head(10).index,)
    return(data.groupby(feature).agg({target: "mean"}).sort_values(by=[target],ascending=[False]).round(decimal))

print(target_mean(data,'Company response to consumer','Consumer disputed?'))
