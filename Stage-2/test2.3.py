import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = 'https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt'
df = pd.read_csv(data, sep='\t')

# Select only numeric columns for subtraction
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
# print(numeric_columns)

# Initialize an empty DataFrame for storing results
WT_MT_df = pd.DataFrame()

# Wild-type metabolic response (subtract row 3 from row 0 for all numeric columns)
WT_MT_df["ΔM_Value_WT"] = df.loc[0, numeric_columns] - df.loc[3, numeric_columns] 

# Mutants metabolic response (subtract row 6 from row 4 for all numeric columns)
WT_MT_df["ΔM_Value_MT"] = df.loc[4, numeric_columns] - df.loc[6, numeric_columns]

# Adding the metabolites as a new column for plotting
WT_MT_df['Metabolites'] = numeric_columns


# Plotting the data
sns.scatterplot(data=WT_MT_df, x="ΔM_Value_MT", y="ΔM_Value_WT", hue="Metabolites")

# Add reference line:
values_y = []
values_x = []
def line_function():
    for i in range(-3,3):
        y = i
        values_x.append(i)
        values_y.append(y)
line_function()
plt.plot(values_x, values_y)

# Set plot title and labels
plt.title('Wild-type and Mutant Metabolic Responses')
plt.xlabel('ΔM Value MT')
plt.ylabel('ΔM Value WT')
plt.show()
