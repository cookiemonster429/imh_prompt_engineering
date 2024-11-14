import json
import pandas as pd

def json_to_csv(json_file_path, csv_output_path):
    # Open and load the JSON data
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Convert the JSON data to a pandas DataFrame
    df = pd.DataFrame([json_data])  # Wrap the json_data in a list to ensure it's treated as a row

    # Save the DataFrame as a CSV file
    df.to_csv(csv_output_path, index=False)

# Example usage
json_file_path = '/Users/jovanwong/Pictures/Desktop/IMH/New Prompt Engineering/Categorised forms/Simulated_form17.json'
csv_output_path = '/Users/jovanwong/Pictures/Desktop/IMH/New Prompt Engineering/Simulated_form17_uncategorised.csv'
json_to_csv(json_file_path, csv_output_path)
