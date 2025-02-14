# First function. Write a function for translating DNA to protein
RNA_code_table = {'UUU' : 'F', 'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V', 'UUC' : 'F', 'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V',  
'UUA' : 'L', 'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V', 'UUG' : 'L', 'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V',  
'UCU' : 'S', 'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A', 'UCC' : 'S', 'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',  
'UCA' : 'S', 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A', 'UCG' : 'S', 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',  
'UAU' : 'Y', 'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D', 'UAC' : 'Y', 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',  
'UAA' : 'Stop', 'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E', 'UAG' : 'Stop', 'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E',  
'UGU' : 'C', 'CGU' : 'R', 'AGU' : 'S', 'GGU' : 'G', 'UGC' : 'C', 'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G',  
'UGA' : 'Stop', 'CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G', 'UGG' : 'W', 'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G'
} # key:value, codon is key, amino-acid is value

def translate(DNA:str):
        # convert DNA to RNA
        
        RNA = DNA.replace('T', 'U')

        protein = [] # for a large sequence it is better to use [] than ''
        for i in range(0, len(RNA), 3):
            codon = RNA[i:i+3] # def of codon
            if codon in RNA_code_table:
                amino_acid = RNA_code_table[codon]
            if amino_acid == 'Stop':
                break
            protein.append(amino_acid)

        return(''.join(protein))

DNA = 'ATGGCCCTGTGGATGCGGGGAAGGCCAGGCACCGAGGGCCAGGGACCTGGCGGCTCTTCTACCAGCAGCAGCCTGTGGATGCGGGGAAGGCCAGGCACCGAGGGCCAGGGACCTGGCGGCTCTTCTACCAGCAGCAGCCTGTGGATGCGGGGAAGGCCAGGCACCGAGGGCCAGGGACCTGGCGGCTCTTCTACCAGCAGCAGCTGCCCTGGCAGCTGGAGGCGGGGCAGCCTGGAGCAGGACCTGCAGATCGCGGGCATCGCGGGCGGAGGAGGAGGGTGCCGCGCGGGAGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGAGGCGGCGGA'
print(translate(DNA))

# Fourth function
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
import matplotlib.pyplot as plt
# defined constants:
MAX_VALUE = 50
MAX_TIME = 30

def logistic_growth_curve(initial_population, max_value, max_time, lag_phase, expo_phase):
    population = [] # list for storing the population_sizes from 1 - 30 days
    for time in range(max_time):
        if time < lag_phase:
            population_size = initial_population #staying in lag_phase
        elif lag_phase <= time < MAX_TIME*2/3:
            population_size = max_value/ (1+ ((max_value - initial_population)/initial_population) * math.exp(-expo_phase * (time - lag_phase)))
        
        # defined stationary and dead phase
        elif MAX_TIME*2/3 <= time < MAX_TIME*5/6:
            population_size = max_value
        else:
            population_size = -(time - MAX_TIME*5/6) + MAX_VALUE

        population.append(population_size)

    return population

dataframe=[] # store all informations about population_size in dataframe 

for i in range(100):
    # randomize lag_phase and expo_phase
    lag_phase=random.randint(0,10)
    expo_phase=random.uniform(0.1,1)
    generate_growth_curve = logistic_growth_curve(initial_population=10, max_value=MAX_VALUE, max_time=MAX_TIME, lag_phase=lag_phase, expo_phase=expo_phase)
    x = list(range(0, len(generate_growth_curve)))
    plt.plot(x,generate_growth_curve) # ploting of calculated data

    dataframe.append(generate_growth_curve) # generate dataframe

# Additional parametars for graphs
plt.xlabel('time (days)')
plt.ylabel('population size')
plt.title('Logistic growth curve')
plt.show()

# Third funtion
# Write a function for determining the time to reach 80% of the maximum growth; usually the carrying capacity
# 100 % is max_value, 80 %
def calculate_time_80_percent(population_size:list, max_value):
    population_size80 = max_value*80/100
    for i in range(len(population_size)):
        if population_size[i] >= population_size80:
            return i
print(calculate_time_80_percent(dataframe[0], max_value=MAX_VALUE))

# Code can be find on: https://github.com/teodorades/hackbio-biocoding-internship/tree/main/Stage-1
    

