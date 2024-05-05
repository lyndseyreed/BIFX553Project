# combine the 2 fasta files into one

def concatenate_fasta_files(file1, file2, output_file):
    '''
    This function takes in 2 files and combines them into one
    '''
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        for line in f1:
            out.write(line)
        for line in f2:
            out.write(line)

concatenate_fasta_files("kinases_IPR000719.fasta", "phosphatases_IPR000387.fasta", "seq_database.fasta")