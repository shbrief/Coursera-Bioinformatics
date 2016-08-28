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

# Vibrio cholerae example in Septic
import urllib
seq = urllib.urlopen('https://stepik.org/media/attachments/lessons/3/Vibrio_cholerae.txt').read()   # len(seq) = 1108251
pattern_match("CTTGATCAT", seq)


# sample input/output:
# - sample input: ATAT  GATATATGCATATACTT
# - sample output:  1 3 9
