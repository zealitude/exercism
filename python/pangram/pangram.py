def is_pangram(input_str):
    # print '------'
    from collections import Counter  
    cnt = Counter(list(input_str.lower()))

    a_ascii = ord('a')
    for letter_offset in xrange(26):
        # print a_ascii, letter_offset, chr(a_ascii+letter_offset), cnt[chr(a_ascii+letter_offset)]
        if cnt[chr(a_ascii+letter_offset)] is 0:
            return False
    
    return True