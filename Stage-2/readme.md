#### Task 2.6 Transcriptomics ####

Important libraries were imported (`pandas`, `seaborn`, `matplotlib.pyplot`, `math`).

Data was imported from .txt file, and DataFrame named `gene_df` were created from imported data.

*padj* values were extracted from the DataFrame as a list using `.tolist()` method.
To calucalte -log(10)padj, a funtion  named `log_padj()` was defined. The computed values were than added as a new column named *-log10padj* in the DataFrame.

To classify genes based on differential expression, upregulated genes were identified as those with log2fc > 1 and pval < 0.01, while downregulated genes were those with log2fc < -1 and pval < 0.01. All other genes were classified as insignificant. The classification was performed by iterating through both the *log2FoldChange* and *pvalue* using `zip()` function. The results were stored in a newly created column named "regulation of genes".


To calucalte the top 5  upregulated and downregulated genes `.nlargest()` and `.nsmallest()` method were used.

Finally, a Volcano plot scattering the `seaborn` and `matplotlib.pyplot` were used, where genes were color-coded based on their regulation status.

#### Task 2.4 Biochemistry & Oncology ####

Important libraries were imported (`pandas`, `matplotlib.pyplot`, `math`).

Data was imported from .txt files, and DataFrames named `sift_df` and `fold_df` were created from imported data. Because file has a lot of tabs and a lot of spaces: `sep='r\s+'` was used --> to properly create Dataframes.

As task request, new colum *specific_Protein_aa* was created from two existing columns *Protein* and *Amino_Acid* in boths Dataframes (`shift_df`, and `fold_df`)

*merged_df* was created using `.merge` method based on newly created *specific_Protein_aa*
`.drop` and `.rename` method were used to arrange newly created *merged_df* 

As defined in article, the SIFT Score below 0.05, and FoldX Score greater than 2 kCal/mol is deletarious. 
Mutants list was determing using this if conditions.

To extract the original (wild-type) amino_acid, new column was created: `merged_df["Wild_Type_AA"]` which stores first string (`.str[0]`) character of column `merged_df["Amino_Acid"]`.
To calculate the frequency of amino acid, list `freq_aa` was created, and method `.value_counts()` was used.

As asked in the task, using `matplotlib.pyplot as plt` the barplot and pie-chart were created.

