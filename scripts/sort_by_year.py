import pandas as pd

def sort_dataset_by_year(file_path: str, year_column: str) -> None:
    """
    Sort a dataset by year in ascending order (oldest to newest) and save back to the same file.
    
    Args:
        file_path (str): Path to the CSV file
        year_column (str): Name of the column containing year data
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Sort the dataframe by year (ascending=True means oldest first)
        df_sorted = df.sort_values(by=year_column, ascending=True)
        
        # Save the sorted dataframe back to the same file
        df_sorted.to_csv(file_path, index=False)
        
        print(f"Successfully sorted dataset and saved back to {file_path}")
        print(f"Year range: {df_sorted[year_column].min()} - {df_sorted[year_column].max()}")
        
    except FileNotFoundError:
        print(f"Error: Could not find the file {file_path}")
    except KeyError:
        print(f"Error: Column '{year_column}' not found in the dataset")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    file_path = "cleaned_vehicles3.csv"
    year_column = "year"
    
    sort_dataset_by_year(file_path, year_column) 