# Protein Sequence Alignment and Evolutionary Analysis Pipeline

## Overview
This pipeline performs pairwise and multiple sequence alignment of protein sequences using BioPython. It aims to explore evolutionary relationships between neurotransmitter-gated ion-channel transmembrane proteins and fibrinogen, focusing on sequence conservation and functional domain identification. The pipeline enables further evolutionary analysis and molecular modeling based on conserved and variable regions.

## Features
- **Pairwise Sequence Alignment**: Uses global alignment to compare two sequences at a time and prints the alignment.
- **Multiple Sequence Alignment (MSA)**: Analyzes and visualizes sequence conservation and variability across multiple sequences.
- **Evolutionary Insights**: Helps identify conserved residues critical for structural integrity and functional domains in protein sequences.
- **Molecular Modeling Preparation**: Facilitates selection of protein sequences for building molecular models based on conservation and structural relevance.

## Requirements
- Python 3.x
- BioPython package

You can install the necessary Python package using pip:

```
pip install biopython
```

## Usage

1. Prepare a **Stockholm format** alignment file containing the protein sequences to be analyzed.
    <img width="483" alt="image" src="https://github.com/user-attachments/assets/81082674-59c0-4274-8a83-8ea7d1deeea5" />
    
    or use the Fibrogen input file - PF12160.alignment.seed

3. Run the script:

```
python protein_alignment_pipeline.py
```

3. Provide the file path to the alignment file when prompted.
4. The pipeline will print the pairwise and multiple sequence alignments and save the results to a file named `alignment_results.txt`.

## Output

- **Pairwise Alignment**: Shows the alignment of two selected sequences with details of matches, mismatches, and gaps.
- **Multiple Sequence Alignment**: Lists the sequences and their IDs in the alignment.
- **alignment_results.txt**: A text file containing the results of both pairwise and multiple sequence alignments.

## Example

Example output of pairwise alignment:

```
Pairwise Alignment:
  ACGT--GTA
  |||  |||
  ACGTGGGTA
```

Example output of multiple sequence alignment:

```
ACGT--GTA - Sequence_1
ACGTGGGTA - Sequence_2
ACGTG-GTA - Sequence_3
```
  <img width="758" alt="image" src="https://github.com/user-attachments/assets/ded114df-4998-477d-8eff-1d9ebaea32b3" />
  
## FIBRGEN RESULTS:
### OUTPUT
  <img width="598" alt="image" src="https://github.com/user-attachments/assets/c6f2bd1e-4dcd-446c-9281-d8ede92132d5" />


