nucleotide = {"A":0, "C":1, "G":2, "T":3}
def pattern_to_number(Pattern):
    if len(Pattern) == 0:
        return 0    
    symbol = Pattern[-1]
    prefix = Pattern[0:-1]
    return (4 * pattern_to_number(prefix) + nucleotide.get(symbol))
    

# sample input/output:
# - sample input: AGT
# - sample output: 11
