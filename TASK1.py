import pandas as pd
import os

# Specify the directory where CSV files are stored
directory = 'property_interactions.csv'

# List to hold DataFrames
data_frames = []

# Loop through all files in the specified directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Create the full file path
        file_path = os.path.join(directory, filename)
        
        # Read each CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Append the DataFrame to the list
        data_frames.append(df)

# Concatenate all DataFrames into one final DataFrame
final_df = pd.concat(data_frames, ignore_index=True)
# Check for missing data across all columns
missing_data = final_df.isnull().sum()

# Display columns with missing data
print(missing_data[missing_data > 0])

# Fill missing values with a placeholder or mean/median (if applicable)
final_df.fillna('Unknown', inplace=True)

# Or, drop rows with missing critical data
final_df.dropna(subset=['column_name'], inplace=True)

# Standardize column names (remove spaces, convert to lowercase)
final_df.columns = final_df.columns.str.strip().str.lower().str.replace(' ', '_')

# Check if columns are consistent
print(final_df.columns)
# Check the data types of each column
print(final_df.dtypes)

# Convert columns to the correct data type if necessary
final_df['price'] = pd.to_numeric(final_df['price'], errors='coerce')  # Example for price column

# Convert date columns to datetime if applicable
final_df['date'] = pd.to_datetime(final_df['date'], errors='coerce')

final_df['price'] = final_df['price'].replace({'\$': '', ',': ''}, regex=True)
final_df['price'] = pd.to_numeric(final_df['price'], errors='coerce')
# Drop duplicate rows based on all columns (or a subset of columns if necessary)
final_df.drop_duplicates(inplace=True)

# Check the first few rows of the final DataFrame
print(final_df.head())

# Save the merged DataFrame to a new CSV file
final_df.to_csv('merged_property_data.csv', index=False)


