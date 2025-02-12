# Write a function for translating DNA to protein
RNA_code_table = {'UUU' : 'F', 'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V', 'UUC' : 'F', 'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V',  
'UUA' : 'L', 'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V', 'UUG' : 'L', 'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V',  
'UCU' : 'S', 'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A', 'UCC' : 'S', 'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',  
'UCA' : 'S', 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A', 'UCG' : 'S', 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',  
'UAU' : 'Y', 'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D', 'UAC' : 'Y', 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',  
'UAA' : 'Stop', 'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E', 'UAG' : 'Stop', 'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E',  
'UGU' : 'C', 'CGU' : 'R', 'AGU' : 'S', 'GGU' : 'G', 'UGC' : 'C', 'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G',  
'UGA' : 'Stop', 'CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G', 'UGG' : 'W', 'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G'
} # key:value, codon is key, amino-acid is value

def translate(DNA):
        # convert DNA to RNA
        RNA = DNA.replace('T', 'U')

        protein = [] # for a large sequence it is better to use [] than ''
        for i in range(0, len(RNA), 3):
            codon = RNA[i:i+3] #def of codon
            if codon in RNA_code_table:
                amino_acid = RNA_code_table[codon]
            if amino_acid == 'Stop':
                break
            protein.append(amino_acid)

        return(''.join(protein))

DNA = 'ATGGCCCTGTGGATGCGGGGAAGGCCAGGCACCGAGGGCCAGGGACCTGGCGGCTCTTCTACCAGCAGCAGCCTGTGGATGCGGGGAAGGCCAGGCACCGAGGGCCAGGGACCTGGCGGCTCTTCTACCAGCAGCAGCCTGTGGATGCGGGGAAGGCCAGGCACCGAGGGCCAGGGACCTGGCGGCTCTTCTACCAGCAGCAGCTGCCCTGGCAGCTGGAGGCGGGGCAGCCTGGAGCAGGACCTGCAGATCGCGGGCATCGCGGGCGGAGGAGGAGGGTGCCGCGCGGGAGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGA'
print(translate(DNA))


