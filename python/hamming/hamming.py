def distance(s1, s2):
    seq1 = list(s1)
    seq2 = list(s2)

    if len(seq1) is not len(seq2):
        raise ValueError()

    distance = 0
    for idx, c in enumerate(seq1):
        if c is not seq2[idx]:
            distance += 1
    
    return distance

