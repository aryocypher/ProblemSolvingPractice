
#Repetitions


# Time limit: 2.00 s
# Memory limit: 512 MB



# You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
# Input
# The only input line contains a string of n characters.
# Output
# Print one integer: the length of the longest repetition.
# Constraints

# 1 \le n \le 10^6

# Example
# Input:
# ATTCGGGA

# Output:
# 3

dna=input('')

i=0
n=len(dna)
res=0
while i<n:
    j=i
    while j<n and dna[i]==dna[j]:
        j+=1
    res=max(res,j-i)
    i=j

print(res) 