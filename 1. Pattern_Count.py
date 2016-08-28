import sys
lines = sys.stdin.read().splitlines() # read in the input from STDIN
Text = lines[0]
Pattern = lines[1]

def pattern_count(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

print(pattern_count(Text,Pattern))


# sample input/output:
# - sample input: GCGCG    GCG
# - sample putput: 2
