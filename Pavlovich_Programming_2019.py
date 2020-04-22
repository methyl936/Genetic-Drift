# -*- coding: utf-8 -*-
"""

LIFE97011 - Computing
Python Programming - Assessed Exercise No. 2
@Author: Slaviana Pavlovich

"""

# Importing Python packages
import numpy as np
from numpy import random as rd
from random import randint, uniform
import matplotlib.pyplot as plt


# Writing a function for Task 1 
def Task1(popsize, gen, freqA, freqB): 
    # Creating empty frequencies list     
    freq_a = []  
    freq_b = []
    # Adding initial frequencies for alleles A and B in respective lists
    freq_a.append(freqA)
    freq_b.append(freqB)
    
    #Creating a list for the population size with 50 'A' and 50 'B' alleles
    pop_array = []
    for i in range(0, int(popsize/2)):
        pop_array.append('A')
    for i in range(int(popsize/2),popsize):
        pop_array.append('B')
        
    # Running the simulations up to 1000 times
    for i in range(gen):
        # Implementing the condition that frequences should be greater than 0
        if (freqA > 0) and (freqB > 0):
            # Generating a random sample of 100 from pop_array with replacement 
            pop_array_new = rd.choice(pop_array, size = 100, replace = True)  
            # Counting number of alleles A and B in a new sample
            A = np.count_nonzero(pop_array_new == "A") 
            B = np.count_nonzero(pop_array_new == "B") 
            # Computing the frequencies of alleles A and B
            freqA = A / (A + B)
            freqB = B / (A + B)
            # Adding new allele frequencies to the lists freqA and freqB
            freq_a.append(freqA)
            freq_b.append(freqB)
            # Amending the population list
            pop_array = pop_array_new
            
    # Plotting the change in allele frequency with each generation     
    # Creating array with evenly spaced x values    
    len_scale = len(freq_a)
    x = np.arange(0, len_scale, 1)
    # Changing figure size
    fig1 = plt.figure(figsize = (16,9))
    # Labelling the plot
    plt.plot(x, freq_a, label = 'Allele A')
    plt.plot(x, freq_b, label = 'Allele B')
    plt.legend()
    plt.title('Change in allele frequency with each generation', fontsize = 20)
    plt.xlabel('Number of generations', fontsize = 20)
    plt.ylabel('Frequency of allele', fontsize = 20)
    plt.show()
    
    # Returning the plot from Task 1
    return fig1

# Running the function with the given values
Task1(popsize = 100, gen = 1000, freqA = 0.5, freqB = 0.5)
  

# Writing a function for Task 2      
def Task2(popsize, gen, freqAA, freqAa, freqaa):
    # Creating empty frequencies list     
    freq_AA = []  
    freq_Aa = []
    freq_aa = []
    # Adding initial frequencies for alleles A and B in respective lists
    freq_AA.append(freqAA)
    freq_Aa.append(freqAa)
    freq_aa.append(freqaa)
    
    #Creating a list for the population size with 25 'AA', 25 'aa', 50 'Aa' alleles
    pop_array = []
    for i in range(0, int(popsize/4)):
        pop_array.append('AA')
    for i in range(int(popsize/4),int(popsize/2)):
        pop_array.append('aa')
    for i in range(int(popsize/2),popsize):
        pop_array.append('Aa')
        
    pop_array_new = pop_array
    
    for i in range(gen):
        # Implementing the condition that frequences should be greater than 0
        if (freqaa > 0) and (freqAa > 0):
            # Creating empty arrays for new generations
            pop_array_ng = []
            pop_array_static = np.array(pop_array_new)
            
            # Picking a random pair of individuals from pop_array_new
            while popsize != len(pop_array_ng):
                # Picking a random individual from the population
                # and excluding the individual from it
                individual1 = pop_array_new.pop(randint(0, len(pop_array_new) - 1))
                # Second individual is chosen at random from the popululation
                # excluding individual 1
                individual2 = pop_array_new[randint(0, len(pop_array_new) - 1)]
                # Picking a random allele from individual 1 and 2
                # Combining the alleles
                next_gen = individual1[randint(0, 1)] + individual2[randint(0, 1)]
                # Saving the combination other than 'aa' regargless
                # Otherwise, generating a random probability between 0 and 1
                # And if the probability is less than 0.8 (as it is in 80% of the time)
                # then saving the combination too
                if next_gen != "aa" or uniform(0, 1) < 0.8:
                    pop_array_ng.append(next_gen)
                pop_array_new = pop_array_static.tolist()
            # Saving population for the next generation run
            pop_array_new = pop_array_ng
            
            # Counting allele frequencies AA, Aa and aa
            AA = np.count_nonzero(np.array(pop_array_new) == "AA") 
            Aa_1 = np.count_nonzero(np.array(pop_array_new) == "Aa")
            Aa_2 = np.count_nonzero(np.array(pop_array_new) == "aA")
            Aa = Aa_1 + Aa_2
            aa = np.count_nonzero(np.array(pop_array_new) == "aa") 
            # Computing the frequencies of alleles AA, Aa and aa
            freqAA = AA / (AA + Aa + aa)
            freqAa = Aa / (AA + Aa + aa)
            freqaa = aa / (AA + Aa + aa)
            # Adding new allele frequencies to the lists freqAA, freqAa and freqaa
            freq_AA.append(freqAA)
            freq_Aa.append(freqAa)
            freq_aa.append(freqaa)
            
    # Plotting the change in allele frequencies with each generation     
    # Creating array with evenly spaced x values    
    len_scale = len(freq_AA)
    x = np.arange(0, len_scale, 1)
    # Changing figure size
    fig2 = plt.figure(figsize = (16, 9))
    # Labelling the plot
    plt.plot(x, freq_AA, label = 'Genotype AA')
    plt.plot(x, freq_Aa, label = 'Genotype Aa')
    plt.plot(x, freq_aa, label = 'Genotype aa')
    plt.legend()
    plt.title('Change in genotypes with each generation', fontsize = 20)
    plt.xlabel('Number of generations', fontsize = 20)
    plt.ylabel('Frequency of genotypes', fontsize = 20)
    plt.show()
        
    # Returning the plot from Task 2
    return fig2

# Running the function with the given values
Task2(popsize = 100, gen = 500, freqAA = 0.25, freqAa = 0.5, freqaa = 0.25)
