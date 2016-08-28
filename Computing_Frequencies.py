nucleotide = {"A":0, "C":1, "G":2, "T":3}
def pattern_to_number(Pattern):
    if len(Pattern) == 0:
        return 0    
    symbol = Pattern[-1]
    prefix = Pattern[0:-1]
    return (4 * pattern_to_number(prefix) + nucleotide.get(symbol))
        
def computing_frequencies(Text, k):
    frequency_array = [None]*(4**k)
    for i in range(4**k):
        frequency_array[i] = 0
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] = frequency_array[j] + 1
    return (" ".join(str(e) for e in frequency_array))


# sample input/output
# - sample input: ACGCGGCTCTGAAA    2
# - sample output: 2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0
