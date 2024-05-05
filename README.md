# 553Project

Under the BlackBoard companion site for this course, Course Documents -> Project Protein Motifs are 3 files: 2 files containing protein sequences of kinases and phosphatases respectively. The belong accoding to PFAM/InterPro to different protein families: kinases add phosophate groups to their substrate, and phosphatases remove phosphate groups. But frequently in biology it is the case that proteins that do "the opposite" have similarities, because they contain similar bindings sites.
In a different project we try to see if representations of proteins by averaged embedding vectors is superior at distinguishing protein families compared to using sequence alignments&similarity.  You can choose to do that track.
But what I am discribing here is a slightly different but equally interesting focus: protein short linear motifs (SLIMs). By the way some of the descriptions below I will use as README information for that project.

A prime resource for motif searches is PROSITE - a database of essentially 'regular expressions', so strict sequence pattern rules. More general I find the representation of such motifs by sequence profiles - so aligned sequences but only of the motif regions not the whole protein. 
So, I downloaded a directory with hundreds of such sequence profiles. Next, I saved you some work by creating a hidden markov model for each sequence profile with a suite of bioinformatics programs called Hmmer (http://hmmer.org/ ). This is located in subdirectory hmmer_hmmâ€‹).
With the program hmmsearchâ€‹ one can now search for the presence of each of the motifs in a database of sequences. If we use as database of sequences just the two sets of FASTA files for kinases we can do a variety of things:
If one looks at the Prosite annotation for kinases (https://prosite.expasy.org/PDOC00100 )
one sees that there are 3 motifs listed that kinases should have (ids PS50011, PS00107, PS00108, PS00109). Using hmmsearch, one can find hits of these motifs agains our sequences. Example:
the usage is:
hmmsearch  <MYMOTIF>  <MYSEQUENCES>â€‹
so something like
hmmsearch hmmer_hmm/PS00107.msa.hmm MY_PATH/kinases_IPR000719.fastaâ€‹

For phosphatases, the motif with is PS000123 is annotated to be present (https://prosite.expasy.org/PDOC00113 ).


We want to accomplish 2 things:
Evaluate how performant each of the Prosite motifs are for distinguishing kinases from proteases? The kinase motifs should not have hits for phosphatase whole-protein sequences, and vice versa the phosphatase motifs should have no hits for the whole-protein kinase sequences. Any hits there we count as false positives otherwise as true negatives. Next, we want kinase motifs to have hits in kinase whole protein sequences (true positives), otherwise if there is no hit for a sequence it counts as false negative. The total number of TP, TN, FP, FN should be the number of kinase sequences plus the number of phosphatase sequences. One can analyze the two sequence sets separately and later add the numbers or one can concatenate the FASTA files and analyze the matches or lack thereof on the combined data. Let's try to get some metrics that way! It will lead to different metrics for each of the mentioned motifs. Combining motifs is fascinating but goes beyond the scope of this project - it would then be essentially a language of motifs one deals with.

Next, we want to try to improve upon the motif concept as it is common in bioinformatics. The approach using hidden Markov models to define protein families works very well for whole protein sequences (that is the foundation of PFAM / InterPro). But motif searches have a mixed/bad reputation, because protein sequence motifs are so short, that in a different molecular context the same sequence pattern could be doing something entirely different. But now we have more data: we have residue-specific embedding vectors and we have the 3D structure of each of the involved proteins. You can choose whether to focus on adding structural constraints or employing residue-specific embedding vectors (one could average over the embedding vectors corresponding to the short linear motif).  Once you are at that step let's discuss and you will obtain more data depending on that.

I provided concrete steps and data to facilitate making concrete progress with the project. It is just a suggestion, but time is getting short and one needs to decide on a path of action. As mentioned, there are other prepared project routes (so far 3 with prepared data): motif searches (described here), protein family searches based on averaged embedding vectors (described separately) and protein per-residue embeddings to predict disordered regions (described previously in an announcement). Each of these routes have concrete data to get started with. If you already progressed far with something else let's discuss, that could be fine also.








ORDER OF EXECUTION:

combine.py
original_model.py
compare_results.py
improved_model.py
compare_results_improved.py
