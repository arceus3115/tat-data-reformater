import os
import pandas as pd
import DataMover  # Import the DataMover class

# Path to the folder containing the CSV files
data_folder = 'Data'

# Iterate through all CSV files in the folder
for file in os.listdir(data_folder):
    if file.endswith('.csv'):  # Process only CSV files
        file_path = os.path.join(data_folder, file)

        # Extract the filename without the extension
        filename = os.path.splitext(file)[0]

        # Read the data from the CSV file
        df = pd.read_csv(file_path)

        # Use the DataMover class to split and save the scripts
        data_frames = DataMover.split_and_save_scripts(df)

        # Process the split scripts and organize data
        output_df = DataMover.atomic_row_wrangler(data_frames, output_folder='Organized_Data', filename=filename)

        print(f"Processed {file} successfully. Output saved in 'Organized_Data'.")
