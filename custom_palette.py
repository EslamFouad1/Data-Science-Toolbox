# Custom Palette for Visualization
sns.set_style("white")
sns.set(rc={"axes.facecolor":"#f2d4b1","figure.facecolor":"#f2d4b1","grid.color":"white"})
sns.set_context("poster",font_scale = .7)

palette = ["#c94727","#ea5b17","#e57716","#f2a324","#a2c0a6","#7ac0a8","#5e9786","#557260"]

# sns.palplot(sns.color_palette(palette))
# plt.show()

# Example1
print("Let's have a look on the Classes :")
plt.subplots(figsize=(20, 8))
p=sns.countplot(y=df_qual["Class"],order=df_qual["Class"].value_counts().index,palette=["#3f4f45","#5e9880"], saturation=1, edgecolor = "#1c1c1c", linewidth = 5)
# p.axes.set_yscale("symlog")
p.axes.set_title("\nClasses\n",fontsize=25)
p.axes.set_ylabel("Class",fontsize=20)
p.axes.set_xlabel("\nTotal",fontsize=20)
p.axes.set_yticklabels(p.get_yticklabels(),rotation = 0)
for container in p.containers:
    p.bar_label(container,label_type="center",padding=6,size=25,color="black",rotation=0,
    bbox={"boxstyle": "round", "pad": 0.4, "facecolor": "#e0b583", "edgecolor": "#1c1c1c", "linewidth" : 4, "alpha": 1})


sns.despine(left=True, bottom=True)
plt.show()

# Example2
print(f"Let's have a look on the distribution of Mean Integrated :")
plt.subplots(figsize=(20, 8))
p = sns.histplot(df_quant["Mean_Integrated"],color=palette[6],kde=True,bins=30,alpha=1,fill=True,edgecolor="black",linewidth=3)
p.axes.lines[0].set_color("orange")
p.axes.set_title("\nMean Integrated Distribution\n",fontsize=25)
plt.ylabel("Count",fontsize=20)
plt.xlabel("Mean Integrated",fontsize=20)
plt.yscale("linear")
sns.despine(left=True, bottom=True)

plt.show()
