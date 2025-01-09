# Check if 'photo_urls' is a string or list, and count the number of photos
# Assuming photo_urls is a string with URLs separated by commas
final_df['photo_count'] = final_df['photo_urls'].apply(lambda x: len(x.split(',')) if pd.notnull(x) else 0)

# Alternatively, if 'photo_urls' is a list, you could count its length directly
# final_df['photo_count'] = final_df['photo_urls'].apply(lambda x: len(x) if isinstance(x, list) else 0)

# Check the new feature
print(final_df[['photo_urls', 'photo_count']].head())
# Load the property_interactions dataset
property_interactions = pd.read_csv('property_interactions.csv')

# Assuming the columns in property_interactions are 'property_id' and 'interaction_count'
# Aggregate the interactions per property by summing up the interaction counts
total_interactions = property_interactions.groupby('property_id')['interaction_count'].sum().reset_index()

# Merge the total_interactions with the main DataFrame (final_df)
final_df = pd.merge(final_df, total_interactions, how='left', left_on='property_id', right_on='property_id')

# If a property has no interactions, set total_interactions to 0
final_df['interaction_count'].fillna(0, inplace=True)

# Check the final DataFrame with the total_interactions
print(final_df[['property_id', 'interaction_count']].head())

# Preview the first few rows to ensure everything looks correct
print(final_df[['property_id', 'photo_count', 'interaction_count']].head())

# Save the updated DataFrame
final_df.to_csv('final_with_features.csv', index=False)

