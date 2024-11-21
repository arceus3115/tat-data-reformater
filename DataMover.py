import os
import pandas as pd
    
def split_and_save_scripts(df):
    # Identify the index where Script_1 ends and Script_2 starts (the row containing 'Mode')
    script_1_end = df[df['Script_1'] == 'Mode'].index[0] + 1  # The row with 'Mode' marks the end of Script_1
    script_2_start = script_1_end + 1  # Script_2 starts after 'Mode'

    # Create DataFrames for Script_1 and Script_2
    script_1_df = df.iloc[:script_1_end].reset_index(drop=True)  # Data for Script_1
    script_2_df = df.iloc[script_2_start:].reset_index(drop=True)  # Data for Script_2

    # Ensure the output folder exists, create it if it doesn't

    # Return DataFrames for debugging
    return (script_1_df, script_2_df)

def atomic_row_wrangler(data_frames, filename, output_folder='Organized_Data'):
    os.makedirs(output_folder, exist_ok=True)
    
    script_names = ["Script_1", "Script_2"]
    
    # Initialize an empty dictionary to hold the dictionaries for each rater
    rater_results = {
        'Rater_1': {},
        'Rater_2': {},
        'Rater_3': {}
    }
    
    # Process each DataFrame in the provided list
    for script_num, df in enumerate(data_frames):   
        # Process each row in the DataFrame
        for row in range(len(df)):
            card = df.iloc[row, 0]  # The first column (Card number)

            # Process the remaining columns
            for col, value in df.iloc[row, 1:].items():  # Skip the first column
                # Get the rater from the first two characters of the column name
                rater = col[:2]
                # Extract the dimension by removing the rater prefix
                dimension = col[2:]

                # Adjust the label format based on whether the card is "Mode"
                if card == "Mode":
                    label = f"{filename}_{dimension}_{script_names[script_num][-1]}_{card}"
                else:
                    label = f"{filename}_{dimension}_Card{card}_{script_names[script_num][-1]}"
                
                # Append the value to the appropriate rater's dictionary
                if rater == "R1":
                    rater_results['Rater_1'][label] = value
                elif rater == "R2":
                    rater_results['Rater_2'][label] = value
                elif rater == "R3":
                    rater_results['Rater_3'][label] = value
    
    # Convert the dictionary of rater results into a DataFrame
    result_df = pd.DataFrame(rater_results)
    
    # Save the DataFrame to a CSV file
    result_df.to_csv(os.path.join(output_folder, f'output_{filename}.csv'))
    
    return result_df
