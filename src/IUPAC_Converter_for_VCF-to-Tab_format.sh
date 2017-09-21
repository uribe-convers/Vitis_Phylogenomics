#This script is intended for modifying files from vcftools that contain allelic
#information. After the vcf file has been exported using the vcf-to-tab program, this
#script will change allelic information at each site to only one nucleotide using UIPAC
#conventions when the alleles are different. If one alle is present and the other one is
#missing, the script will change the site to the available allele.
#All of these changes will be saved in a new file.


#written by Simon Uribe-Convers - www.simonuribe.com
#March 18, 2016

#!/bin/bash

echo "Enter filename:"
read filename

echo "Enter the name for the modified file"
read name

sed 's/:/_/g' $filename > $name
sed -i "" 's/#//g' $name
sed -i "" 's/"//g' $name

sed -i "" 's/A\/-/A/g' $name
sed -i "" 's/C\/-/C/g' $name
sed -i "" 's/G\/-/G/g' $name
sed -i "" 's/T\/-/T/g' $name
sed -i "" 's/-\/A/A/g' $name
sed -i "" 's/-\/C/C/g' $name
sed -i "" 's/-\/G/G/g' $name
sed -i "" 's/-\/T/T/g' $name
sed -i "" 's/A\/G/R/g' $name
sed -i "" 's/C\/T/Y/g' $name
sed -i "" 's/G\/C/S/g' $name
sed -i "" 's/A\/T/W/g' $name
sed -i "" 's/G\/T/K/g' $name
sed -i "" 's/A\/C/M/g' $name
sed -i "" 's/G\/A/R/g' $name
sed -i "" 's/T\/C/Y/g' $name
sed -i "" 's/C\/G/S/g' $name
sed -i "" 's/T\/A/W/g' $name
sed -i "" 's/T\/G/K/g' $name
sed -i "" 's/C\/A/M/g' $name
sed -i "" 's/A\/A/A/g' $name
sed -i "" 's/C\/C/C/g' $name
sed -i "" 's/G\/G/G/g' $name
sed -i "" 's/T\/T/T/g' $name
sed -i "" 's/N\/N/N/g' $name
sed -i "" 's/\.\/\./N/g' $name
sed -i "" 's/-\/-/N/g' $name
sed -i "" 's/-/N/g' $name

sed -i "" 's/¿//g' $name
echo ""
echo "Finished"
