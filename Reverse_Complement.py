# This code doesn't have standard input/output part for Septic submission.

pair = {"A":"T", "T":"A", "G":"C", "C":"G"}    
def reverse_complement(seq):
    reverse = seq[::-1]
    bases = list(reverse)
    complement = [pair.get(base,base) for base in bases]
    reverse_complement = ''.join(complement)
    return reverse_complement 
