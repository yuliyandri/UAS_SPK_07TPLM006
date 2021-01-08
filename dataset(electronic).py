# Ubah nama kolomnya agar lebih mudah 
rating.rename(columns={"reviews.rating":"reviewsRating"},inplace=True)

# Jadikan sebagai variabel dan lakukan perhitungan sejumlah nilai yang ada di kolom reviewRating 
rev_rating = rating['reviewsRating'].value_counts()
rev_rating

# Visualisasikan dari hasil perhitungan nilai
dims = (10, 8)
fig, ax = plt.subplots(figsize=dims)
ax = sns.countplot(x="reviewsRating", data=rating)