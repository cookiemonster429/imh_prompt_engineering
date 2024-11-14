import os
import pandas as pd
import json

# Define the folder path containing the JSON files
folder_path = '/Users/jovanwong/Pictures/Desktop/IMH/New Prompt Engineering/Categorised forms'

# Initialize an empty list to store data
all_data = []

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as f:
            # Load the JSON data
            json_data = json.load(f)
            # Append the JSON data (as a dictionary) to the list
            all_data.append(json_data)

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(all_data)

# Save the DataFrame as a CSV file
output_csv_path = '/Users/jovanwong/Pictures/Desktop/IMH/New Prompt Engineering/combined_output.csv'
df.to_csv(output_csv_path, index=False)

print(f"CSV file created at {output_csv_path}")
