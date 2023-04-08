import os
import glob
import pandas as pd
# Set the directory path
dir_path = r"C:\Users\nonAdmin\Documents\Classes\Cs\598(new)\seperate python scripts_Coloab doesn't like_\combine\products"

# Get a list of all CSV files in the directory
print('start')
csv_files = [os.path.join(dir_path, file) for file in os.listdir(dir_path) if file.endswith('.csv')]

# Initialize an empty list to store the DataFrames
dfs = []

# Loop through the CSV files and read them into DataFrames
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)
    print(file)

# Concatenate the DataFrames into a single DataFrame
combined_df = pd.concat(dfs)
combined_df.to_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/CombinedProducts1.csv")
print('done')
# Print the combined DataFrame
print(combined_df)
