#### First Function 
Task_1: Write a function for translating DNA to protein

A dictionary (RNA_codon_table) was created to store information about codons and their corresponding amino acids.

The function for translating DNA to protein was developed following these steps:
1) To be more realistic, the DNA sequence (in the form of a string) is first translated into RNA by replacing the nucleotide 'T' with 'U' using the .replace() method.
2) An empty list (protein = []) was created to store the protein sequence.
3) The RNA sequence is iterated in steps of three nucleotides (codons) until the end of the sequence, as defined by len(RNA).
4) If a codon is present in RNA_codon_table, the corresponding amino acid is retrieved as the value associated with the codon key. If the codon is 'Stop', the function terminates. _This applies if all codons can be found in the dictionary._
5) Each identified amino acid is appended to the protein sequence list.
6) To ensure better visualization of the output, ''.join(protein) is used for printing.

#### Fourth function 

Task_4: Finally, write a function for calculating the hamming distance between your Slack username and twitter/X handle (synthesize if you don’t have one). Feel free to pad it with extra words if they are not of the same length.

Created the function for comparing the two useranames, for slack and x. 
The function for comparing the two usernames (Slack and X) was created:
1) First, the hamming_distance was initialized to 0.
2) An iteration was performed through the x_username.
3) If the character at a given index in x_username was different from the character at the same index in slack_username, the hamming_distance was increased by 1.

#### Second function
Task_2: Write a function that simulates and generates a logistic population growth curve. 
Your function should include 2 extra parameters that randomize the length of the lag phase and the exponential phase [See population curve here].Most living populations follow a logistic population growth. Therefore, your growth curve can be: Population Size vs Time, Cell density vs Time, OD vs Time, CFU vs Time, etc. Using your function, generate a dataframe with 100 different growth curves.

- Import important libraries
- Defined constants necessary for calculation

Creating function logistic_growth_curve(initial_population, max_value, max_time, lag_phase, expo_phase):
1) Making empty list named population_sizes, which will append calculated values
2) Defining necessary if/elif/else conditions:
Lag phase: Population remains nearly constant.
Exponential phase: Population follows a logistic growth function.
Stationary phase: Growth slows down, reaching carrying capacity.
Death phase: Population decreases.
4) Create a function (generate_different_curves) that calls logistic_growth_curve 100 times:
Use randomized lag and exponential phase values for each curve:
random.randint(min, max) generates an integer.
random.uniform(min, max) generates a floating-point number.
Store each generated growth curve in a list (dataframe).
5) Plotting the results:
The y-axis values are taken from the generated population sizes.
The x-axis values represent time (the length of the population list).
Use matplotlib.pyplot to visualize the results.

#### Third funtion
Task_3: Write a function for determining the time to reach 80% of the maximum growth; usually the carrying capacity

Defined the function for calulating time at 80% of maximum growth, and iterate i to find approximately same value in dataframe[0] with calculated 80%.
