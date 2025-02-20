#### Task 2.6 Transcriptomics ####

Important libraries were `import` (pandas, seaborn, matplotlib.pyplot, math).

Data was imported from txt file, and dataframe (gene_df) we created from imported data.

*padj* values column were separated from dataframe in a list using `.tolist()` method.
To calucalte $$ \log_{10}(padj) $$ funtion `log_padj()` was defined.

New column *-log10padj* were created with values calucalted from defined function.

For the determination of upregulated (Genes with log2fc > 1 and pval < 0.01) and downregulated genes (Genes with log2fc < -1 and pval < 0.01) the iteration was done throught both *log2FoldChange* and *pvalue* using `zip`. All other values of log2fc and pval were determined as insignificant.

Again, new column was added: *regulation of genes*

To calucalte the top 5  upregulated and downregulated genes `.nlargest` and `.nsmallest` method were used.

For the Volcano plot scattering the seaborn and matplotlib.pyplot were used.
