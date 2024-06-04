def obtener_complemento(dna):
    complemento = {
       'A': 'T',
       'T': 'A',
       'C': 'G',
       'G': 'C'
    }
    return''.join([complemento[base]for base in dna])
    secuencia="GGGTTAATGACTAATCAGCCCATGATCACACATAACTGTGGTGTCATGCATTTGGTATTTTTAATTTTTAGGGGGTCGAACTTGCTATGACTCAGCTATGACCTAAAGGTCCTGACTCAGTCAAATATAATGTAGCTGGG"
    print("secuencia original", secuencia)
    complemento= obtener_complemento(secuencia)
    print("secuencia complementaria",complemento)
    