def is_isogram(word):
    from collections import Counter 
    cnt = Counter(list(word.lower()))
    topCnt = cnt.most_common(1)
    if len(topCnt) > 0:
        (letter, count) = topCnt[0]
        return not( not(letter == '-' or letter == ' ' ) and count > 1 ) 
    else:
        return True