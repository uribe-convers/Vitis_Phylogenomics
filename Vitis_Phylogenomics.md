# Vitis Phylogenomics with GBS Data
**Simon Uribe-Convers - June 13th 2017 - [http://simonuribe.com](http://simonuribe.com)**

---
*Disclaimer:* This commands work on a Mac or other Linus/UNIX based computer. 

---


## Commands used to transform VCF to Fasta for Phylogenetics


In general:

- To get the data from VCFTools in the vcf-to-tab format:  

 ```
  -vcf-to-tab < file.vcf > file.txt
 # For Vitis
 vcf-to-tab < Basal_mod_biallele_depth_missing_indv.recode.vcf > Basal_mod_biallele_depth_missing_indv.recode_vcf_to_tab.txt
vcf-to-tab < Final.recode.vcf > Final.recode_vcf_to_tab.txt 
vcf-to-tab < NOAMP_dataset.vcf > NOAMP_dataset_vcf_to_tab.txt
```
 
- Check if there is a '#' on the first line with the headers, if there is one DELETE it!  

- Transpose tab file (either in excel or in R)  
	In R:
	
	```
	x <- read.table("NOAMP_dataset_tab.txt", header = T)  
	y <- t(x)  
	write.table(y, file="NOAMP_dataset_tab_transposed.txt", row.names = T, quote = F)
	```
- Delete the four first lines of the file (if transposed with Excel, delete the first three lines), i.e., delete everything on top of the first sample.

## From biallelic to single alleles

The data from VCF comes with information from both alleles, i.e., A and G at a site, and we need to modify it so that there is only one base per site. We'll use IUPAC ambiguous coding for sites that have different nucleotides. I wrote a python script to do this changes easily. **After the file has been transposed in R or Excel**, simply run the `VCF-to-Tab_to_Fasta_IUPAC_Converter.py` script by tying: `python VCF-to-Tab_to_Fasta_IUPAC_Converter.py VCF-toTab_file Output_file`

## Changing names of raw reads to more useful names

The names of the sequences were not very useful so we changed them to something more informative. The samples had names that were not standardized and we had to do some search and replace to make them have the same format across the samples.

To do this, we created a comma separated value (.csv) file with the long, uninformative name followed by the new, standardized name. With this file, the vcf-to-tab file, and the script  `Replace_Many_Patterns.py`, we were able to change them all. 

To run it, type: `python3.6 Replace_Many_Patterns.py .csv file + + vcf-to-tab file + output file` 

## Making data matrices for phylogenetic analyses

The following programs are essential while working with DNA sequences. Both of them deal with format conversion (e.g., fasta to nexus) or concatenation very smoothly. These programs are:

Download and install [Phyutility](https://code.google.com/archive/p/phyutility/downloads) to do file format conversion. **Update:** The new program [phyx](https://github.com/FePhyFoFum/phyx) does everything that Phyutility does but much much efficiently. 

Download and install [NCLconverter](http://ncl.sourceforge.net) for further file format conversion.

You'll end up with your data in fasta, Nexus, and Phylip.

Starting from a fasta file:

```
# To get a Nexus file
phyutility -concat -in infile.fasta -out outfile.nex

# To get a Phylip file
NCLconverter infile.nex -erelaxedphylip -ofileout

```

## Running RAxML

Use the Phylip file to run RAxML

```
module load raxml

# See what version of RAxML is available

raxmlHPC-PTHREADS-SSE3 -T [number of processors] -f a -m GTRCAT -x 5678 -p 9876 -# [bootstrap number, can also use autoMRE to let RAxML decide when to stop bootstrapping] -s [infile] -n [name]
```


## Running BEAST2 and SNAPP on the Cluster

You need to use the Nexus file in BEAUTi to create an .xml file to run BEAST2. In BEAUTi, check if you have the package SNAPP installed. Go to: File/Manage Packages/ and install it if you don't have it. 

After it's installed, go to File/Template/SNAPP
Then: File/Add Alignment

Select your species identifier
Go through the menus (most of the default values are ok!)

Save your XML file.

Then run that XML in BEAST2.

If using the cluster:

```bash
screen -S Vitis_Accession

module load beast/2.4.5

# If you get an error saying that SNAPP is not available:
addonmanager -add SNAPP 

beast -beagle -beagle_CPU -beagle_SSE -beagle_GPU -threads 16 Basal_mod_biallele_depth_missing_indv.recode_vcf_to_tab_Names_transposed_Ready_IUPAC_No_Accession.xml > info_Vitis_Species_Tree.log

beast -beagle -beagle_CPU -beagle_SSE -beagle_GPU -threads 16 Basal_mod_biallele_depth_missing_indv.recode_vcf_to_tab_Names_transposed_Ready_IUPAC_No_Accession_REDUCED.xml > info_Vitis_SNAPP_Reduced_Dataset.log

```

## Running SVDquartets

Start with a file with all loci (SNPs) concatenated into a NEXUS file, you will use this in Paup.

**If working with a single individual per species, you can skip the following few paragraphs**  

SVDquartets allows for multiple individuals from the same species to be included in the analysis, and those individuals and their information, will be combined into the taxon they belong to. For this to work however, you need to include a taxon block on your NEXUS file specifying which samples belong to which species. It should start with the species name, followed by a colon, the lines the individuals are located (or the range of lines) and a comma. Here is an example:

```
begin sets;
taxpartition species =
sp1: 1-4,
sp2: 5,
sp3: 6-7,
;
END;

``` 
This is easy to do for a few samples but if you have hundreds of individuals it becomes tedious very quickly. To make it a bit easier, use the R code below. **Note:** this code works on a *Phylip* file and not a *NEXUS*, so convert the NEXUS to Phylip using NCLconverter: `NCLconverter infile.nex -erelaxedphylip -ofileout`.


```{R}
### This script will format the settings file for SVDquartets
### It will parse a phylip file and output the line number in which each taxon is located. Then it will write how many
### occurrences a specific species has and the lines of each.
### This works best with species names separated by an underscore, and it will assume that there are no subspecies,
### i.e., only the first two parts of the name will be used.
### by Matthew Pennell, July 23 2014 - http://mwpennell.github.io/

## Read in and parse phylip file
phy.tab <- read.table(phylip.filename)
phy.tab <- as.character(phy.tab[-1,1])

## specific to my naming scheme using underscores
get.species.name <- function(x){
  tmp <- strsplit(x, split="_")
  paste(tmp[[1]][1], tmp[[1]][2], sep="_")
}

## Get species names 
sp.names <- as.character(sapply(phy.tab, function(x) get.species.name(x)))

## get identity of matches
sp.lab <- lapply(unique(sp.names), function(i) which(sp.names == i))
names(sp.lab) <- unique(sp.names)

## output to input file
sink("SVDquartets_settings.txt")
for (i in 1:length(sp.lab)){
	cat(paste(names(sp.lab)[i], length(sp.lab[[i]]), sep=" : "))
	cat("\n")
	cat("\t")
	cat(as.numeric(sp.lab[[i]]))
	cat("\n")

}
sink()
```
Once you have the location of every sample from the code above, modified the text slightly to match the correct format, i.e., put every occurrence in one line, add commas, etc. Finally, copy paste your sample-to-species information at the end of your concatenated NEXUS file and don't forget to include the few lines that the code above doesn't generate, see the format example above!

**Regardless of how many individuals you are working with:**

Now that we have the file ready, get the latest command-line version of [Paup](https://people.sc.fsu.edu/~dswofford/paup_test/) and type the following:

```
paup

#Within Paup

exe file.nex

#No Bootstrap (remove the square brackets and information within)
SVDQuartets nthreads=[number of processors] nquartets=[number of quartets] partition=species speciesTree=yes

#Save the tree
SaveTrees file = Vitis_SVDquartet_MR.tre format = Newick brLens = yes supportValues = Both trees = all

#With Bootstrap
SVDQuartets nthreads=8 nquartets=10000000 bootstrap=standard nreps=100 speciesTree=yes partition=species treeFile= Vitis_SVDquartet_Bootstrap_100.trees

```



