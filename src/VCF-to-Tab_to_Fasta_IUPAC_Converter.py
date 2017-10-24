#!/usr/bin/python

def usage():
    print("""
    This script is intended for modifying files from vcftools that contain 
    biallelic information and convert them to fasta format. After the vcf file has
    been exported using the vcf-to-tab program from VCFTools, this script will 
    change biallelic information at each site to only one nucleotide using UIPAC 
    conventions when the alleles are different (heterozygous) or to the available
    nucleotide if both alleles are the same. If one alle is present and the other 
    one is missing, the script will change the site to the available allele. 
    All of these changes will be saved to a new file in fasta format.
    
    written by Simon Uribe-Convers - www.simonuribe.com
    October 23rd, 2017
    
    To use this script, type: python3.6 VCF-to-Tab_to_Fasta_IUPAC_Converter.py VCF-to-Tab_file Output_file
    """)


import sys
import __future__

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        print("~~~~Error~~~~\n\nCorrect usage: python3.6 "+sys.argv[0]+" VCF-to-Tab file + Output file")
        sys.exit("Missing either the VCF-to-Tab and/or the output files!")

filename = open(sys.argv[1], "r")
# filename = open("VCF_to_Tab.txt", "rU")
outfile = open(sys.argv[2] + ".fasta", "w")
# outfile = open("VCF_to_Tab_out.txt", "w")

# def IUPAC_converter(filename, outfile):
IUPAC_Codes = { "G/G" : "G", "C/C" : "C", "T/T" : "T", "A/A" : "A", 
"-/G" : "G", "-/C" : "C", "-/T" : "T", "-/A" : "A", "G/-" : "G", 
"C/-" : "C", "T/-" : "T", "A/-" : "A", "G/T" : "K", "T/G" : "K", 
"A/C" : "M", "C/A" : "M", "C/G" : "S", "G/C" : "S", "A/G" : "R", 
"G/A" : "R", "A/T" : "W", "T/A" : "W", "C/T" : "Y", "T/C" : "Y", 
"./." : "N", "-/-" : "N", "N/N" : "N", "-/N" : "N", "N/-" : "N", 
"N/." : "N", "./N" : "N"
}

for line in filename:
    species_name = line.strip().split(" ")[0]
    data = line.strip().split(" ")[1:]
    new_data = [IUPAC_Codes[i] for i in data]
    # print(new_data)
    new_data2 = "".join(new_data)
    outfile.write(">" + species_name + "\n" + new_data2 + "\n")


    
# IUPAC_CODES = {
# "R": {"A":"G", "G":"A"},
# "Y": {"C":"T", "T":"C"},
# "S": {"G":"C", "C":"G"},
# "W": {"A":"T", "T":"A"},
# "K": {"G":"T", "T":"G"},
# "M": {"A":"C", "C":"A"},
# }
