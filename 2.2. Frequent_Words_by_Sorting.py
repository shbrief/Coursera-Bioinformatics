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

def finding_frequent_words_by_sorting(Text, k):
    frequent_patterns = []
    index = [None]*(4**k)
    count = [None]*(4**k)
    
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        index[i] = pattern_to_number(pattern)
        count[i] = 1
    sorted_index = [x for x in sorted(index) if x is not None]
    
    for i in range(1, len(Text)-k+1):
        if sorted_index[i] == sorted_index[i-1]:
            count[i] = count[i-1] + 1
    max_count = max(count)
    
    for i in range(len(Text)-k+1):
        if count[i] == max_count:
            pattern = number_to_pattern(sorted_index[i], k)
            frequent_patterns.append(pattern)
    return " ".join(frequent_patterns)
