def to_rna(dna_strand):
    rna = []
    for nuc in dna_strand:
        if nuc == "G":
            rna.append("C")
        if nuc == "C":
            rna.append("G")
        if nuc == "T":
            rna.append("A")
        if nuc == "A":
            rna.append("U")
    rna = "".join(rna)
    return rna