def clump_finding(Genome,k,L,t):
    # find how frequently kmer show up in genome
    # kmer_dict dictionary -> {pattern, [frequency, [list of kmers' indicies]]}
    kmer_dict = {}
    for i in range(len(Genome)-k+1):
        pattern = Genome[i:i+k]
	if pattern in kmer_dict:
		kmer_dict[pattern][0] += 1
		kmer_dict[pattern][1].append(i)		
	else:
		kmer_dict[pattern] = [1, [i]] 
    print(kmer_dict)
    		
    # kmer_candidate dictionary -> [sequence, [list of kmers' indicies]]
    kmer_candidate = [[kmer[0], kmer[1][1]] for kmer in kmer_dict.items() if kmer[1][0] >= t]
    
    # test wheather any consecutive 4 kmers' indices are within the length of L  
    kmer_clump = []
    for candidate in kmer_candidate:
        for i in range(len(candidate[1])-t+1):
            if candidate[1][i+t-1] - candidate[1][i] <= L:
                kmer_clump.append(candidate[0])    
    return (' '.join(kmer_clump))

    
# sample input/output:
# - sample input: CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA 5 50 4
# - sample output: CGACA GAAGA
