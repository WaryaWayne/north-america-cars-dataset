import pandas as pd

def remove_old_years(file_path: str, min_year: int = 2000) -> None:
    """
    Remove all entries before a specified year from the dataset and save the filtered data.
    
    Args:
        file_path (str): Path to the CSV file
        min_year (int): Minimum year to keep (default: 2000)
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Get the original row count
        original_count = len(df)
        
        # Filter out years before min_year
        df_filtered = df[df['year'] >= min_year]
        
        # Calculate removed rows
        removed_count = original_count - len(df_filtered)
        
        # Save the filtered dataset
        output_file = 'filtered_vehicles_2000_plus.csv'
        df_filtered.to_csv(output_file, index=False)
        
        print(f"Successfully filtered dataset:")
        print(f"- Original entries: {original_count}")
        print(f"- Entries removed: {removed_count}")
        print(f"- Remaining entries: {len(df_filtered)}")
        print(f"- Year range: {df_filtered['year'].min()} - {df_filtered['year'].max()}")
        print(f"Filtered dataset saved to: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Could not find the file {file_path}")
    except KeyError:
        print(f"Error: Column 'year' not found in the dataset")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "north_america_cars_1984_2025.csv"
    remove_old_years(input_file)

