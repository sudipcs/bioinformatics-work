#!/usr/bin/env python
# coding: utf-8

# ### Task 1: Given a GTF file, the script to extract and save the transcriptome features (Genes, Transcripts, Coding exons, 5' UTRs, 3' UTRs, and introns) into individual BED files.

# In[15]:


import pandas as pd
import os
# Read the GTF file
gtf_file_path = "gencode.v33.annotation.gtf"
gtf_df = pd.read_csv(gtf_file_path, sep='\t', header=None, comment='#')

# Define output folder path
output_folder = "output_result"  # output directory
# Create the directory
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create a dictionary to store feature data
features = {
    "genes": [],
    "transcripts": [],
    "coding_exons": [],   # ["CDS", "exon"]
    "5UTR": [],
    "3UTR": [],
    "introns": [],
}

# Iterate through the GTF data
for row in gtf_df.itertuples(index=False, name=None):
    feature_type = row[2]
    attributes = row[8]

    # Parse attributes to extract relevant information
    attribute_dict = dict(item.strip().split() for item in attributes.split(';') if item.strip())

    if feature_type == "gene":
        gene_id = attribute_dict["gene_id"].strip('"')
        gene_name = attribute_dict["gene_name"].strip('"')
        features["genes"].append((row[0], row[3] - 1, row[4], gene_id, gene_name))

    if feature_type == "transcript":
        transcript_id = attribute_dict["transcript_id"].strip('"')
        gene_id = attribute_dict["gene_id"].strip('"')
        gene_name = attribute_dict["gene_name"].strip('"')
        features["transcripts"].append((row[0], row[3] - 1, row[4], transcript_id, gene_id, gene_name))

    if feature_type in ["CDS", "exon"]:
        transcript_id = attribute_dict["transcript_id"].strip('"')
        gene_id = attribute_dict["gene_id"].strip('"')
        gene_name = attribute_dict["gene_name"].strip('"')
        features["coding_exons"].append((row[0], row[3] - 1, row[4], transcript_id, gene_id, gene_name))

    if feature_type == "5UTR":
        transcript_id = attribute_dict["transcript_id"].strip('"')
        gene_id = attribute_dict["gene_id"].strip('"')
        gene_name = attribute_dict["gene_name"].strip('"')
        features["5UTR"].append((row[0], row[3] - 1, row[4], transcript_id, gene_id, gene_name))

    if feature_type == "3UTR":
        transcript_id = attribute_dict["transcript_id"].strip('"')
        gene_id = attribute_dict["gene_id"].strip('"')
        gene_name = attribute_dict["gene_name"].strip('"')
        features["3UTR"].append((row[0], row[3] - 1, row[4], transcript_id, gene_id, gene_name))

# Group intron coordinates by transcript ID
intron_coords = {}
for row in gtf_df.itertuples(index=False, name=None):
    feature_type = row[2]

    if feature_type == "exon":
        attributes = row[8]
        attribute_dict = dict(item.strip().split() for item in attributes.split(';') if item.strip())
        transcript_id = attribute_dict["transcript_id"].strip('"')
        gene_id = attribute_dict["gene_id"].strip('"')
        gene_name = attribute_dict["gene_name"].strip('"')

        if transcript_id not in intron_coords:
            intron_coords[transcript_id] = [(row[0], row[3] - 1, row[4], transcript_id, gene_id, gene_name)]
        else:
            intron_coords[transcript_id].append((row[0], row[3] - 1, row[4], transcript_id, gene_id, gene_name))

# Calculate introns based on exons
for transcript_id, exon_list in intron_coords.items():
    exon_list.sort(key=lambda x: x[1])
    intron_coords[transcript_id] = []
    for i in range(len(exon_list) - 1):
        intron_start = exon_list[i][2]  # End of current exon
        intron_end = exon_list[i + 1][1]  # Start of next exon
        intron_coords[transcript_id].append(
            (exon_list[i][0], intron_start, intron_end, transcript_id, exon_list[i][4], exon_list[i][5]))

# Save features to individual BED files
for feature_type, feature_data in features.items():
    if not feature_data:
        continue

    #bed_columns = ["Chromosome", "Start", "End", "FeatureID", "GeneID", "GeneName"]
    bed_df = pd.DataFrame(feature_data) # , columns=bed_columns

    output_file = f"{feature_type}.bed"
    bed_df.to_csv(output_folder + "/" + output_file, sep='\t', index=False, header=False)


# ### Task 1: Using an external BED file provided (T1.bed), map and match its regions to the features extracted above. Save the results in a separate file and append a column indicating the corresponding feature type (e.g., exon, 5UTR, 3UTR, intron and UN for non-mapped).

# In[7]:


import pandas as pd

# Read the input BED files into pandas DataFrames
genes_df = pd.read_csv("genes.bed", sep='\t', header=None)    # need to change the file genes names generates from prev
transcripts_df = pd.read_csv("transcripts.bed", sep='\t', header=None)   # need to change the file transcripts names generates from prev
coding_exons_df = pd.read_csv("coding_exons1.bed", sep='\t', header=None)    # need to change the file coding_exons names generates from prev
bed_df = pd.read_csv("T1.bed", sep='\t', header=None)


# Function to map and match features
def map_and_match_features(bed_df, features_df, feature_type):
    mapped_regions = []
    for index, bed_row in bed_df.iterrows():
        chrom, start, end, strand = bed_row[0], bed_row[1], bed_row[2], bed_row[3]
        mapped_feature = None

        for index, feature_row in features_df.iterrows():
            feature_start, feature_end = feature_row[1], feature_row[2]
            if feature_start <= start < feature_end or feature_start < end <= feature_end:
                mapped_feature = feature_row
                break

        if mapped_feature is not None:
            mapped_regions.append(list(bed_row) + [feature_type] + list(mapped_feature[3:]))
        else:
            mapped_regions.append(list(bed_row) + [feature_type] + [None] * (features_df.shape[1] - 3))

    return mapped_regions

print("process start")
# Map and match regions to genes, transcripts, and coding exons
mapped_genes = map_and_match_features(bed_df, genes_df, 'exon')
mapped_transcripts = map_and_match_features(bed_df, transcripts_df, 'transcript')
mapped_coding_exons = map_and_match_features(bed_df, coding_exons_df, 'coding_exon')
print("process end")

# Combine results and create a DataFrame
mapped_regions = mapped_genes + mapped_transcripts + mapped_coding_exons
result_df = pd.DataFrame(mapped_regions) # ,columns=["Chrom", "Start", "End", "Strand", "FeatureType", "FeatureChrom", "FeatureStart",
                                #  "FeatureEnd", "FeatureStrand"]

# Save the results to a separate file
result_df.to_csv("mapped_regions_output.bed", sep='\t', index=False, header=True)


# In[ ]:




