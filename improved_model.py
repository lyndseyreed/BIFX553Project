import os
import subprocess
from Bio import SeqIO
from Bio import SearchIO

def new_run_hmmsearch(query_sequence, hmm_profile):
    '''
    This function takes in a fasta file with multiple sequences, parses the file with SeqIO,
    runs hmmsearch from command line subprocess, and returns the significant hits from the search as a list.
    '''
    query_file = "temp_query.fasta"
    with open(query_file, "w") as f:
        SeqIO.write(query_sequence, f, "fasta")
    cmd = ["hmmsearch", "--incE", "0.05", "--tblout", "temp_results.out", hmm_profile, query_file]
    subprocess.run(cmd, check=True)
    results = list(SearchIO.parse("temp_results.out", "hmmer3-tab"))  
    os.remove(query_file)
    os.remove("temp_results.out")
    return results

def categorize_sequences(input_fasta, kinase_profiles, phosphatase_profile):
    '''
    This functin takes in an input_fasta to categorize, hmm profiles of phosphatases and kinases,
    then runs the hmmsearch function and saves the results as either phosphatase or kinase 
    in 2 respective files.
    '''
    kinase_results = {}
    phosphatase_results = {}

    with open(input_fasta, "r") as f:
        for record in SeqIO.parse(f, "fasta"):
            is_phosphatase = False

            phosphatase_hits = new_run_hmmsearch(record, phosphatase_profile)
            if phosphatase_hits:
                is_phosphatase = True
                if record.id not in phosphatase_results:
                    phosphatase_results[record.id] = []
                phosphatase_results[record.id].append(("PS00123", "Phosphatase"))

            if not is_phosphatase:
                for kinase_name, kinase_profile in kinase_profiles.items():
                    kinase_hits = new_run_hmmsearch(record, kinase_profile)
                    if kinase_hits:
                        if record.id not in kinase_results:
                            kinase_results[record.id] = []
                        kinase_results[record.id].append((kinase_name, "Kinase"))
                        break


    with open("kinase_predict_improved.txt", "w") as kinase_file:
        for seq_id, results in kinase_results.items():
            for result in results:
                kinase_file.write(f"{seq_id}: Predicted Kinase - {result[0]}\n")
    with open("phosphatase_predict_improved.txt", "w") as phosphatase_file:
        for seq_id, results in phosphatase_results.items():
            for result in results:
                phosphatase_file.write(f"{seq_id}: Predicted Phosphatase - {result[0]}\n")



##USER INPUT AREA##

input_fasta = "seq_database.fasta"
kinase_profiles = {"PS00109": "prosite_alignments_for_logos/hmmer_hhm/PS00109.msa.hmm", "PS00107": "prosite_alignments_for_logos/hmmer_hhm/PS00107.msa.hmm", "PS00108": "prosite_alignments_for_logos/hmmer_hhm/PS00108.msa.hmm", "PS50011": "prosite_alignments_for_logos/hmmer_hhm/PS50011.msa.hmm"}
phosphatase_profile = "prosite_alignments_for_logos/hmmer_hhm/PS00123.msa.hmm"

categorize_sequences(input_fasta, kinase_profiles, phosphatase_profile)