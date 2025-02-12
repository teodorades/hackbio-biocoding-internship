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

# Forth function
""" Finally, write a function for calculating the hamming distance
 between your Slack username and twitter/X handle (synthesize if you don’t have one). 
 Feel free to pad it with extra words if they are not of the same length."""


def compare(x_username, slack_username):
    hamming_distance = 0
    for i in range(len(x_username)):
        if x_username[i] != slack_username[i]:
            hamming_distance += 1
    return hamming_distance
print(compare('desteodora', 'Teodoraaaa'))

# Second function
""" Write a function that simulates and generates a logistic population growth curve. 
Your function should include 2 extra parameters that randomize the length of the lag phase and the exponential phase [See population curve here].
Most living populations follow a logistic population growth. 
Therefore, your growth curve can be: Population Size vs Time, Cell density vs Time, OD vs Time, CFU vs Time, etc
Using your function, generate a dataframe with 100 different growth curves """
import math
import random
import pandas as pd

def logistic_growth_cruve(initial_population, time, max_value, lag_phase, expo_phase):
    for time in range(time - lag_phase, 400):
        population_size = max_value/ (1+ ((max_value - initial_population)/initial_population) * math.exp(-expo_phase * (time - lag_phase)))
        # defined stationary and dead phase
        if 20 <= time <= 150:
          population_size = 20
        elif time <=150:
         population_size -= 50

def generate_logistic_gowth_curve(num = 100):
    rows  = [] 

    for i in range(num):
        initial_population = random.randint(0,5)
        max_value = random.randint(50, 200)
        lag_phase = random.randint(0,10)
        expo_phase = random.randint(0.1,1)
         
print(logistic_growth_cruve())

