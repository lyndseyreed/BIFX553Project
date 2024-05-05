from Bio import SeqIO
from compare_results import compare_predicted

##Basic Summary Statistics##

True_Positives = compare_predicted("kinase_predict_improved.txt", "kinases_IPR000719.fasta")
print("Common sequences between predicted kinase and kinase FASTA file (True Positives):", True_Positives)

True_Negatives = compare_predicted("phosphatase_predict_improved.txt", "phosphatases_IPR000387.fasta")
print("Common sequences between predicted phosphatase and phosphatase FASTA file (True Negatives):", True_Negatives)

False_Positive = compare_predicted("phosphatase_predict_improved.txt", "kinases_IPR000719.fasta")
print("Common sequences between predicted phosphatase and kinase FASTA file (False Positives):", False_Positive)

False_Negatives = compare_predicted("kinase_predict_improved.txt", "phosphatases_IPR000387.fasta")
print("Common sequences between predicted phosphatase and kinase FASTA file (False Negatives):", False_Negatives)


Total_sequences = 0
with open("seq_database.fasta", "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        Total_sequences += 1     
print("Total number of sequences tested:", Total_sequences)

with open("phosphatase_predict_improved.txt", "r") as file:
    lines = file.readlines()
    Total_predicted_p = len(lines)
print(Total_predicted_p)

with open("kinase_predict_improved.txt", "r") as file:
    lines = file.readlines()
    Total_predicted_k = len(lines)
print(Total_predicted_k)

Total_predicted_improved = (Total_predicted_p + Total_predicted_k)

print("Total number of matches found:", Total_predicted_improved)
print("Total number of sequences not found to match:", (Total_sequences - Total_predicted_improved))

accuracy = (True_Negatives +True_Positives) / Total_predicted_improved

print("The accuracy of the inital model is:", accuracy)


## I am not sure what keeps happening but when i test without --max only hmmsearch fails to recognize phosphatase profiles. This may be because there are only 408 phosphatase to search and 4423 kinases to search
## so hmmsearch is not able to accuralty detect them?