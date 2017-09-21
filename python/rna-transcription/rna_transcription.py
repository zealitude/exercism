def to_rna(dna):
    dna2rna_map = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U', 
    }

    rna = ''
    for c in dna:
        try:
            rna += dna2rna_map[c]
        except KeyError:
            return ''
    return rna
