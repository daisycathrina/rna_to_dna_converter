# RNA to DNA Converter

def rna_to_dna(rna_sequence):
    return rna_sequence.replace("U", "T")

# Ask the user for an RNA sequence
rna = input("Enter RNA sequence: ").upper()

# Convert to DNA
dna = rna_to_dna(rna)

print("DNA sequence:", dna)