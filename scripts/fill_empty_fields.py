import pandas as pd

def fill_empty_fields(input_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Replace empty strings, NaN, and whitespace-only strings with "None"
    for column in df.columns:
        # Convert to string first to handle any numeric NaN
        df[column] = df[column].astype(str)
        # Replace empty or whitespace-only strings with "None"
        df[column] = df[column].apply(lambda x: "None" if x.strip() == "" or x.lower() == "nan" else x)
    
    # Save changes back to the input file
    df.to_csv(input_file, index=False)
    print(f"Changes saved to: {input_file}")

if __name__ == "__main__":
    input_file = "removed_duplicates.csv"  # Update this to your input file name
    fill_empty_fields(input_file)
