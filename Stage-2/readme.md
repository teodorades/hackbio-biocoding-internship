#### Task 2.6 Transcriptomics ####

Important libraries were imported (`pandas`, `seaborn`, `matplotlib.pyplot`, `math`).

Data was imported from .txt file, and DataFrame named `gene_df` were created from imported data.

*padj* values were extracted from the DataFrame as a list using `.tolist()` method.
To calucalte $$ \log_{10}(\text{padj}) $$, a funtion  named `log_padj()` was defined. The computed values were than added as a new column named *-log10padj* in the DataFrame.

To classify genes based on differential expression, upregulated genes were identified as those with log2fc > 1 and pval < 0.01, while downregulated genes were those with log2fc < -1 and pval < 0.01. All other genes were classified as insignificant. The classification was performed by iterating through both the *log2FoldChange* and *pvalue* using `zip()` function. The results were stored in a newly created column named "regulation of genes".


To calucalte the top 5  upregulated and downregulated genes `.nlargest()` and `.nsmallest()` method were used.

Finally, a Volcano plot scattering the `seaborn` and `matplotlib.pyplot` were used, where genes were color-coded based on their regulation status.
