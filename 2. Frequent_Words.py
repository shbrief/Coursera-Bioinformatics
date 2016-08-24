import sys
lines = sys.stdin.read().splitlines() # read in the input from STDIN
Text = lines[0]
k = int(lines[1])

def FrequentWords(Text, k):    
    kmer_dict = dict()
    for i in range(len(Text)-k+1):
	if Text[i:i+k] in kmer_dict:
            kmer_dict[Text[i:i+k]] += 1
	else:
	    kmer_dict[Text[i:i+k]] = 1
    kmers = [item[0] for item in kmer_dict.items() if item[1] == max(kmer_dict.values())]
    return(' '.join(kmers))

print(FrequentWords(Text,k))
