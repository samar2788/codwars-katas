def DNA_strand(dna):
    trans = str.maketrans('ATGC', 'TACG')
    return dna.translate(trans)
