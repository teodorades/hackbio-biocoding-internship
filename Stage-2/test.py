import pandas as pd

sift_data = 'https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv'
fold_data = 'https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv'

# Read file with proper whitespace handling, when \t and ' ' was used, the dataframe was not properly print
sift_df = pd.read_csv(sift_data, sep=r'\s+') 
fold_df = pd.read_csv(fold_data, sep=r'\s+')
# print(sift_df) # --> check the printing of dataframe

sift_df["specific_Protein_aa"] = sift_df["Protein"] + '_' + sift_df["Amino_Acid"]
fold_df["specific_Protein_aa"] = fold_df["Protein"] + '_' + fold_df["Amino_Acid"]
modified_sift_df = sift_df.drop(["Protein", "Amino_Acid"], axis='columns')
modified_fold_df = fold_df.drop(["Protein", "Amino_Acid"], axis='columns')

# print(modified_sift_df, '\n', modified_fold_df) # --> check if the columns were added correctly

# merge datasets with specific_Protein_aa
merged_df = pd.merge(modified_fold_df, modified_sift_df, on="specific_Protein_aa")
# print(merged_df) # --> check

# A SIFT Score below 0.05 is deleterious
delet_sift = merged_df[merged_df["sift_Score"] < 0.05]
# A FoldX score greater than 2 kCal/mol is deleterious
delet_fold = merged_df[merged_df["foldX_Score"] > 2]
print(delet_fold, delet_sift)

mutants = []
for i in delet_sift['specific_Protein_aa']:  
    if i in delet_fold['specific_Protein_aa'].values:  
        mutants.append(i) 

print(mutants)
print(len(mutants))