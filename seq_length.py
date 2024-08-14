from Bio import SeqIO
import re


# Define a function to read sequences from a FASTA file and identify TE sequences
def read_fasta_and_identify_te_sequences(fasta_file, te_pattern):
    te_sequences = []
    with open(fasta_file, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequence = str(record.seq)
            te_matches = re.findall(te_pattern, sequence)
            if te_matches:
                te_sequences.append(te_matches)
    return te_sequences


# Define a function to analyze TE sequences and calculate statistics
def analyze_te_sequences(te_sequences):
    total_te_count = 0
    te_lengths = []

    for seq_list in te_sequences:
        total_te_count += len(seq_list)
        for seq in seq_list:
            te_lengths.append(len(seq))

    average_te_length = sum(te_lengths) / total_te_count if total_te_count > 0 else 0
    return total_te_count, average_te_length


# Main function for TE genotypes analysis
def main(fasta_file, te_pattern):
    te_sequences = read_fasta_and_identify_te_sequences(fasta_file, te_pattern)

    total_te_count, average_te_length = analyze_te_sequences(te_sequences)

    print(f"Total TE Sequences: {total_te_count}")
    print(f"Average TE Length: {average_te_length:.2f} bp")


if __name__ == "__main__":
    # Specify your FASTA file and TE sequence pattern
    fasta_file = "SRR11771595.fa"
    te_pattern = r"TTTTTTTTGGTACCTATTCCTCCAGGAATTACTG"  # Update with your TE pattern regular expression

    main(fasta_file, te_pattern)
