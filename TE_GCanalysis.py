from Bio import SeqIO


# Function to calculate GC content of a sequence
def calculate_gc_content(sequence):
    gc_count = sum(1 for base in sequence if base in "GCgc")
    total_bases = len(sequence)
    gc_content = (gc_count / total_bases) * 100
    return gc_content


# Function to analyze TE genotypes from a FASTA file
def analyze_te_genotypes(fasta_file):
    sequences = SeqIO.parse(fasta_file, "fasta")
    gc_contents = []

    for seq_record in sequences:
        sequence = str(seq_record.seq)
        gc_content = calculate_gc_content(sequence)
        gc_contents.append(gc_content)

  

    return gc_contents


def main(fasta_file):
    gc_contents = analyze_te_genotypes(fasta_file)
    print("GC Contents of TE Sequences:")
    for i, gc_content in enumerate(gc_contents, start=1):
        print(f"TE Sequence {i}: {gc_content:.2f}%")


if __name__ == "__main__":
    fasta_file = "SRR11771595.fa"  # the path of the FASTA file
    main(fasta_file)
