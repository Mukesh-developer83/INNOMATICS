# Handle missing values
df['photo_urls'] = df['photo_urls'].fillna('')

# If 'photo_urls' is a string, split by commas to count the number of photos
df['num_photos'] = df['photo_urls'].apply(lambda x: len(x.split(',')) if x else 0)

# If 'photo_urls' is a list, count the length of the list
# df['num_photos'] = df['photo_urls'].apply(lambda x: len(x) if isinstance(x, list) else 0)

# Optionally, you can inspect the first few rows to verify
print(df[['photo_urls', 'num_photos']].head())
