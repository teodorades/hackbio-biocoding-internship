import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

# Task Code 2.1: Microbiology

# Task Code 2.4:Biochemistry & Oncology


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













    



