import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

# Task Code 2.1: Microbiology

# Task Code 2.4:Biochemistry & Oncology
sift_data = 'https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv'
fold_data = 'https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv'

# Read file with proper whitespace handling, when \t and ' ' was used, the dataframe was not properly print
sift_df = pd.read_csv(sift_data, sep=r'\s+') 
fold_df = pd.read_csv(fold_data, sep=r'\s+')
# print(sift_df) # --> check the printing of dataframe

sift_df["specific_Protein_aa"] = sift_df["Protein"] + '_' + sift_df["Amino_Acid"]
fold_df["specific_Protein_aa"] = fold_df["Protein"] + '_' + fold_df["Amino_Acid"]
# print(sift_df, '\n', fold_df) # --> check if the columns were added correctly

# merge datasets with specific_Protein_aa
merged_df = pd.merge(fold_df, sift_df, on="specific_Protein_aa")

# Drop duplicate columns
merged_df = merged_df.drop(columns=["Protein_y", "Amino_Acid_y"])
# Rename remaining columns for clarity
merged_df = merged_df.rename(columns={"Protein_x": "Protein", "Amino_Acid_x": "Amino_Acid"})
# print(merged_df) # --> check

# A SIFT Score below 0.05 is deleterious
delet_sift = merged_df[merged_df["sift_Score"] < 0.05]
# A FoldX score greater than 2 kCal/mol is deleterious
delet_fold = merged_df[merged_df["foldX_Score"] > 2]
# print(delet_fold, delet_sift) --> check

mutants = []
for i in delet_sift["specific_Protein_aa"]:  
    if i in delet_fold["specific_Protein_aa"].values:  
        mutants.append(i) 
# print(mutants)
# print(len(mutants)) # --> check

""" Study the amino_acid_substitution_nomenclature
(https://atlasgeneticsoncology.org/teaching/30067/nomenclature-for-the-description-of-mutations-and-other-sequence-variations#section-3)"""

# Extract the original (wild-type) amino acid
merged_df["Wild_Type_AA"] = merged_df["Amino_Acid"].str[0]
# print(merged_df) # --> check

# Generate frequency table:
freq_aa = merged_df["Wild_Type_AA"].value_counts()
print(freq_aa)

# Generate a barplot:
plt.bar(x=freq_aa.index, height=freq_aa.values)
plt.xlabel("Wild Type AA")
plt.ylabel("Frequency")
plt.show()

# Generate a pie-chart:
plt.pie(freq_aa.values, labels=freq_aa.index, textprops={'fontsize': 6})
plt.show()

"""The amino acid with the highest impact on protein structure and function is: A (alanine).
    Alanine has non-polar, small side chain, hydrofobic structure, and no charge."""


# Task Code 2.6:Transcriptomics
gene_data = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"
gene_df = pd.read_csv(gene_data, sep= ' ')

padj_list = gene_df['padj'].tolist() # creating separete list from dataframe 'padj' column

# Calculate -log10padj that will be used for y-axis values in Volcano plot
log_padj_values = []

def log_padj():
    for i in padj_list:
        log_value = -math.log10(i)
        log_padj_values.append(log_value)

    return log_padj_values

gene_df["-log10padj"] = list(log_padj())
# print(gene_df) # --> check if new column -log10padj is added

regulation_of_genes = []
# Determine the upregulated genes (Genes with Log2FC > 1 and pvalue < 0.01)
# Determine the downregulated genes (Genes with Log2FC < -1 and pvalue < 0.01)

for log2fc, pval in zip(gene_df["log2FoldChange"], gene_df["pvalue"]): # zip allows iteration over two columns
    if log2fc > 1 and pval < 0.01:
        regulation = 'up'
    elif log2fc < -1 and pval < 0.01:
        regulation = 'down'
    else:
        regulation = 'insignificant'
    regulation_of_genes.append(regulation)

gene_df["regulation of genes"] = list(regulation_of_genes)
# print(gene_df) # --> check if we have new colum added to dataframe gene_df

# Get top 5 upregulated and downregulated genes
top_upregulated = gene_df.loc[gene_df["regulation of genes"] == "up"].nlargest(5, "log2FoldChange")
top_downregulated = gene_df.loc[gene_df["regulation of genes"] == "down"].nsmallest(5, "log2FoldChange")

print(f'Top 5 Upregulated genes: \n{top_upregulated[["Gene", "log2FoldChange", "pvalue"]]}')
print(f'Top 5 Downregulated genes: \n{top_downregulated[["Gene", "log2FoldChange", "pvalue"]]}')

# Volcano plot
sns.scatterplot(data=gene_df, x="log2FoldChange", y="-log10padj", hue = "regulation of genes")
plt.xlabel("log2 Fold Change")
plt.ylabel("-log10(padj)")
plt.title("Volcano Plot")
plt.show() 













    



