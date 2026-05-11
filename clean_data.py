import pandas as pd
import json

# Read CSV file
csv_df = pd.read_csv("data/input.csv")

# Read JSON file
with open("data/input.json", "r") as file:
    json_data = json.load(file)

json_df = pd.DataFrame(json_data)

# Combine data
combined_df = pd.concat([csv_df, json_df], ignore_index=True)

# Remove missing rows
cleaned_df = combined_df.dropna()

# Export cleaned data
cleaned_df.to_csv("data/cleaned_output.csv", index=False)

print("Data cleaned successfully!")