# number_to_pattern with index and k inputs                
def number_to_symbol(Index):
    nucleotide = {"A":0, "C":1, "G":2, "T":3}
    for k, v in nucleotide.items():
        if v == Index:
            return k
       
def number_to_pattern(Index, k):
    if k == 1:
        return number_to_symbol(Index)
    prefix_index = Index // 4
    r = Index % 4 
    symbol = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k-1)
    return "".join([prefix_pattern, symbol]) 
    
nucleotide = {"A":0, "C":1, "G":2, "T":3}
def pattern_to_number(Pattern):
    if len(Pattern) == 0:
        return 0    
    symbol = Pattern[-1]
    prefix = Pattern[0:-1]
    return (4 * pattern_to_number(prefix) + nucleotide.get(symbol))
    
def computing_frequencies_no_space(Text, k):
    frequency_array = [None]*(4**k)
    for i in range(4**k):
        frequency_array[i] = 0
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] = frequency_array[j] + 1
    return ("".join(str(e) for e in frequency_array))    
    
def faster_frequent_words(Text, k):
    frequent_pattern = []
    
    # remove space from the return of 'computing_frequencies' function 
    # -> 'computing_frequencies_no_space' to give correct i (indices)
    frequency_array = computing_frequencies_no_space(Text, k)
    
    max_count = max(frequency_array)
    for i in range(4**k - 1):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_pattern.append(pattern)
    return " ".join(frequent_pattern) 
