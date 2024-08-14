import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert FASTQ file into two separate FASTQ files.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input FASTQ file')
    parser.add_argument('-1', '--output1', type=str, required=True, help='Output file for read 1')
    parser.add_argument('-2', '--output2', type=str, required=True, help='Output file for read 2')
    return parser.parse_args()


def separate_reads(input_file, output_file1, output_file2):
    read1_id = None
    read1_seq = None
    read1_qual = None
    read1_b = None
    read2_id = None
    read2_seq = None
    read2_qual = None
    read2_b = None

    try:
        with open(input_file, 'r') as interleaved_file:
            
            with open(output_file1, 'w') as read1_file, open(output_file2, 'w') as read2_file:
                for line in interleaved_file:
                    if line.startswith('@'):
                        if '/1' in line:  # Read1 identifier
                            read1_id = line.strip()
                        elif '/2' in line:  # Read2 identifier
                            read2_id = line.strip()
                    elif read1_id and not read1_seq:  # Read1 sequence
                        read1_seq = line.strip()
                    elif read2_id and not read2_seq:  # Read2 sequence
                        read2_seq = line.strip()
                    elif read1_seq and not read1_b:  
                        read1_b = line.strip()
                    elif read2_seq and not read2_b:  
                        read2_b = line.strip()
                    elif read1_b and not read1_qual:  # Read1 quality scores
                        read1_qual = line.strip()
                    elif read2_b and not read2_qual:  # Read2 quality scores
                        read2_qual = line.strip()

                        read1_file.write(f"{read1_id}\n{read1_seq}\n+\n{read1_qual}\n")
                        read2_file.write(f"{read2_id}\n{read2_seq}\n+\n{read2_qual}\n")

                        # Reset variables for the next reads
                        read1_id = None
                        read1_seq = None
                        read1_qual = None
                        read1_b = None
                        read2_id = None
                        read2_seq = None
                        read2_qual = None
                        read2_b = None

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")


def main():
    args = parse_arguments()
    input_file = args.input
    output_file1 = args.output1
    output_file2 = args.output2

    separate_reads(input_file, output_file1, output_file2)


if __name__ == '__main__':
    main()
