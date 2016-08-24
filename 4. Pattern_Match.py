import sys
lines = sys.stdin.read().splitlines()
Pattern = lines[0]
Genome = lines[1]

def pattern_match(Pattern, Genome):
    count = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            count.extend([i])
    return (" ".join(str(e) for e in count))

print(pattern_match(Pattern,Genome))
