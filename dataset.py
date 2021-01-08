primary_cat = rating['primaryCategories'].value_counts()
primary_cat

# Visualisasikan kolom primaryCategories
dims = (10, 8)
fig, ax = plt.subplots(figsize=dims)
ax = sns.countplot(x=rating.primaryCategories)