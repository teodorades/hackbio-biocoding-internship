#### First Function 
Task: Write a function for translating DNA to protein

A dictionary (RNA_codon_table) was created to store information about codons and their corresponding amino acids.

The function for translating DNA to protein was developed following these steps:
1) To be more realistic, the DNA sequence (in the form of a string) is first translated into RNA by replacing the nucleotide 'T' with 'U' using the .replace() method.
2) An empty list (protein = []) was created to store the protein sequence.
3) The RNA sequence is iterated through in steps of three nucleotides (codons) until the end of the sequence, as defined by len(RNA).
4) If a codon is present in RNA_codon_table, the corresponding amino acid is retrieved as the value associated with the codon key. If the codon is 'Stop', the function terminates. _This applies if all codons can be found in the dictionary._
5) Each identified amino acid is appended to the protein sequence list.
6) To ensure better visualization of the output, ''.join(protein) is used for printing.

#### Fourth function 

Task: Finally, write a function for calculating the hamming distance between your Slack username and twitter/X handle (synthesize if you don’t have one). Feel free to pad it with extra words if they are not of the same length.

Created the function for comparing the two useranames, for slack and x. 
The function for comparing the two usernames (Slack and X) was created:

1) First, the hamming_distance was initialized to 0.
2) An iteration was performed through the x_username.
3) If the character at a given index in x_username was different from the character at the same index in slack_username, the hamming_distance was increased by 1.
