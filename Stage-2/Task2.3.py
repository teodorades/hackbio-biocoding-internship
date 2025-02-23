# Task Code 2.3: Botany and Plant Science 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = 'https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt'
df = pd.read_csv(data, sep='\t')

# Select only numeric columns for subtraction
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
# print(numeric_columns) # --> check

# Initialize an empty DataFrame for storing results
WT_MT_df = pd.DataFrame()

# Wild-type metabolic response (subtract row 3 from row 0 for all numeric columns)
WT_MT_df["ΔM_Value_WT"] = df.loc[0, numeric_columns] - df.loc[3, numeric_columns] 

# Mutants metabolic response (subtract row 6 from row 4 for all numeric columns)
WT_MT_df["ΔM_Value_MT"] = df.loc[4, numeric_columns] - df.loc[6, numeric_columns]

# Calculate the distance of each metabolite from y=x:
WT_MT_df["Distance"] = np.abs(WT_MT_df["ΔM_Value_MT"] - WT_MT_df["ΔM_Value_WT"]) / np.sqrt(2)
print(WT_MT_df['Distance'])

# Defined residual cutoff:
residual_cutoff = []
for i in WT_MT_df["Distance"]:
    if - 0.3 <= i <= 0.3:
        residual = 'inside'
    else:
        residual = 'outside'
    residual_cutoff.append(residual)

WT_MT_df["Residual_cutoff"] = residual_cutoff
print(f"This are metabolites outisde the residual cut-off:\n{WT_MT_df[WT_MT_df["Residual_cutoff"] == 'outside'].index}")
print(f"This are metabolites inside the residual cut-off:\n{WT_MT_df[WT_MT_df["Residual_cutoff"] == 'inside'].index}")

# Needs two graphs:
fig, ax = plt.subplots()

# Plotting the data
sns.scatterplot(data=WT_MT_df, x="ΔM_Value_MT", y="ΔM_Value_WT", hue="Residual_cutoff", palette = {'inside' : 'grey', 'outside' : 'salmon'}, ax=ax)

# Add reference line:
values_y = []
values_x = []
def line_function():
    for i in range(-3,3):
        y = i
        values_x.append(i)
        values_y.append(y)
line_function()
ax.plot(values_x, values_y)

# Set plot title and labels
ax.set_title('Wild-type and Mutant Metabolic Responses')
ax.set_xlabel('ΔM Value MT')
ax.set_ylabel('ΔM Value WT')
plt.show()

# 'Grey' metabolites (inside) - with low residual, and less deviation from the line show simmilar response between WT and MT plants, where
# 'Salmon' metabolites (outside) - with high residual, more deviation from the line show different responses between conditions.
# Comment: Deffinitely there is significant difference in metabolic response between wild-type (WT), and the mutant (MT) plants.

outside_metabolites = WT_MT_df[WT_MT_df["Residual_cutoff"] == 'outside'].head(6)
# Time points for the x-axis
x = [0, 8, 24]

# Create the figure and axes
fig, ax = plt.subplots()

# Loop over metabolites that are outside the residual cut-off
for index in outside_metabolites.index:
    # Get the values for the metabolite from rows 1 to 3:
    y1 = df.loc[1:3, index].values
    # Plot the metabolite data on the same axes
    ax.plot(x, y1, marker='o', linestyle='-', label=f"WT {index}")

# Set plot title and labels
ax.set_title('Metabolic Response Over Time for Selected Metabolites')
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Metabolic Response')
ax.legend()

plt.show()

# Code: https://github.com/teodorades/hackbio-biocoding-internship/blob/main/Stage-2/Task2.3.py








