# protein_alignment_pipeline.py

from Bio import AlignIO
from Bio.pairwise2 import format_alignment
from Bio.pairwise2 import align

# Define the path to your alignment file
alignment_file = input("Location of input file :")

# Read the alignment file using BioPython's AlignIO.read() function
alignment = AlignIO.read(alignment_file, "stockholm")

# Print the alignment object to verify successful reading
print(alignment)

# Extract two sequences from the alignment (for example, the first two sequences)
sequence1 = alignment[2].seq
sequence2 = alignment[3].seq

# Perform pairwise alignment between the two sequences
alignments = align.globalxx(sequence1, sequence2)

# Print the first alignment
print("Pairwise Alignment:")
print(format_alignment(*alignments[0]))

# Multiple Sequence Alignment
print("Alignment length:", alignment.get_alignment_length())

# Print each sequence and its ID in the alignment
print("\nMultiple Sequence Alignment:")
for record in alignment:
    print(f"{record.seq} - {record.id}")

# Write the alignment results to a file
with open("alignment_results.txt", "w") as file:
    file.write("Pairwise Alignment:\n")
    file.write(format_alignment(*alignments[0]))
    file.write("\n\nMultiple Sequence Alignment:\n")
    for record in alignment:
        file.write(f"{record.seq} - {record.id}\n")

print("Alignment results saved to alignment_results.txt.")
