import pandas as pd

# Read the CSV file
df = pd.read_csv('cleaned_vehicles3.csv')

# Find duplicates based on all columns except any potential index columns
duplicates = df[df.duplicated(keep=False)]

# Sort duplicates by relevant columns to make it easier to see the groups
duplicates_sorted = duplicates.sort_values(['year', 'make', 'model', 'VClass', 'baseModel'])

# Display duplicate count
print(f"\nTotal number of duplicate rows: {len(duplicates)}")

# Save duplicates to a separate CSV file for review
if not duplicates.empty:
    duplicates_sorted.to_csv('duplicate_entries.csv', index=False)
    print(f"Duplicate entries have been saved to 'duplicate_entries.csv'")
    
    # Remove duplicates keeping first occurrence and save to new file
    df_no_duplicates = df.drop_duplicates()
    df_no_duplicates.to_csv('removed_duplicates.csv', index=False)
    print(f"Dataset with duplicates removed saved to 'removed_duplicates.csv'")
    
    # Display a summary of duplicates
    print("\nSummary of duplicate entries:")
    for _, group in duplicates_sorted.groupby(['year', 'make', 'model', 'VClass', 'baseModel']):
        if len(group) > 1:
            print(f"\nFound {len(group)} duplicates for:")
            print(f"Year: {group['year'].iloc[0]}")
            print(f"Make: {group['make'].iloc[0]}")
            print(f"Model: {group['model'].iloc[0]}")
            print(f"VClass: {group['VClass'].iloc[0]}")
            print(f"Base Model: {group['baseModel'].iloc[0]}")
            if pd.notna(group['atvType'].iloc[0]):
                print(f"ATV Type: {group['atvType'].iloc[0]}")
            print(f"Cylinders: {group['cylinders'].iloc[0]}")

else:
    print("No duplicates found in the dataset!")