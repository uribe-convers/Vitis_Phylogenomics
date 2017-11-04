"""This script will take two files. The first one is a file with two 
columns, 1) the original name (pattern1) of the sample (usually long and uninformative) 
and 2) the name (pattern2) you want to replace it with. The two values must be 
separated by a comma. The second file is the data that came out of VCFTools (or
any other string) using the vcf-to-tab command. You'll also provide a filename 
to write the results.

Simon Uribe-Convers - November 3rd, 2017 - http://simonuribe.com"""

import sys
import os
import __future__


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("~~~~Error~~~~\n\nCorrect usage: python3.6 "+sys.argv[0]+" .csv file + + vcf-to-tab file + output file")
        sys.exit("Missing arguments!")
        
infile = open(sys.argv[1], "r")
data_file = open(sys.argv[2], "r")
outfile = open(sys.argv[3], "w")

# infile = open("All_Names.csv", "r")
# data_file = open("Basal_mod_biallele_depth_missing_indv.recode_vcf_to_tab.txt", "r")
# outfile = open("test.txt", "w")

# Create dictionary with old names as keys and new names as values
name_dic = {}
name_to_change = []
for line in infile:
    old_name = line.strip().split(",")[0]
    new_name = line.strip().split(",")[1]
    name_to_change.append(line.strip().split(",")[0])
    
    if old_name not in name_dic:
        name_dic[old_name] = new_name

# new_names = [name_dic[i] for i in name_to_change]

# Function to seacrh and replace all key for values in the dictionary
def replace_all(text, dic):
    for i, j in iter(dic.items()):
        text = text.replace(i, j)
    return text

# Read in data
data = data_file.read()


data_new_names = replace_all(data, name_dic)

outfile.write(data_new_names)
