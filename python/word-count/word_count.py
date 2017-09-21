def word_count(input_str):
    from collections import Counter
    import re
    cnt = Counter(re.split('[^a-z0-9]+', input_str.lower()))
    del cnt['']
    return dict(cnt)
