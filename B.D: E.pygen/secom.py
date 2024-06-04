#primera funcionn definida. aplicaciones de conocimiento basico de variables.
def obtener_complemento(dna):
    complemento = {
       'A': 'T',
       'T': 'A',
       'C': 'G',
       'G': 'C'
    }
    return''.join([complemento[base]for base in dna]) #encontrar una forma rapida para carrear tantas bases
    secuencia="GGGTTAATGACTAATCAGCCCATGATCACACATAACTGTGGTGTCATGCATTTGGTATTTTTAATTTTTAGGGGGTCGAACTTGCTATGACTCAGCTATGACCTAAAGGTCCTGACTCAGTCAAATATAATGTAGCTGGG"
    print("secuencia original", secuencia)
    complemento= obtener_complemento(secuencia) #supuestamente para debug. Revisar más tarde
    print("secuencia complementaria",complemento)
    
