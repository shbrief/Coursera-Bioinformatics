# number_to_pattern using two inputs: index and k.    

def number_to_symbol(index):
    nucleotide = {"A":0, "C":1, "G":2, "T":3}
    for k, v in nucleotide.items():
        if v == index:
            return k
       
def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefix_index = index // 4
    r = index % 4 
    symbol = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k-1)
    return "".join([prefix_pattern, symbol]) 
    

# Sample Input: 45  4
# Sample Output: AGTC
