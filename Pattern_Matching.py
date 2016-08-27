# Pattern matching problem

def pattern_match(Pattern, Genome):
    count = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            count.extend([i])
    return (" ".join(str(e) for e in count))
