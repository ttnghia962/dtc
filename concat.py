import pandas as pd
import glob

# Get the list of Excel file paths
file_paths = glob.glob(r"C:\Users\nghia.truong_innova\OneDrive - Equus Products\Data Engineer\Anh Tien\dtc\Data\*.xlsx")  # Adjust the path


# Load and concatenate all the Excel files
df_list = [pd.read_excel(file, header=None) for file in file_paths]
final_df = pd.concat(df_list, ignore_index=True)
final_df.columns = ['DTC']

final_df.to_excel(r'C:\Users\nghia.truong_innova\OneDrive - Equus Products\Data Engineer\Anh Tien\dtc\Data\Final_total_DTC.xlsx', index= False)

# Now, final_df contains all the data from the Excel files stacked vertically
