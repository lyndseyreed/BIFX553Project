from Bio import SeqIO

def compare_predicted(hmmsearch_results_file, fasta_file):
    predicted = set()
    with open(hmmsearch_results_file, "r") as f:
        for line in f:
            predict_id = line.split("|")[0]
            predicted.add(predict_id)

    sequences = set()
    with open(fasta_file, "r") as f:
        for record in SeqIO.parse(f, "fasta"):
            sequence_id = record.id.split("|")[0]
            sequences.add(sequence_id)

    common_sequences = predicted.intersection(sequences)
    return len(common_sequences)

##Basic Summary Statistics##

True_Positives = compare_predicted("kinase_predict.txt", "kinases_IPR000719.fasta")
print("Common sequences between predicted kinase and kinase FASTA file (True Positives):")
print(True_Positives)

True_Negatives = compare_predicted("phosphatase_predict.txt", "phosphatases_IPR000387.fasta")
print("Common sequences between predicted phosphatase and phosphatase FASTA file (True Negatives):")
print(True_Negatives)

False_Positive = compare_predicted("phosphatase_predict.txt", "kinases_IPR000719.fasta")
print("Common sequences between predicted phosphatase and kinase FASTA file (False Positives):")
print(False_Positive)

False_Negatives = compare_predicted("kinase_predict.txt", "phosphatases_IPR000387.fasta")
print("Common sequences between predicted phosphatase and kinase FASTA file (False Negatives):")
print(False_Negatives)

Total_sequences = 0
with open("seq_database.fasta", "r") as f:
    for record in SeqIO.parse(f, "fasta"):
        Total_sequences += 1     
print("Total number of sequences tested:", Total_sequences)


with open("phosphatase_predict.txt", "r") as file:
    lines = file.readlines()
    Total_predicted_p = len(lines)

with open("kinase_predict.txt", "r") as file:
    lines = file.readlines()
    Total_predicted_k = len(lines)

Total_predicted = (Total_predicted_p + Total_predicted_k)

print("Total number of matches found:", Total_predicted)

print("Total number of sequences not found to match:", (Total_sequences - Total_predicted))

accuracy = (True_Negatives +True_Positives) / Total_predicted
sensitivty = True_Positives / (True_Positives + False_Negatives)
specificity = True_Negatives / (True_Negatives + False_Positive)

print("The accuracy of the inital model is:", accuracy)
print("The sensitivity of the inital model is:", sensitivty)
print("The specificity of the inital model is:", specificity)

##Based on this information it would seem that the model has a large amount of False positives and a low accuracy of 0.5.
#the next steps would be adjusting the e-value threshold since i have the original model to --max to remove the thresholds.

import matplotlib.pyplot as plt 

categories = ['True Positives', 'True Negatives', 'False Positives', 'False Negatives']
counts = [True_Positives, True_Negatives, False_Positive, False_Negatives]

plt.figure(figsize=(10, 6))
plt.bar(categories, counts, color=['green', 'blue', 'red', 'orange'])
plt.xlabel('Categories')
plt.ylabel('Counts')
plt.title('Performance Metrics')
plt.show()