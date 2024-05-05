from Bio import SeqIO

Total_sequences = 0
with open("seq_database.fasta", "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        Total_sequences += 1     
print("Total number of sequences tested:", Total_sequences)

Total_sequences_k = 0
with open("kinases_IPR000719.fasta", "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        Total_sequences_k += 1     
print("Total number of sequences kinase:", Total_sequences_k)

Total_sequences_p = 0
with open("phosphatases_IPR000387.fasta", "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        Total_sequences_p += 1     
print("Total number of sequences phosphatase:", Total_sequences_p)
