# Vitis Phylogenomics with GBS Data
**June 13th 2017**

---
*Disclaimer:* This commands work on a Mac or other UNIX based computer. 

---



## Commands used to transform VCF to Fasta for Phylogenetics

```bash
# General:

-vcf-to-tab < file.vcf > file.txt
-Check if there is a '#' on the first line with the headers, if there is one DELETE it!
-Transpose tab file (either in excel or in R)
	In R:
	x <- read.table("NOAMP_dataset_tab.txt", header = T)
	y <- t(x)
	write.table(y, file="NOAMP_dataset_tab_transposed.txt", row.names = T, quote = F)
-delete the four first lines of the file (if transposed with Excel, delete the first three lines). Delete everything on top of the first sample.

# Vitis Commands:

vcf-to-tab < Basal_mod_biallele_depth_missing_indv.recode.vcf > Basal_mod_biallele_depth_missing_indv.recode_vcf_to_tab.txt
vcf-to-tab < Final.recode.vcf > Final.recode_vcf_to_tab.txt 
vcf-to-tab < NOAMP_dataset.vcf > NOAMP_dataset_vcf_to_tab.txt
```

##Make fasta files

From the transposed datasets you'll need to create fasta files. This is done easily in a text editor with search and replace:


```
-replace: ^(\w+)
	for: >\1\r
-replace: "space" (an actual space key stroke)
	for: nothing
-save your file with ".fasta"

```

## From biallelic to single alleles

The data from VCF comes with information from both alleles, i.e., A and G at a site, and we need to modify it so that there is only one base per site. We'll use IUPAC ambiguous coding for sites that have different nucleotides.

Put the code below in a file, call it `IUPAC_Converter_for_VCF-to-Tab_format.sh`, and make it executable with `chmod 755 IUPAC_Converter_for_VCF-to-Tab_format.sh`.

Then run it with: `./IUPAC_Converter_for_VCF-to-Tab_format.sh`

```bash
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
```

## Changing names of raw reads to more useful names

The names of the sequences were not very useful so we changed them to something more informative. 

The samples had names that were not standardized and we had to do some search and replace to make then names have the same format across the samples.

The code below *should* change all the names, but double check to make sure!

Put the code below in a file, call it `Change_Names_Vitis.sh`, and make it executable with `chmod 755 Change_Names_Vitis.sh`.

Run it with `./Change_Names_Vitis.sh`

```
#!/bin/bash
#This will rename all the samples changing the original name from the sequencer to a meaningful name

#written by Simon Uribe-Convers - www.simonuribe.com
#April 28th, 2017


echo "Enter File to modify"
read filename

echo "Enter name of file to create"
read name


sed '1 s/1625_a_C2C7HACXX_8_250232525/Ampelopsis_cordata_1625_a/g' $filename > $name
sed -i "" '1 s/1625_b_C2C7HACXX_8_250232526/Ampelopsis_cordata_1625_b/g' $name
sed -i "" '1 s/1626_a_C2C7HACXX_8_250232527/Ampelopsis_glandulosa_brevip_1626_a/g' $name
sed -i "" '1 s/1626_b_C2C7HACXX_8_250232528/Ampelopsis_glandulosa_brevip_1626_b/g' $name
sed -i "" '1 s/1626_c_C2C7HACXX_8_250232529/Ampelopsis_glandulosa_brevip_1626_c/g' $name
sed -i "" '1 s/1627_a_C2C7HACXX_8_250232530/Ampelopsis_delavayana_glabra_1627_a/g' $name
sed -i "" '1 s/1627_b_C2C7HACXX_8_250232531/Ampelopsis_delavayana_glabra_1627_b/g' $name
sed -i "" '1 s/1627_c_C2C7HACXX_8_250232532/Ampelopsis_delavayana_glabra_1627_c/g' $name
sed -i "" '1 s/1628_a_C2C7HACXX_8_250232533/Ampelopsis_glandulosa_brevip_1628_a/g' $name
sed -i "" '1 s/1628_b_C2C7HACXX_8_250232534/Ampelopsis_glandulosa_brevip_1628_b/g' $name
sed -i "" '1 s/1628_c_C2C7HACXX_8_250232535/Ampelopsis_glandulosa_brevip_1628_c/g' $name
sed -i "" '1 s/1664_b_MERGE/V_aestivalis_1664_c/g' $name
sed -i "" '1 s/1664_j_C2C9HACXX_3_250225625/V_aestivalis_1664_j/g' $name
sed -i "" '1 s/1665_a_C2C7HACXX_8_250232511/V_aestivalis_1665_a/g' $name
sed -i "" '1 s/1665_l_C2C7HACXX_8_250232522/V_aestivalis_1665_l/g' $name
sed -i "" '1 s/237621_C0TCDACXX_2_250088582/V_rupestris_237621/g' $name
sed -i "" '1 s/255189_C0TCDACXX_2_250088554/V_riparia_255189/g' $name
sed -i "" '1 s/271662_C0KDJACXX_1_250087458/V_rupestris_271662/g' $name
sed -i "" '1 s/279897_C0TCDACXX_2_250088436/V_riparia_279897/g' $name
sed -i "" '1 s/313922_C0TCDACXX_2_250088507/V_riparia_vinifera_313922/g' $name
sed -i "" '1 s/318684_C0TCDACXX_2_250088544/V_acerifolia_318684/g' $name
sed -i "" '1 s/483130_C0TCDACXX_2_250088617/V_labrusca_483130/g' $name
sed -i "" '1 s/483137_C0TCDACXX_2_250088605/V_aestivalis_bicolor_483137/g' $name
sed -i "" '1 s/483138_C0TCDACXX_2_250088558/V_aestivalis_bicolor_483138/g' $name
sed -i "" '1 s/483145_C0TCDACXX_2_250088420/V_labrusca_483145/g' $name
sed -i "" '1 s/483146_C0TCDACXX_2_250088444/V_labrusca_483146/g' $name
sed -i "" '1 s/483147_C0TCDACXX_2_250088432/V_labrusca_483147/g' $name
sed -i "" '1 s/483148_C0TCDACXX_2_250088468/V_labrusca_483148/g' $name
sed -i "" '1 s/483149_C0TCDACXX_2_250088503/V_labrusca_483149/g' $name
sed -i "" '1 s/483150_C0TCDACXX_2_250088467/V_labrusca_483150/g' $name
sed -i "" '1 s/483151_C0TCDACXX_2_250088469/V_labrusca_483151/g' $name
sed -i "" '1 s/483152_C0TCDACXX_2_250088419/V_labrusca_483152/g' $name
sed -i "" '1 s/483153_C0TCDACXX_2_250088479/V_labrusca_483153/g' $name
sed -i "" '1 s/483154_C0TCDACXX_2_250088443/V_labrusca_483154/g' $name
sed -i "" '1 s/483155_C0TCDACXX_2_250088431/V_labrusca_483155/g' $name
sed -i "" '1 s/483157_C0TCDACXX_2_250088492/V_labrusca_483157/g' $name
sed -i "" '1 s/483160_C0TCDACXX_2_250088480/V_labrusca_483160/g' $name
sed -i "" '1 s/483161_C0TCDACXX_2_250088502/V_labrusca_483161/g' $name
sed -i "" '1 s/483162_C0TCDACXX_2_250088457/V_labrusca_483162/g' $name
sed -i "" '1 s/483163_C0TCDACXX_2_250088456/V_labrusca_483163/g' $name
sed -i "" '1 s/483165_C0TCDACXX_2_250088602/V_riparia_483165/g' $name
sed -i "" '1 s/483166_C0KDJACXX_1_250087469/V_riparia_483166/g' $name
sed -i "" '1 s/483168_C0TCDACXX_2_250088601/V_riparia_483168/g' $name
sed -i "" '1 s/483169_C0TCDACXX_2_250088499/V_riparia_483169/g' $name
sed -i "" '1 s/483170_C0TCDACXX_2_250088626/V_riparia_483170/g' $name
sed -i "" '1 s/483171_C0TCDACXX_2_250088565/V_riparia_483171/g' $name
sed -i "" '1 s/483172_C0TCDACXX_2_250088614/V_riparia_483172/g' $name
sed -i "" '1 s/483174_C0TCDACXX_2_250088555/V_riparia_483174/g' $name
sed -i "" '1 s/483175_C0TCDACXX_2_250088567/V_riparia_483175/g' $name
sed -i "" '1 s/483176_C0TCDACXX_2_250088427/V_riparia_483176/g' $name
sed -i "" '1 s/483177_C0TCDACXX_2_250088428/V_riparia_483177/g' $name
sed -i "" '1 s/483181_C0TCDACXX_2_250088638/V_riparia_483181/g' $name
sed -i "" '1 s/483182_C0TCDACXX_2_250088591/V_riparia_483182/g' $name
sed -i "" '1 s/483185_C0TCDACXX_2_250088546/V_aestivalis_483185/g' $name
sed -i "" '1 s/495622_q_C2C9HACXX_3_250225394/V_riparia_495622_q/g' $name
sed -i "" '1 s/495622_C0KDJACXX_1_250087456/V_riparia_495622/g' $name
sed -i "" '1 s/588054_C0KDJACXX_1_250087445/V_riparia_588054/g' $name
sed -i "" '1 s/588060_C0TCDACXX_2_250088553/V_coignetiae_588060/g' $name
sed -i "" '1 s/588123_C2C9HACXX_3_250225304/V_spp_mustangensis_588123/g' $name
sed -i "" '1 s/588128_C0TCDACXX_2_250088477/V_labrusca_588128/g' $name
sed -i "" '1 s/588134_C0TCDACXX_2_250088574/V_cinerea_588134/g' $name
sed -i "" '1 s/588138_C0TCDACXX_2_250088501/V_labrusca_588138/g' $name
sed -i "" '1 s/588141_C0TCDACXX_2_250088556/V_acerifolia_588141/g' $name
sed -i "" '1 s/588143_C0TCDACXX_2_250088563/V_cinerea_588143/g' $name
sed -i "" '1 s/588144_C0TCDACXX_2_250088568/V_acerifolia_588144/g' $name
sed -i "" '1 s/588145_C0TCDACXX_2_250088441/V_labrusca_588145/g' $name
sed -i "" '1 s/588146_C0KDJACXX_1_250087446/V_rupestris_588146/g' $name
sed -i "" '1 s/588147_C0KDJACXX_1_250087410/V_rupestris_588147/g' $name
sed -i "" '1 s/588152_C0TCDACXX_2_250088482/V_spp_rubra_588152/g' $name
sed -i "" '1 s/588154_C0TCDACXX_2_250088621/V_cinerea_588154/g' $name
sed -i "" '1 s/588155_C0TCDACXX_2_250088470/V_palmata_588155/g' $name
sed -i "" '1 s/588160_C0KDJACXX_1_250087482/V_rupestris_588160/g' $name
sed -i "" '1 s/588164_C0TCDACXX_2_250088429/V_labrusca_588164/g' $name
sed -i "" '1 s/588165_C0TCDACXX_2_250088417/V_labrusca_588165/g' $name
sed -i "" '1 s/588167_C0TCDACXX_2_250088495/V_riparia_588167/g' $name
sed -i "" '1 s/588169_C0TCDACXX_2_250088418/V_labrusca_588169/g' $name
sed -i "" '1 s/588181_C0KDJACXX_1_250087434/V_rupestris_588181/g' $name
sed -i "" '1 s/588182_C0TCDACXX_2_250088465/V_labrusca_588182/g' $name
sed -i "" '1 s/588186_C0TCDACXX_2_250088562/V_cinerea_588186/g' $name
sed -i "" '1 s/588188_C0KDJACXX_1_250087470/V_rupestris_588188/g' $name
sed -i "" '1 s/588190_C0TCDACXX_2_250088471/V_riparia_588190/g' $name
sed -i "" '1 s/588194_C0TCDACXX_2_250088455/V_labrusca_588194/g' $name
sed -i "" '1 s/588197_C0TCDACXX_2_250088609/V_cinerea_588197/g' $name
sed -i "" '1 s/588198_C0TCDACXX_2_250088561/V_cinerea_588198/g' $name
sed -i "" '1 s/588199_C0TCDACXX_2_250088596/V_cinerea_588199/g' $name
sed -i "" '1 s/588200_C0TCDACXX_2_250088573/V_cinerea_588200/g' $name
sed -i "" '1 s/588201_C0TCDACXX_2_250088494/V_palmata_588201/g' $name
sed -i "" '1 s/588204_C0TCDACXX_2_250088483/V_riparia_588204/g' $name
sed -i "" '1 s/588205_C0TCDACXX_2_250088620/V_cinerea_helleri_588205/g' $name
sed -i "" '1 s/588208_C0TCDACXX_2_250088586/V_cinerea_588208/g' $name
sed -i "" '1 s/588210_C0TCDACXX_2_250088608/V_cinerea_helleri_588210/g' $name
sed -i "" '1 s/588214_C0TCDACXX_2_250088459/V_riparia_588214/g' $name
sed -i "" '1 s/588217_C0TCDACXX_2_250088610/V_cinerea_588217/g' $name
sed -i "" '1 s/588218_C0TCDACXX_2_250088598/V_cinerea_588218/g' $name
sed -i "" '1 s/588220_C0TCDACXX_2_250088585/V_cinerea_588220/g' $name
sed -i "" '1 s/588222_C0TCDACXX_2_250088549/V_cinerea_588222/g' $name
sed -i "" '1 s/588225_C0KDJACXX_1_250087483/V_rupestris_588225/g' $name
sed -i "" '1 s/588227_C0KDJACXX_1_250087460/V_rupestris_588227/g' $name
sed -i "" '1 s/588228_C2C9HACXX_3_250225327/V_rupestris_588228/g' $name
sed -i "" '1 s/588229_C0KDJACXX_1_250087435/V_rupestris_588229/g' $name
sed -i "" '1 s/588230_C0KDJACXX_1_250087447/V_rupestris_588230/g' $name
sed -i "" '1 s/588231_C0KDJACXX_1_250087459/V_rupestris_588231/g' $name
sed -i "" '1 s/588233_C0TCDACXX_2_250088506/V_palmata_588233/g' $name
sed -i "" '1 s/588258_C0TCDACXX_2_250088486/V_riparia_588258/g' $name
sed -i "" '1 s/588259_C0TCDACXX_2_250088438/V_riparia_588259/g' $name
sed -i "" '1 s/588260_C0TCDACXX_2_250088497/V_riparia_588260/g' $name
sed -i "" '1 s/588261_C0TCDACXX_2_250088426/V_riparia_588261/g' $name
sed -i "" '1 s/588262_C0TCDACXX_2_250088473/V_riparia_588262/g' $name
sed -i "" '1 s/588269_C0TCDACXX_2_250088498/V_riparia_588269/g' $name
sed -i "" '1 s/588270_C0TCDACXX_2_250088450/V_riparia_588270/g' $name
sed -i "" '1 s/588271_C0TCDACXX_2_250088625/V_riparia_588271/g' $name
sed -i "" '1 s/588272_C0TCDACXX_2_250088462/V_riparia_588272/g' $name
sed -i "" '1 s/588273_C0TCDACXX_2_250088578/V_riparia_588273/g' $name
sed -i "" '1 s/588274_C0TCDACXX_2_250088613/V_riparia_588274/g' $name
sed -i "" '1 s/588275_C0KDJACXX_1_250087444/V_riparia_588275/g' $name
sed -i "" '1 s/588276_C0TCDACXX_2_250088637/V_riparia_588276/g' $name
sed -i "" '1 s/588282_C2C9HACXX_3_250225303/V_spp_588282/g' $name
sed -i "" '1 s/588304_C0TCDACXX_2_250088484/V_riparia_588304/g' $name
sed -i "" '1 s/588307_C0KDJACXX_1_250087467/V_labrusca_588307/g' $name
sed -i "" '1 s/588324_C0TCDACXX_2_250088604/V_acerifolia_588324/g' $name
sed -i "" '1 s/588325_C0TCDACXX_2_250088616/V_acerifolia_588325/g' $name
sed -i "" '1 s/588328_C0TCDACXX_2_250088551/V_cinerea_588328/g' $name
sed -i "" '1 s/588329_C0TCDACXX_2_250088599/V_cinerea_588329/g' $name
sed -i "" '1 s/588330_C0KDJACXX_1_250087448/V_rupestris_588330/g' $name
sed -i "" '1 s/588331_C0KDJACXX_1_250087496/V_rupestris_588331/g' $name
sed -i "" '1 s/588333_C0KDJACXX_1_250087495/V_rupestris_588333/g' $name
sed -i "" '1 s/588335_C0KDJACXX_1_250087422/V_rupestris_588335/g' $name
sed -i "" '1 s/588344_C0TCDACXX_2_250088448/V_riparia_588344/g' $name
sed -i "" '1 s/588345_C0TCDACXX_2_250088451/V_riparia_588345/g' $name
sed -i "" '1 s/588346_C0TCDACXX_2_250088439/V_riparia_588346/g' $name
sed -i "" '1 s/588347_C0TCDACXX_2_250088496/V_riparia_588347/g' $name
sed -i "" '1 s/588349_C0TCDACXX_2_250088485/V_riparia_588349/g' $name
sed -i "" '1 s/588350_C0TCDACXX_2_250088474/V_riparia_588350/g' $name
sed -i "" '1 s/588352_C0TCDACXX_2_250088632/V_cinerea_588352/g' $name
sed -i "" '1 s/588353_C0TCDACXX_2_250088463/V_riparia_588353/g' $name
sed -i "" '1 s/588354_C0TCDACXX_2_250088472/V_riparia_588354/g' $name
sed -i "" '1 s/588355_C0KDJACXX_1_250087484/V_rupestris_588355/g' $name
sed -i "" '1 s/588356_C0TCDACXX_2_250088633/V_cinerea_588356/g' $name
sed -i "" '1 s/588369_C0TCDACXX_2_250088510/V_riparia_588369/g' $name
sed -i "" '1 s/588372_C0TCDACXX_2_250088587/V_cinerea_588372/g' $name
sed -i "" '1 s/588373_C0TCDACXX_2_250088508/V_riparia_588373/g' $name
sed -i "" '1 s/588374_C0TCDACXX_2_250088425/V_riparia_588374/g' $name
sed -i "" '1 s/588385_C0TCDACXX_2_250088584/V_amurensis_588385/g' $name
sed -i "" '1 s/588393_C0TCDACXX_2_250088592/V_acerifolia_588393/g' $name
sed -i "" '1 s/588395_C0KDJACXX_1_250087423/V_rupestris_588395/g' $name
sed -i "" '1 s/588398_C0TCDACXX_2_250088634/V_cinerea_588398/g' $name
sed -i "" '1 s/588399_C0TCDACXX_2_250088594/V_spp_588399/g' $name
sed -i "" '1 s/588400_C0TCDACXX_2_250088460/V_riparia_588400/g' $name
sed -i "" '1 s/588404_C0TCDACXX_2_250088424/V_riparia_588404/g' $name
sed -i "" '1 s/588406_C0TCDACXX_2_250088509/V_riparia_588406/g' $name
sed -i "" '1 s/588415_C0KDJACXX_1_250087411/V_rupestris_588415/g' $name
sed -i "" '1 s/588420_c_C2C9HACXX_3_250225496/V_amurensis_588420_c/g' $name
sed -i "" '1 s/588421_a_C2C9HACXX_3_250225363/V_yenshanensis_588421_a/g' $name
sed -i "" '1 s/588421_g_C2C9HACXX_3_250225369/V_yenshanensis_588421_g/g' $name
sed -i "" '1 s/588422_a_C2C9HACXX_3_250225468/V_yenshanensis_588422_a/g' $name
sed -i "" '1 s/588435_C0TCDACXX_2_250088475/V_riparia_588435/g' $name
sed -i "" '1 s/588436_C0TCDACXX_2_250088461/V_riparia_588436/g' $name
sed -i "" '1 s/588437_C0TCDACXX_2_250088449/V_riparia_588437/g' $name
sed -i "" '1 s/588438_C0TCDACXX_2_250088437/V_riparia_588438/g' $name
sed -i "" '1 s/588439_C0TCDACXX_2_250088589/V_riparia_588439/g' $name
sed -i "" '1 s/588440_C0TCDACXX_2_250088566/V_riparia_588440/g' $name
sed -i "" '1 s/588441_C2C9HACXX_3_250225305/V_spp_588441/g' $name
sed -i "" '1 s/588442_C0TCDACXX_2_250088580/V_acerifolia_588442/g' $name
sed -i "" '1 s/588444_a_C2C9HACXX_3_250225457/V_cinerea_helleri_588444_a/g' $name
sed -i "" '1 s/588445_a_C2C9HACXX_3_250225460/V_cinerea_helleri_588445_a/g' $name
sed -i "" '1 s/588446_b_C2C9HACXX_3_250225577/V_cinerea_588446_b/g' $name
sed -i "" '1 s/588447_a_C2C9HACXX_3_250225476/V_cinerea_588447_a/g' $name
sed -i "" '1 s/588448_c_C2C9HACXX_3_250225486/V_acerifolia_588448_c/g' $name
sed -i "" '1 s/588448_d_C2C9HACXX_3_250225487/V_acerifolia_588448_d/g' $name
sed -i "" '1 s/588450_b_C2C9HACXX_3_250225490/V_riparia_588450_b/g' $name
sed -i "" '1 s/588451_e_C2C9HACXX_3_250225482/V_cignetiae_588451_e/g' $name
sed -i "" '1 s/588453_b_C2C9HACXX_3_250225479/V_riparia_588453_b/g' $name
sed -i "" '1 s/588454_g_C2C9HACXX_3_250225499/V_rupestris_588454_g/g' $name
sed -i "" '1 s/588454_o_C2C9HACXX_3_250225580/V_rupestris_588454_o/g' $name
sed -i "" '1 s/588455_C0TCDACXX_2_250088590/V_riparia_588455/g' $name
sed -i "" '1 s/588456_C0TCDACXX_2_250088577/V_riparia_588456/g' $name
sed -i "" '1 s/588458_a_C2C9HACXX_3_250225431/V_acerifolia_588458_a/g' $name
sed -i "" '1 s/588459_C0TCDACXX_2_250088593/V_acerifolia_588459/g' $name
sed -i "" '1 s/588460_C0TCDACXX_2_250088588/V_cinerea_588460/g' $name
sed -i "" '1 s/588465_C0TCDACXX_2_250088435/V_piasezkii_588465/g' $name
sed -i "" '1 s/588466_C0TCDACXX_2_250088622/V_cinerea_helleri_588466/g' $name
sed -i "" '1 s/588467_C0TCDACXX_2_250088423/V_spp_588467/g' $name
sed -i "" '1 s/588483_C0TCDACXX_2_250088579/V_riparia_588483/g' $name
sed -i "" '1 s/588501_C2C9HACXX_3_250225308/V_spp_588501/g' $name
sed -i "" '1 s/588508_C2C9HACXX_3_250225306/V_spp_588508/g' $name
sed -i "" '1 s/588510_C0KDJACXX_1_250087457/V_riparia_588510/g' $name
sed -i "" '1 s/588529_C2C9HACXX_3_250225310/V_spp_588529/g' $name
sed -i "" '1 s/588540_C0KDJACXX_1_250087481/V_rupestris_OPseedling_588540/g' $name
sed -i "" '1 s/588549_C2C9HACXX_3_250225307/V_spp_588549/g' $name
sed -i "" '1 s/588562_C0TCDACXX_2_250088440/V_riparia_588562/g' $name
sed -i "" '1 s/588564_C0TCDACXX_2_250088487/V_riparia_labHyb_588564/g' $name
sed -i "" '1 s/588574_C0KDJACXX_1_250087493/V_rupestris_588574/g' $name
sed -i "" '1 s/588575_C0TCDACXX_2_250088611/V_cinerea_588575/g' $name
sed -i "" '1 s/588583_C0TCDACXX_2_250088434/V_labrusca_588583/g' $name
sed -i "" '1 s/588584_C0TCDACXX_2_250088433/V_labrusca_588584/g' $name
sed -i "" '1 s/588585_C0TCDACXX_2_250088504/V_labrusca_588585/g' $name
sed -i "" '1 s/588586_C0KDJACXX_1_250087468/V_riparia_588586/g' $name
sed -i "" '1 s/588588_b_C2C9HACXX_3_250225596/V_riparia_588588_b/g' $name
sed -i "" '1 s/588588_i_C2C9HACXX_3_250225603/V_riparia_588588_i/g' $name
sed -i "" '1 s/588589_b_C2C9HACXX_3_250225582/V_vulpina_588589_b/g' $name
sed -i "" '1 s/588590_b_C2C9HACXX_3_250225524/V_riparia_588590_b/g' $name
sed -i "" '1 s/588591_a_C2C9HACXX_3_250225503/V_vulpina_588591_a/g' $name
sed -i "" '1 s/588592_a_C2C9HACXX_3_250225619/Ampelopsis_glandulosa_588592_a/g' $name
sed -i "" '1 s/588592_b_C2C9HACXX_3_250225620/Ampelopsis_glandulosa_588592_b/g' $name
sed -i "" '1 s/588625_C0TCDACXX_2_250088564/V_cinerea_helleri_588625/g' $name
sed -i "" '1 s/588626_C0TCDACXX_2_250088629/V_aestivalis_588626/g' $name
sed -i "" '1 s/588628_C2C9HACXX_3_250225309/V_spp_588628/g' $name
sed -i "" '1 s/588632_C0TCDACXX_2_250088631/V_amurensis_588632/g' $name
sed -i "" '1 s/588633_C0TCDACXX_2_250088548/V_amurensis_588633/g' $name
sed -i "" '1 s/588634_C0TCDACXX_2_250088618/V_amurensis_588634/g' $name
sed -i "" '1 s/588636_C0TCDACXX_2_250088619/V_amurensis_588636/g' $name
sed -i "" '1 s/588637_C0TCDACXX_2_250088630/V_amurensis_588637/g' $name
sed -i "" '1 s/588639_C0TCDACXX_2_250088547/V_amurensis_588639/g' $name
sed -i "" '1 s/588640_C0TCDACXX_2_250088595/V_amurensis_588640/g' $name
sed -i "" '1 s/588641_C0TCDACXX_2_250088607/V_amurensis_588641/g' $name
sed -i "" '1 s/588642_C0TCDACXX_2_250088612/V_coignetiae_588642/g' $name
sed -i "" '1 s/588644_C0TCDACXX_2_250088624/V_coignetiae_588644/g' $name
sed -i "" '1 s/588647_C0TCDACXX_2_250088493/V_labrusca_588647/g' $name
sed -i "" '1 s/588650_a_C2C9HACXX_3_250225621/V_yenshanensis_588650_a/g' $name
sed -i "" '1 s/588653_C0KDJACXX_1_250087421/V_riparia_588653/g' $name
sed -i "" '1 s/588658_C0TCDACXX_2_250088422/V_labrusca_588658/g' $name
sed -i "" '1 s/588675_C0TCDACXX_2_250088505/V_labrusca_588675/g' $name
sed -i "" '1 s/588677_C0TCDACXX_2_250088570/V_aestivalis_588677/g' $name
sed -i "" '1 s/588678_C0TCDACXX_2_250088623/V_cinerea_588678/g' $name
sed -i "" '1 s/588685_C0TCDACXX_2_250088576/V_cinerea_588685/g' $name
sed -i "" '1 s/588688_a_C2C7HACXX_8_250232536/V_cinerea_588688_a/g' $name
sed -i "" '1 s/588710_C0KDJACXX_1_250087433/V_riparia_588710/g' $name
sed -i "" '1 s/588711_C0KDJACXX_1_250087492/V_riparia_588711/g' $name
sed -i "" '1 s/588715_C2C9HACXX_3_250225312/V_spp_588715/g' $name
sed -i "" '1 s/588718_C0KDJACXX_1_250087480/V_riparia_588718/g' $name
sed -i "" '1 s/594344_C0KDJACXX_1_250087409/V_riparia_594344/g' $name
sed -i "" '1 s/594348_C2C9HACXX_3_250225319/V_spp_594348/g' $name
sed -i "" '1 s/594349_C0TCDACXX_2_250088446/V_labrusca_594349/g' $name
sed -i "" '1 s/597104_C0TCDACXX_2_250088489/V_labrusca_597104/g' $name
sed -i "" '1 s/597172_C0KDJACXX_1_250087455/V_labrusca_597172/g' $name
sed -i "" '1 s/597228_C0TCDACXX_2_250088430/V_labrusca_597228/g' $name
sed -i "" '1 s/597232_C0TCDACXX_2_250088552/V_cinerea_597232/g' $name
sed -i "" '1 s/597257_C0TCDACXX_2_250088447/V_piasezkii_597257/g' $name
sed -i "" '1 s/597292_C2C9HACXX_3_250225317/V_spp_597292/g' $name
sed -i "" '1 s/597293_C2C9HACXX_3_250225315/V_spp_597293/g' $name
sed -i "" '1 s/597294_C2C9HACXX_3_250225320/V_spp_597294/g' $name
sed -i "" '1 s/597295_C2C9HACXX_3_250225313/V_spp_597295/g' $name
sed -i "" '1 s/597298_C2C9HACXX_3_250225316/V_spp_597298/g' $name
sed -i "" '1 s/Cabernet_Franc_C2C7HACXX_7_250232032/V_vinifera_Cabernet_Franc_250232032/g' $name
sed -i "" '1 s/Centennial_C2C7HACXX_7_250232029/V_vinifera_Centennial_250232029/g' $name
sed -i "" '1 s/Dornfelder_C2C7HACXX_7_250232025/V_vinifera_Dornfelder_250232025/g' $name
sed -i "" '1 s/DVIT1134_C0TCDACXX_2_250088346/V_mustangensis_DVIT1134/g' $name
sed -i "" '1 s/DVIT1156_2_C0TCDACXX_2_250088354/V_amurensis_DVIT1156_2/g' $name
sed -i "" '1 s/DVIT1268_C0KDJACXX_1_250087475/V_riparia_DVIT1268/g' $name
sed -i "" '1 s/DVIT1269_C0KDJACXX_1_250087426/V_arizonica_DVIT1269/g' $name
sed -i "" '1 s/DVIT1280_C0KDJACXX_1_250087418/V_vulpina_DVIT1280/g' $name
sed -i "" '1 s/DVIT1287_C0KDJACXX_1_250087465/V_acerifolia_DVIT1287/g' $name
sed -i "" '1 s/DVIT1288_C0KDJACXX_1_250087430/V_vulpina_DVIT1288/g' $name
sed -i "" '1 s/DVIT1290_C0KDJACXX_1_250087442/V_vulpina_DVIT1290/g' $name
sed -i "" '1 s/DVIT1292_C0KDJACXX_1_250087454/V_vulpina_DVIT1292/g' $name
sed -i "" '1 s/DVIT1294_C0KDJACXX_1_250087466/V_vulpina_DVIT1294/g' $name
sed -i "" '1 s/DVIT1296_C0KDJACXX_1_250087477/V_acerifolia_DVIT1296/g' $name
sed -i "" '1 s/DVIT1297_C0KDJACXX_1_250087489/V_acerifolia_DVIT1297/g' $name
sed -i "" '1 s/DVIT1299_C0KDJACXX_1_250087440/V_acerifolia_DVIT1299/g' $name
sed -i "" '1 s/DVIT1301_C0KDJACXX_1_250087478/V_vulpina_DVIT1301/g' $name
sed -i "" '1 s/DVIT1303_C0KDJACXX_1_250087462/V_monticola_DVIT1303/g' $name
sed -i "" '1 s/DVIT1369_C0TCDACXX_2_250088294/V_monticola_DVIT1369/g' $name
sed -i "" '1 s/DVIT1370_C0KDJACXX_1_250087474/V_monticola_DVIT1370/g' $name
sed -i "" '1 s/DVIT1371_C0KDJACXX_1_250087486/V_monticola_DVIT1371/g' $name
sed -i "" '1 s/DVIT1372_C0KDJACXX_1_250087403/V_monticola_DVIT1372/g' $name
sed -i "" '1 s/DVIT1376_C0KDJACXX_1_250087415/V_monticola_DVIT1376/g' $name
sed -i "" '1 s/DVIT1381_C0KDJACXX_1_250087490/V_vulpina_DVIT1381/g' $name
sed -i "" '1 s/DVIT1397_C0KDJACXX_1_250087452/V_acerifolia_DVIT1397/g' $name
sed -i "" '1 s/DVIT1399_C0KDJACXX_1_250087464/V_acerifolia_DVIT1399/g' $name
sed -i "" '1 s/DVIT1401_C0KDJACXX_1_250087476/V_acerifolia_DVIT1401/g' $name
sed -i "" '1 s/DVIT1403_C0KDJACXX_1_250087488/V_acerifolia_DVIT1403/g' $name
sed -i "" '1 s/DVIT1406_C0KDJACXX_1_250087428/V_rupestris_DVIT1406/g' $name
sed -i "" '1 s/DVIT1418_C0KDJACXX_1_250087405/V_rupestris_DVIT1418/g' $name
sed -i "" '1 s/DVIT1420_C0KDJACXX_1_250087417/V_rupestris_DVIT1420/g' $name
sed -i "" '1 s/DVIT1421_C0KDJACXX_1_250087429/V_rupestris_DVIT1421/g' $name
sed -i "" '1 s/DVIT1424_C0KDJACXX_1_250087487/V_riparia_DVIT1424/g' $name
sed -i "" '1 s/DVIT1425_C0KDJACXX_1_250087404/V_riparia_DVIT1425/g' $name
sed -i "" '1 s/DVIT1434_C0KDJACXX_1_250087416/V_riparia_DVIT1434/g' $name
sed -i "" '1 s/DVIT1435_C0KDJACXX_1_250087427/V_riparia_DVIT1435/g' $name
sed -i "" '1 s/DVIT1438_C0KDJACXX_1_250087439/V_riparia_DVIT1438/g' $name
sed -i "" '1 s/DVIT1440_C0KDJACXX_1_250087451/V_riparia_DVIT1440/g' $name
sed -i "" '1 s/DVIT1441_C0KDJACXX_1_250087463/V_riparia_DVIT1441/g' $name
sed -i "" '1 s/DVIT1451_C0KDJACXX_1_250087407/V_vulpina_DVIT1451/g' $name
sed -i "" '1 s/DVIT1594_999_C0TCDACXX_2_250088318/V_monticola_DVIT1594_999/g' $name
sed -i "" '1 s/DVIT1608_C0TCDACXX_2_250088299/V_aestivalis_DVIT1608/g' $name
sed -i "" '1 s/DVIT1689_C0TCDACXX_2_250088347/V_rotundifolia_DVIT1689/g' $name
sed -i "" '1 s/DVIT1690_C0TCDACXX_2_250088359/V_rotundifolia_DVIT1690/g' $name
sed -i "" '1 s/DVIT1694_C0TCDACXX_2_250088371/V_rotundifolia_DVIT1694/g' $name
sed -i "" '1 s/DVIT1701_C0TCDACXX_2_250088311/V_aestivalis_DVIT1701/g' $name
sed -i "" '1 s/DVIT1706_999_C0TCDACXX_2_250088312/V_rotundifolia_DVIT1706/g' $name
sed -i "" '1 s/DVIT1707_C0TCDACXX_2_250088324/V_rotundifolia_DVIT1707/g' $name
sed -i "" '1 s/DVIT1756_C0KDJACXX_1_250087402/V_rotundifolia_DVIT1756/g' $name
sed -i "" '1 s/DVIT1826_C0TCDACXX_2_250088368/V_aestivalis_DVIT1826/g' $name
sed -i "" '1 s/DVIT1844_C0TCDACXX_2_250088370/V_mustangensis_DVIT1844/g' $name
sed -i "" '1 s/DVIT1854_C0TCDACXX_2_250088335/V_monticola_DVIT1854/g' $name
sed -i "" '1 s/DVIT1872_C0KDJACXX_1_250087414/V_arizonica_DVIT1872/g' $name
sed -i "" '1 s/DVIT1901_C0TCDACXX_2_250088327/V_cinerea_DVIT1901/g' $name
sed -i "" '1 s/DVIT1903_C0TCDACXX_2_250088323/V_cinerea_DVIT1903/g' $name
sed -i "" '1 s/DVIT1905_C0TCDACXX_2_250088339/V_cinerea_DVIT1905/g' $name
sed -i "" '1 s/DVIT2006_1_C0TCDACXX_2_250088366/V_amurensis_DVIT2006_1/g' $name
sed -i "" '1 s/DVIT2026_C0TCDACXX_2_250088361/V_piasezkii_DVIT2026/g' $name
sed -i "" '1 s/DVIT2027_C0TCDACXX_2_250088373/V_piasezkii_DVIT2027/g' $name
sed -i "" '1 s/DVIT2028_C0KDJACXX_1_250087401/V_piasezkii_DVIT2028/g' $name
sed -i "" '1 s/DVIT2031_C0TCDACXX_2_250088301/V_piasezkii_DVIT2031/g' $name
sed -i "" '1 s/DVIT2032_C0TCDACXX_2_250088372/V_piasezkii_DVIT2032/g' $name
sed -i "" '1 s/DVIT2033_C0TCDACXX_2_250088360/V_piasezkii_DVIT2033/g' $name
sed -i "" '1 s/DVIT2098_C0TCDACXX_2_250088356/V_mustangensis_DVIT2098/g' $name
sed -i "" '1 s/DVIT2202_10_C0TCDACXX_2_250088321/V_aestivalis_DVIT2202_10/g' $name
sed -i "" '1 s/DVIT2203_6_C0TCDACXX_2_250088309/V_aestivalis_DVIT2203_6/g' $name
sed -i "" '1 s/DVIT2206_2_C0TCDACXX_2_250088297/V_aestivalis_DVIT2206_2/g' $name
sed -i "" '1 s/DVIT2207_15_C0TCDACXX_2_250088380/V_aestivalis_DVIT2207_15/g' $name
sed -i "" '1 s/DVIT2211_1_C0TCDACXX_2_250088333/V_arizonica_DVIT2211_1/g' $name
sed -i "" '1 s/DVIT2212_7_C0TCDACXX_2_250088352/V_biformis_DVIT2212_7/g' $name
sed -i "" '1 s/DVIT2217_1_C0TCDACXX_2_250088351/V_cinerea_DVIT2217_1/g' $name
sed -i "" '1 s/DVIT2218_17_C0TCDACXX_2_250088375/V_cinerea_DVIT2218_17/g' $name
sed -i "" '1 s/DVIT2220_1_C0TCDACXX_2_250088292/V_cinerea_DVIT2220_1/g' $name
sed -i "" '1 s/DVIT2221_7_C0TCDACXX_2_250088304/V_cinerea_DVIT2221_7/g' $name
sed -i "" '1 s/DVIT2227_1_C0TCDACXX_2_250088317/V_palmata_DVIT2227_1/g' $name
sed -i "" '1 s/DVIT2228_8_C0TCDACXX_2_250088293/V_palmata_DVIT2228_8/g' $name
sed -i "" '1 s/DVIT2230_2_C0TCDACXX_2_250088330/V_monticola_DVIT2230_2/g' $name
sed -i "" '1 s/DVIT2231_4_C0TCDACXX_2_250088342/V_monticola_DVIT2231_4/g' $name
sed -i "" '1 s/DVIT2232_2_C0TCDACXX_2_250088345/V_mustangensis_DVIT2232_2/g' $name
sed -i "" '1 s/DVIT2234_11_C0TCDACXX_2_250088369/V_mustangensis_DVIT2234_11/g' $name
sed -i "" '1 s/DVIT2235_4_C0TCDACXX_2_250088362/V_nesbittiana_DVIT2235_4/g' $name
sed -i "" '1 s/DVIT2235_5_C0TCDACXX_2_250088374/V_nesbittiana_DVIT2235_5/g' $name
sed -i "" '1 s/DVIT2236_2_C0TCDACXX_2_250088291/V_nesbittiana_DVIT2236_2/g' $name
sed -i "" '1 s/DVIT2244_3_C0TCDACXX_2_250088341/V_rotundifolia_DVIT2244_3/g' $name
sed -i "" '1 s/DVIT2245_3_C0TCDACXX_2_250088353/V_rotundifolia_DVIT2245_3/g' $name
sed -i "" '1 s/DVIT2246_1_C0TCDACXX_2_250088365/V_rotundifolia_DVIT2246_1/g' $name
sed -i "" '1 s/DVIT2248_5_C0TCDACXX_2_250088377/V_rotundifolia_DVIT2248_5/g' $name
sed -i "" '1 s/DVIT2249_2_C0TCDACXX_2_250088381/V_shuttleworthii_DVIT2249_2/g' $name
sed -i "" '1 s/DVIT2249_7_C0TCDACXX_2_250088298/V_shuttleworthii_DVIT2249_7/g' $name
sed -i "" '1 s/DVIT2249_9_C0TCDACXX_2_250088310/V_shuttleworthii_DVIT2249_9/g' $name
sed -i "" '1 s/DVIT2253_10_C0TCDACXX_2_250088329/V_vulpina_DVIT2253_10/g' $name
sed -i "" '1 s/DVIT2365_C0TCDACXX_2_250088338/V_aestivalis_DVIT2365/g' $name
sed -i "" '1 s/DVIT2371_C0TCDACXX_2_250088290/V_aestivalis_DVIT2371/g' $name
sed -i "" '1 s/DVIT2376_C0TCDACXX_2_250088350/V_aestivalis_DVIT2376/g' $name
sed -i "" '1 s/DVIT2380_C0TCDACXX_2_250088302/V_aestivalis_DVIT2380/g' $name
sed -i "" '1 s/DVIT2385_C0TCDACXX_2_250088314/V_aestivalis_DVIT2385/g' $name
sed -i "" '1 s/DVIT2386_C0TCDACXX_2_250088322/V_shuttleworthii_DVIT2386/g' $name
sed -i "" '1 s/DVIT2387_C0TCDACXX_2_250088334/V_shuttleworthii_DVIT2387/g' $name
sed -i "" '1 s/DVIT2435_C0KDJACXX_1_250087449/V_rotundifolia_DVIT2435/g' $name
sed -i "" '1 s/DVIT2436_C0KDJACXX_1_250087485/V_rotundifolia_DVIT2436/g' $name
sed -i "" '1 s/DVIT2596_3_C0TCDACXX_2_250088313/V_piasezkii_DVIT2596_3/g' $name
sed -i "" '1 s/DVIT2596_7_C0TCDACXX_2_250088325/V_piasezkii_DVIT2596_7/g' $name
sed -i "" '1 s/DVIT2699_C0TCDACXX_2_250088349/V_piasezkii_DVIT2699/g' $name
sed -i "" '1 s/DVIT2719_C0KDJACXX_1_250087473/V_rotundifolia_DVIT2719/g' $name
sed -i "" '1 s/DVIT2951_C0KDJACXX_1_250087419/V_vulpina_DVIT2951/g' $name
sed -i "" '1 s/DVIT2956_1_C0TCDACXX_2_250088300/V_cinerea_DVIT2956_1/g' $name
sed -i "" '1 s/DVIT2977_C0TCDACXX_2_250088320/V_palmata_DVIT2977/g' $name
sed -i "" '1 s/DVIT2979_C0TCDACXX_2_250088332/V_palmata_DVIT2979/g' $name
sed -i "" '1 s/DVIT2980_C0TCDACXX_2_250088344/V_palmata_DVIT2980/g' $name
sed -i "" '1 s/DVIT2983_C0KDJACXX_1_250087406/V_palmata_DVIT2983/g' $name
sed -i "" '1 s/Flame_C2C7HACXX_7_250232037/V_vinifera_Flame_250232037/g' $name
sed -i "" '1 s/Fruhburgunder_C2C7HACXX_7_250232028/V_vinifera_Fruhburgunder_250232028/g' $name
sed -i "" '1 s/Gewurztraminer_C2C7HACXX_7_250232030/V_vinifera_Gewurztraminer_250232030/g' $name
sed -i "" '1 s/GVIT_1583_C0TCDACXX_2_250088545/V_acerifolia_GVIT_1583/g' $name
sed -i "" '1 s/GVIT_1587_C0TCDACXX_2_250088458/V_labrusca_GVIT_1587/g' $name
sed -i "" '1 s/GVIT_171_C0TCDACXX_2_250088635/V_cinerea_GVIT_171/g' $name
sed -i "" '1 s/GVIT1471_C2C9HACXX_3_250225321/V_spp_GVIT1471/g' $name
sed -i "" '1 s/GVIT1613_C2C9HACXX_3_250225322/V_spp_GVIT1613/g' $name
sed -i "" '1 s/PI588260_C2CLAACXX_3_250225213/V_riparia_PI588260/g' $name
sed -i "" '1 s/PI588269_C2CLAACXX_3_250225205/V_riparia_PI588269/g' $name
sed -i "" '1 s/PI588270_C2CLAACXX_3_250225203/V_riparia_PI588270/g' $name
sed -i "" '1 s/PI588273_C2CLAACXX_3_250225194/V_riparia_PI588273/g' $name
sed -i "" '1 s/PI588274_C2CLAACXX_3_250225195/V_riparia_PI588274/g' $name
sed -i "" '1 s/PI588276_C2CLAACXX_3_250225204/V_riparia_PI588276/g' $name
sed -i "" '1 s/PI588347_C2CLAACXX_3_250225211/V_riparia_PI588347/g' $name
sed -i "" '1 s/Pinot_Gris_C2C7HACXX_7_250232050/V_vinifera_Pinot_Gris_250232050/g' $name
sed -i "" '1 s/Riesling_C2C7HACXX_7_250232027/V_vinifera_Riesling_250232027/g' $name
sed -i "" '1 s/Ruby_Cabernet_C2C7HACXX_7_250232038/V_vinifera_Ruby_Cabernet_250232038/g' $name
sed -i "" '1 s/Siegerrebe_C2C7HACXX_7_250232046/V_vinifera_Siegerrebe_250232046/g' $name
sed -i "" '1 s/Syrah_C2C7HACXX_7_250232026/V_vinifera_Syrah_250232026/g' $name
sed -i "" '1 s/V_riparia_NH2_C2CLAACXX_3_250225197/V_riparia_250225197/g' $name
sed -i "" '1 s/V_riparia14_C2CLAACXX_3_250225183/V_riparia14_250225183/g' $name
sed -i "" '1 s/V_riparia39_C2CLAACXX_3_250225184/V_riparia39_250225184/g' $name
sed -i "" '1 s/Zweigeltrebe_C2C7HACXX_7_250232031/V_vinifera_Zweigeltrebe_250232031/g' $name


sed -i "" '1 s/LLK293_C2C7HACXX_6_250241118/V_cinerea_250241118/g' $name
sed -i "" '1 s/LLK303_C2C7HACXX_6_250241128/V_cinerea_250241128/g' $name
sed -i "" '1 s/LLK299_C2C7HACXX_6_250241114/V_cinerea_250241114/g' $name
sed -i "" '1 s/LLK307_C2C7HACXX_6_250241133/V_cinerea_250241133/g' $name
sed -i "" '1 s/LLK162_C2C7HACXX_6_250241138/V_spp_250241138/g' $name
sed -i "" '1 s/LLK290_C2C7HACXX_6_250241119/V_palmata_250241119/g' $name
sed -i "" '1 s/LLK102_C2C7HACXX_8_250232587/V_riparia_250232587/g' $name
sed -i "" '1 s/LLK103_C2C7HACXX_8_250232588/V_riparia_250232588/g' $name
sed -i "" '1 s/LLK104_C2C7HACXX_8_250232589/V_riparia_250232589/g' $name
sed -i "" '1 s/LLK105_C2C7HACXX_8_250232590/V_riparia_250232590/g' $name
sed -i "" '1 s/LLK106_C2C7HACXX_8_250232591/V_riparia_250232591/g' $name
sed -i "" '1 s/LLK107_C2C7HACXX_8_250232592/V_riparia_250232592/g' $name
sed -i "" '1 s/LLK108_C2C7HACXX_8_250232593/V_riparia_250232593/g' $name
sed -i "" '1 s/LLK109_C2C7HACXX_8_250232594/V_riparia_250232594/g' $name
sed -i "" '1 s/LLK110_C2C7HACXX_8_250232595/V_riparia_250232595/g' $name
sed -i "" '1 s/LLK111_C2C7HACXX_8_250232596/V_riparia_250232596/g' $name
sed -i "" '1 s/LLK112_C2C7HACXX_8_250232597/V_riparia_250232597/g' $name
sed -i "" '1 s/LLK113_C2C7HACXX_8_250232598/V_riparia_250232598/g' $name
sed -i "" '1 s/LLK114_C2C7HACXX_8_250232599/V_riparia_250232599/g' $name
sed -i "" '1 s/LLK115_C2C7HACXX_8_250232600/V_riparia_250232600/g' $name
sed -i "" '1 s/LLK116_C2C7HACXX_8_250232601/V_riparia_250232601/g' $name
sed -i "" '1 s/LLK117_C2C7HACXX_8_250232602/V_riparia_250232602/g' $name
sed -i "" '1 s/LLK118_C2C7HACXX_8_250232603/V_riparia_250232603/g' $name
sed -i "" '1 s/LLK119_C2C7HACXX_8_250232604/V_riparia_250232604/g' $name
sed -i "" '1 s/LLK120_C2C7HACXX_8_250232605/V_riparia_250232605/g' $name
sed -i "" '1 s/LLK121_C2C7HACXX_8_250232606/V_riparia_250232606/g' $name
sed -i "" '1 s/LLK159_C2C7HACXX_6_250241145/V_riparia_250241145/g' $name
sed -i "" '1 s/LLK169_C2C7HACXX_6_250241149/V_riparia_250241149/g' $name
sed -i "" '1 s/LLK185_C2C7HACXX_6_250241152/V_riparia_250241152/g' $name
sed -i "" '1 s/LLK273_C2C7HACXX_6_250241177/V_riparia_250241177/g' $name
sed -i "" '1 s/LLK288_C2C7HACXX_6_250241121/V_riparia_250241121/g' $name
sed -i "" '1 s/LLK289_C2C7HACXX_6_250241120/V_riparia_250241120/g' $name
sed -i "" '1 s/LLK29_C2C7HACXX_8_250232543/V_riparia_250232543/g' $name
sed -i "" '1 s/LLK295_C2C7HACXX_6_250241132/V_riparia_250241132/g' $name
sed -i "" '1 s/LLK296_C2C7HACXX_6_250241126/V_riparia_250241126/g' $name
sed -i "" '1 s/LLK30_C2C7HACXX_8_250232539/V_riparia_250232539/g' $name
sed -i "" '1 s/LLK306_C2C7HACXX_6_250241131/V_riparia_250241131/g' $name
sed -i "" '1 s/LLK31_C2C7HACXX_8_250232538/V_riparia_250232538/g' $name
sed -i "" '1 s/LLK32_C2C7HACXX_8_250232540/V_riparia_250232540/g' $name
sed -i "" '1 s/LLK38_C2C7HACXX_8_250232547/V_riparia_250232547/g' $name
sed -i "" '1 s/LLK39_C2C7HACXX_8_250232548/V_riparia_250232548/g' $name
sed -i "" '1 s/LLK40_C2C7HACXX_8_250232549/V_riparia_250232549/g' $name
sed -i "" '1 s/LLK41_C2C7HACXX_8_250232550/V_riparia_250232550/g' $name
sed -i "" '1 s/LLK54_C2C7HACXX_8_250232555/V_riparia_250232555/g' $name
sed -i "" '1 s/LLK55_C2C7HACXX_8_250232556/V_riparia_250232556/g' $name
sed -i "" '1 s/LLK56_C2C7HACXX_8_250232557/V_riparia_250232557/g' $name
sed -i "" '1 s/LLK57_C2C7HACXX_8_250232558/V_riparia_250232558/g' $name
sed -i "" '1 s/LLK58_C2C7HACXX_8_250232551/V_riparia_250232551/g' $name
sed -i "" '1 s/LLK59_C2C7HACXX_8_250232559/V_riparia_250232559/g' $name
sed -i "" '1 s/LLK60_C2C7HACXX_8_250232552/V_riparia_250232552/g' $name
sed -i "" '1 s/LLK61_C2C7HACXX_8_250232560/V_riparia_250232560/g' $name
sed -i "" '1 s/LLK62_C2C7HACXX_8_250232561/V_riparia_250232561/g' $name
sed -i "" '1 s/LLK63_C2C7HACXX_8_250232553/V_riparia_250232553/g' $name
sed -i "" '1 s/LLK64_C2C7HACXX_8_250232554/V_riparia_250232554/g' $name
sed -i "" '1 s/LLK66_C2C7HACXX_8_250232563/V_riparia_250232563/g' $name
sed -i "" '1 s/LLK67_C2C7HACXX_8_250232564/V_riparia_250232564/g' $name
sed -i "" '1 s/LLK68_C2C7HACXX_8_250232565/V_riparia_250232565/g' $name
sed -i "" '1 s/LLK69_C2C7HACXX_8_250232566/V_riparia_250232566/g' $name
sed -i "" '1 s/LLK70_C2C7HACXX_8_250232567/V_riparia_250232567/g' $name
sed -i "" '1 s/LLK71_C2C7HACXX_8_250232568/V_riparia_250232568/g' $name
sed -i "" '1 s/LLK75_C2C7HACXX_8_250232569/V_riparia_250232569/g' $name
sed -i "" '1 s/LLK76_C2C7HACXX_8_250232570/V_riparia_250232570/g' $name
sed -i "" '1 s/LLK77_C2C7HACXX_8_250232571/V_riparia_250232571/g' $name
sed -i "" '1 s/LLK78_C2C7HACXX_8_250232572/V_riparia_250232572/g' $name
sed -i "" '1 s/LLK79_C2C7HACXX_8_250232573/V_riparia_250232573/g' $name
sed -i "" '1 s/LLK80_C2C7HACXX_8_250232574/V_riparia_250232574/g' $name
sed -i "" '1 s/LLK81_C2C7HACXX_8_250232575/V_riparia_250232575/g' $name
sed -i "" '1 s/LLK82_C2C7HACXX_8_250232576/V_riparia_250232576/g' $name
sed -i "" '1 s/LLK83_C2C7HACXX_8_250232577/V_riparia_250232577/g' $name
sed -i "" '1 s/LLK84_C2C7HACXX_8_250232578/V_riparia_250232578/g' $name
sed -i "" '1 s/LLK85_C2C7HACXX_8_250232579/V_riparia_250232579/g' $name
sed -i "" '1 s/LLK86_C2C7HACXX_8_250232580/V_riparia_250232580/g' $name
sed -i "" '1 s/LLK87_C2C7HACXX_8_250232581/V_riparia_250232581/g' $name
sed -i "" '1 s/LLK88_C2C7HACXX_8_250232583/V_riparia_250232583/g' $name
sed -i "" '1 s/LLK89_C2C7HACXX_8_250232582/V_riparia_250232582/g' $name
sed -i "" '1 s/LLK90_C2C7HACXX_8_250232584/V_riparia_250232584/g' $name
sed -i "" '1 s/LLK91_C2C7HACXX_8_250232585/V_riparia_250232585/g' $name
sed -i "" '1 s/LLK92_C2C7HACXX_8_250232586/V_riparia_250232586/g' $name
sed -i "" '1 s/LLK184_C2C7HACXX_6_250241140/V_riparia_250241140/g' $name
sed -i "" '1 s/LLK287_C2C7HACXX_6_250241122/V_riparia_250241122/g' $name
sed -i "" '1 s/LLK264_C2C7HACXX_6_250241174/V_riparia_250241174/g' $name
sed -i "" '1 s/LLK286_C2C7HACXX_6_250241162/V_riparia_250241162/g' $name
sed -i "" '1 s/LLK300_C2C7HACXX_6_250241115/V_riparia_250241115/g' $name
sed -i "" '1 s/LLK301_C2C7HACXX_6_250241130/V_riparia_250241130/g' $name
sed -i "" '1 s/LLK302_C2C7HACXX_6_250241134/V_riparia_250241134/g' $name
sed -i "" '1 s/LLK304_C2C7HACXX_6_250241127/V_riparia_250241127/g' $name
sed -i "" '1 s/LLK165_C2C7HACXX_6_250241157/V_riparia_250241157/g' $name
sed -i "" '1 s/LLK244_C2C7HACXX_6_250241165/V_riparia_250241165/g' $name
sed -i "" '1 s/LLK272_C2C7HACXX_6_250241176/V_riparia_250241176/g' $name
sed -i "" '1 s/LLK173_C2C7HACXX_6_250241161/V_riparia_250241161/g' $name
sed -i "" '1 s/LLK291_C2C7HACXX_6_250241123/V_riparia_250241123/g' $name
sed -i "" '1 s/LLK65_C2C7HACXX_8_250232562/V_riparia_250232562/g' $name
sed -i "" '1 s/LLK175_C2C7HACXX_6_250241083/V_rupestris_250241083/g' $name
sed -i "" '1 s/LLK188_C2C7HACXX_6_250241084/V_rupestris_250241084/g' $name
sed -i "" '1 s/LLK189_C2C7HACXX_6_250241085/V_rupestris_250241085/g' $name
sed -i "" '1 s/LLK190_C2C7HACXX_6_250241086/V_rupestris_250241086/g' $name
sed -i "" '1 s/LLK191_C2C7HACXX_6_250241087/V_rupestris_250241087/g' $name
sed -i "" '1 s/LLK192_C2C7HACXX_6_250241088/V_rupestris_250241088/g' $name
sed -i "" '1 s/LLK193_C2C7HACXX_6_250241089/V_rupestris_250241089/g' $name
sed -i "" '1 s/LLK194_C2C7HACXX_6_250241096/V_rupestris_250241096/g' $name
sed -i "" '1 s/LLK195_C2C7HACXX_6_250241090/V_rupestris_250241090/g' $name
sed -i "" '1 s/LLK196_C2C7HACXX_6_250241095/V_rupestris_250241095/g' $name
sed -i "" '1 s/LLK197_C2C7HACXX_6_250241100/V_rupestris_250241100/g' $name
sed -i "" '1 s/LLK198_C2C7HACXX_6_250241099/V_rupestris_250241099/g' $name
sed -i "" '1 s/LLK199_C2C7HACXX_6_250241093/V_rupestris_250241093/g' $name
sed -i "" '1 s/LLK200_C2C7HACXX_6_250241091/V_rupestris_250241091/g' $name
sed -i "" '1 s/LLK201_C2C7HACXX_6_250241092/V_rupestris_250241092/g' $name
sed -i "" '1 s/LLK202_C2C7HACXX_6_250241094/V_rupestris_250241094/g' $name
sed -i "" '1 s/LLK204_C2C7HACXX_6_250241097/V_rupestris_250241097/g' $name
sed -i "" '1 s/LLK205_C2C7HACXX_6_250241098/V_rupestris_250241098/g' $name
sed -i "" '1 s/LLK211_C2C7HACXX_6_250241101/V_rupestris_250241101/g' $name
sed -i "" '1 s/LLK212_C2C7HACXX_6_250241102/V_rupestris_250241102/g' $name
sed -i "" '1 s/LLK47_C2C7HACXX_6_250241106/V_rupestris_250241106/g' $name
sed -i "" '1 s/LLK48_C2C7HACXX_6_250241105/V_rupestris_250241105/g' $name
sed -i "" '1 s/LLK49_C2C7HACXX_6_250241108/V_rupestris_250241108/g' $name
sed -i "" '1 s/LLK51_C2C7HACXX_6_250241103/V_rupestris_250241103/g' $name
sed -i "" '1 s/LLK52_C2C7HACXX_6_250241104/V_rupestris_250241104/g' $name
sed -i "" '1 s/588378_MERGE/V_acerifolia_588378/g' $name
sed -i "" '1 s/588448_a_MERGE/V_acerifolia_588448_a/g' $name
sed -i "" '1 s/588448_b_C2C9HACXX_3_250225485/V_acerifolia_588448_b_250225485/g' $name
sed -i "" '1 s/588448_e_C2C9HACXX_3_250225488/V_acerifolia_588448_e_250225488/g' $name
sed -i "" '1 s/588448_C0TCDACXX_2_250088581/V_acerifolia_588448_250088581/g' $name
sed -i "" '1 s/588449_a_MERGE/V_acerifolia_588449_a/g' $name
sed -i "" '1 s/588458_b_C2C9HACXX_3_250225432/V_acerifolia_588458_b_250225432/g' $name
sed -i "" '1 s/588458_c_C2C9HACXX_3_250225433/V_acerifolia_588458_c_250225433/g' $name
sed -i "" '1 s/588458_d_C2C9HACXX_3_250225434/V_acerifolia_588458_d_250225434/g' $name
sed -i "" '1 s/588458_e_C2C9HACXX_3_250225435/V_acerifolia_588458_e_250225435/g' $name
sed -i "" '1 s/588458_f_C2C9HACXX_3_250225436/V_acerifolia_588458_f_250225436/g' $name
sed -i "" '1 s/588458_g_C2C9HACXX_3_250225437/V_acerifolia_588458_g_250225437/g' $name
sed -i "" '1 s/588458_h_C2C9HACXX_3_250225438/V_acerifolia_588458_h_250225438/g' $name
sed -i "" '1 s/588458_i_C2C9HACXX_3_250225439/V_acerifolia_588458_i_250225439/g' $name
sed -i "" '1 s/588458_j_C2C9HACXX_3_250225440/V_acerifolia_588458_j_250225440/g' $name
sed -i "" '1 s/588458_k_C2C9HACXX_3_250225441/V_acerifolia_588458_k_250225441/g' $name
sed -i "" '1 s/588458_l_C2C9HACXX_3_250225442/V_acerifolia_588458_l_250225442/g' $name
sed -i "" '1 s/588458_m_C2C9HACXX_3_250225443/V_acerifolia_588458_m_250225443/g' $name
sed -i "" '1 s/588458_n_C2C9HACXX_3_250225444/V_acerifolia_588458_n_250225444/g' $name
sed -i "" '1 s/588458_o_C2C9HACXX_3_250225445/V_acerifolia_588458_o_250225445/g' $name
sed -i "" '1 s/588458_p_C2C9HACXX_3_250225446/V_acerifolia_588458_p_250225446/g' $name
sed -i "" '1 s/588458_q_C2C9HACXX_3_250225447/V_acerifolia_588458_q_250225447/g' $name
sed -i "" '1 s/588458_r_C2C9HACXX_3_250225448/V_acerifolia_588458_r_250225448/g' $name
sed -i "" '1 s/588458_s_C2C9HACXX_3_250225449/V_acerifolia_588458_s_250225449/g' $name
sed -i "" '1 s/588458_t_C2C9HACXX_3_250225450/V_acerifolia_588458_t_250225450/g' $name
sed -i "" '1 s/588458_u_MERGE/V_acerifolia_588458_u/g' $name
sed -i "" '1 s/588458_v_C2C9HACXX_3_250225452/V_acerifolia_588458_v_250225452/g' $name
sed -i "" '1 s/588458_w_C2C9HACXX_3_250225453/V_acerifolia_588458_w_250225453/g' $name
sed -i "" '1 s/588458_x_C2C9HACXX_3_250225454/V_acerifolia_588458_x_250225454/g' $name
sed -i "" '1 s/588458_y_C2C9HACXX_3_250225455/V_acerifolia_588458_y_250225455/g' $name
sed -i "" '1 s/588459_a_C2C9HACXX_3_250225341/V_acerifolia_588459_a_250225341/g' $name
sed -i "" '1 s/588459_b_C2C9HACXX_3_250225342/V_acerifolia_588459_b_250225342/g' $name
sed -i "" '1 s/588459_c_C2C9HACXX_3_250225343/V_acerifolia_588459_c_250225343/g' $name
sed -i "" '1 s/588459_e_C2C9HACXX_3_250225344/V_acerifolia_588459_e_250225344/g' $name
sed -i "" '1 s/588459_f_C2C9HACXX_3_250225345/V_acerifolia_588459_f_250225345/g' $name
sed -i "" '1 s/588459_g_C2C9HACXX_3_250225346/V_acerifolia_588459_g_250225346/g' $name
sed -i "" '1 s/588459_h_C2C9HACXX_3_250225347/V_acerifolia_588459_h_250225347/g' $name
sed -i "" '1 s/588459_i_C2C9HACXX_3_250225348/V_acerifolia_588459_i_250225348/g' $name
sed -i "" '1 s/588459_j_C2C9HACXX_3_250225349/V_acerifolia_588459_j_250225349/g' $name
sed -i "" '1 s/588459_k_C2C9HACXX_3_250225350/V_acerifolia_588459_k_250225350/g' $name
sed -i "" '1 s/588459_l_C2C9HACXX_3_250225351/V_acerifolia_588459_l_250225351/g' $name
sed -i "" '1 s/588459_n_C2C9HACXX_3_250225352/V_acerifolia_588459_n_250225352/g' $name
sed -i "" '1 s/588459_o_C2C9HACXX_3_250225353/V_acerifolia_588459_o_250225353/g' $name
sed -i "" '1 s/588459_p_C2C9HACXX_3_250225354/V_acerifolia_588459_p_250225354/g' $name
sed -i "" '1 s/588459_q_C2C9HACXX_3_250225355/V_acerifolia_588459_q_250225355/g' $name
sed -i "" '1 s/588459_r_C2C9HACXX_3_250225356/V_acerifolia_588459_r_250225356/g' $name
sed -i "" '1 s/588459_s_C2C9HACXX_3_250225357/V_acerifolia_588459_s_250225357/g' $name
sed -i "" '1 s/588459_t_MERGE/V_acerifolia_588459_t/g' $name
sed -i "" '1 s/588459_u_C2C9HACXX_3_250225359/V_acerifolia_588459_u_250225359/g' $name
sed -i "" '1 s/588459_v_C2C9HACXX_3_250225360/V_acerifolia_588459_v_250225360/g' $name
sed -i "" '1 s/588459_w_C2C9HACXX_3_250225361/V_acerifolia_588459_w_250225361/g' $name
sed -i "" '1 s/588459_x_C2C9HACXX_3_250225362/V_acerifolia_588459_x_250225362/g' $name
sed -i "" '1 s/588646_MERGE/V_acerifolia_588646/g' $name
sed -i "" '1 s/006_1_C28DTACXX_2_250190416/V_aestivalis_006_1_250190416/g' $name
sed -i "" '1 s/006_2_C28DTACXX_2_250190417/V_aestivalis_006_2_250190417/g' $name
sed -i "" '1 s/009_1_C28DTACXX_2_250190247/V_aestivalis_009_1_250190247/g' $name
sed -i "" '1 s/009_2_C28DTACXX_2_250190151/V_aestivalis_009_2_250190151/g' $name
sed -i "" '1 s/009_3_C28DTACXX_2_250190248/V_aestivalis_009_3_250190248/g' $name
sed -i "" '1 s/009_4_C28DTACXX_2_250190152/V_aestivalis_009_4_250190152/g' $name
sed -i "" '1 s/009_5_C28DTACXX_2_250190153/V_aestivalis_009_5_250190153/g' $name
sed -i "" '1 s/011_1_C28DTACXX_2_250190035/V_aestivalis_011_1_250190035/g' $name
sed -i "" '1 s/011_10_C28DTACXX_2_250190426/V_aestivalis_011_10_250190426/g' $name
sed -i "" '1 s/011_6_C28DTACXX_2_250190261/V_aestivalis_011_6_250190261/g' $name
sed -i "" '1 s/011_7_C28DTACXX_2_250190262/V_aestivalis_011_7_250190262/g' $name
sed -i "" '1 s/011_8_C28DTACXX_2_250190414/V_aestivalis_011_8_250190414/g' $name
sed -i "" '1 s/011_9_C28DTACXX_2_250190415/V_aestivalis_011_9_250190415/g' $name
sed -i "" '1 s/017_1_C28DTACXX_2_250190267/V_aestivalis_017_1_250190267/g' $name
sed -i "" '1 s/022_1_C28DTACXX_2_250189954/V_aestivalis_022_1_250189954/g' $name
sed -i "" '1 s/022_2_C28DTACXX_2_250190158/V_aestivalis_022_2_250190158/g' $name
sed -i "" '1 s/053_1_C28DTACXX_2_250190138/V_aestivalis_053_1_250190138/g' $name
sed -i "" '1 s/060_1_C28DTACXX_2_250190093/V_aestivalis_060_1_250190093/g' $name
sed -i "" '1 s/069_2_C28DTACXX_2_250190141/V_aestivalis_069_2_250190141/g' $name
sed -i "" '1 s/090_2_C28DTACXX_2_250190277/V_aestivalis_090_2_250190277/g' $name
sed -i "" '1 s/090_3_C28DTACXX_2_250190278/V_aestivalis_090_3_250190278/g' $name
sed -i "" '1 s/090_4_C28DTACXX_2_250190279/V_aestivalis_090_4_250190279/g' $name
sed -i "" '1 s/090_5_C28DTACXX_2_250190402/V_aestivalis_090_5_250190402/g' $name
sed -i "" '1 s/090_6_C28DTACXX_2_250190403/V_aestivalis_090_6_250190403/g' $name
sed -i "" '1 s/090_7_C28DTACXX_2_250190423/V_aestivalis_090_7_250190423/g' $name
sed -i "" '1 s/091_1_C28DTACXX_2_250190032/V_aestivalis_091_1_250190032/g' $name
sed -i "" '1 s/091_2_C28DTACXX_2_250190033/V_aestivalis_091_2_250190033/g' $name
sed -i "" '1 s/091_3_C28DTACXX_2_250190364/V_aestivalis_091_3_250190364/g' $name
sed -i "" '1 s/091_4_C28DTACXX_2_250190034/V_aestivalis_091_4_250190034/g' $name
sed -i "" '1 s/093_1_C28DTACXX_2_250190102/V_aestivalis_093_1_250190102/g' $name
sed -i "" '1 s/093_2_C28DTACXX_2_250190135/V_aestivalis_093_2_250190135/g' $name
sed -i "" '1 s/093_3_C28DTACXX_2_250190136/V_aestivalis_093_3_250190136/g' $name
sed -i "" '1 s/117_1_C28DTACXX_2_250189962/V_aestivalis_117_1_250189962/g' $name
sed -i "" '1 s/120_4_C28DTACXX_2_250190391/V_aestivalis_120_4_250190391/g' $name
sed -i "" '1 s/120_5_C28DTACXX_2_250190390/V_aestivalis_120_5_250190390/g' $name
sed -i "" '1 s/122_1_C28DTACXX_2_250190039/V_aestivalis_122_1_250190039/g' $name
sed -i "" '1 s/122_2_C28DTACXX_2_250190040/V_aestivalis_122_2_250190040/g' $name
sed -i "" '1 s/122_4_C28DTACXX_2_250190041/V_aestivalis_122_4_250190041/g' $name
sed -i "" '1 s/123_1_C28DTACXX_2_250190418/V_aestivalis_123_1_250190418/g' $name
sed -i "" '1 s/125_1_C28DTACXX_2_250190106/V_aestivalis_125_1_250190106/g' $name
sed -i "" '1 s/125_3_C28DTACXX_2_250190107/V_aestivalis_125_3_250190107/g' $name
sed -i "" '1 s/125_4_C28DTACXX_2_250190108/V_aestivalis_125_4_250190108/g' $name
sed -i "" '1 s/1664_a_MERGE/V_aestivalis_1664_a/g' $name
sed -i "" '1 s/1664_c_C2C9HACXX_3_250225624/V_aestivalis_1664_c_250225624/g' $name
sed -i "" '1 s/1664_k_C2C9HACXX_3_250225626/V_aestivalis_1664_k_250225626/g' $name
sed -i "" '1 s/1664_m_C2C9HACXX_3_250225651/V_aestivalis_1664_m_250225651/g' $name
sed -i "" '1 s/1664_n_C2C9HACXX_3_250225652/V_aestivalis_1664_n_250225652/g' $name
sed -i "" '1 s/1665_b_C2C7HACXX_8_250232512/V_aestivalis_1665_b_250232512/g' $name
sed -i "" '1 s/1665_c_MERGE/V_aestivalis_1665_c/g' $name
sed -i "" '1 s/1665_d_C2C7HACXX_8_250232514/V_aestivalis_1665_d_250232514/g' $name
sed -i "" '1 s/1665_e_C2C7HACXX_8_250232515/V_aestivalis_1665_e_250232515/g' $name
sed -i "" '1 s/1665_f_C2C7HACXX_8_250232516/V_aestivalis_1665_f_250232516/g' $name
sed -i "" '1 s/1665_g_C2C7HACXX_8_250232517/V_aestivalis_1665_g_250232517/g' $name
sed -i "" '1 s/1665_h_C2C7HACXX_8_250232518/V_aestivalis_1665_h_250232518/g' $name
sed -i "" '1 s/1665_i_C2C7HACXX_8_250232520/V_aestivalis_1665_i_250232520/g' $name
sed -i "" '1 s/1665_k_C2C7HACXX_8_250232521/V_aestivalis_1665_k_250232521/g' $name
sed -i "" '1 s/1665_m_C2C7HACXX_8_250232523/V_aestivalis_1665_m_250232523/g' $name
sed -i "" '1 s/1665_n_C2C7HACXX_8_250232524/V_aestivalis_1665_n_250232524/g' $name
sed -i "" '1 s/DVIT1445_C0TCDACXX_2_250088348/V_jacquemontii_DVIT1445_250088348/g' $name
sed -i "" '1 s/LLK37_C2C7HACXX_8_250232546/V_Ampelopsis_cordata_250232546/g' $name
sed -i "" '1 s/588382_MERGE/V_amurensis_588382/g' $name
sed -i "" '1 s/588420_a_MERGE/V_amurensis_588420_a/g' $name
sed -i "" '1 s/588420_d_C2C9HACXX_3_250225497/V_amurensis_588420_d_250225497/g' $name
sed -i "" '1 s/588420_m_C2C9HACXX_3_250225595/V_amurensis_588420_m_250225595/g' $name
sed -i "" '1 s/588629_MERGE/V_amurensis_588629/g' $name
sed -i "" '1 s/588630_MERGE/V_amurensis_588630/g' $name
sed -i "" '1 s/588631_MERGE/V_amurensis_588631/g' $name
sed -i "" '1 s/588635_MERGE/V_amurensis_588635/g' $name
sed -i "" '1 s/588638_MERGE/V_amurensis_588638/g' $name
sed -i "" '1 s/DVIT1157_2_C0TCDACXX_2_250088378/V_amurensis_DVIT1157_2_250088378/g' $name
sed -i "" '1 s/DVIT1158_2_C0TCDACXX_2_250088295/V_amurensis_DVIT1158_2_250088295/g' $name
sed -i "" '1 s/DVIT2005_12_C0TCDACXX_2_250088367/V_amurensis_DVIT2005_12_250088367/g' $name
sed -i "" '1 s/DVIT2211_7_C0TCDACXX_2_250088326/V_arizonica_DVIT2211_7_250088326/g' $name
sed -i "" '1 s/DVIT2212_14_C0TCDACXX_2_250088340/V_biformis_DVIT2212_14_250088340/g' $name
sed -i "" '1 s/DVIT2212_16_C0TCDACXX_2_250088364/V_biformis_DVIT2212_16_250088364/g' $name
sed -i "" '1 s/DVIT2212_17_C0TCDACXX_2_250088376/V_biformis_DVIT2212_17_250088376/g' $name
sed -i "" '1 s/DVIT2212_19_C0TCDACXX_2_250088305/V_biformis_DVIT2212_19_250088305/g' $name
sed -i "" '1 s/DVIT2212_23_C0TCDACXX_2_250088328/V_biformis_DVIT2212_23_250088328/g' $name
sed -i "" '1 s/DVIT2952_C0TCDACXX_2_250088296/V_biformis_DVIT2952_250088296/g' $name
sed -i "" '1 s/DVIT2213_8_C0TCDACXX_2_250088316/V_blancoii_DVIT2213_8_250088316/g' $name
sed -i "" '1 s/DVIT2214_14_C0TCDACXX_2_250088331/V_bloodworthiana_DVIT2214_14_250088331/g' $name
sed -i "" '1 s/DVIT2214_17_C0TCDACXX_2_250088355/V_bloodworthiana_DVIT2214_17_250088355/g' $name
sed -i "" '1 s/DVIT2214_3_C0TCDACXX_2_250088307/V_bloodworthiana_DVIT2214_3_250088307/g' $name
sed -i "" '1 s/DVIT2214_4_C0TCDACXX_2_250088319/V_bloodworthiana_DVIT2214_4_250088319/g' $name
sed -i "" '1 s/DVIT2214_8_C0TCDACXX_2_250088343/V_bloodworthiana_DVIT2214_8_250088343/g' $name
sed -i "" '1 s/DVIT2606_C0TCDACXX_2_250088379/V_bourgaeana_DVIT2606_250088379/g' $name
sed -i "" '1 s/056_1_C28DTACXX_2_250190099/V_cinerea_056_1_250190099/g' $name
sed -i "" '1 s/056_2_C28DTACXX_2_250190100/V_cinerea_056_2_250190100/g' $name
sed -i "" '1 s/056_3_C28DTACXX_2_250190374/V_cinerea_056_3_250190374/g' $name
sed -i "" '1 s/056_4_C28DTACXX_2_250190375/V_cinerea_056_4_250190375/g' $name
sed -i "" '1 s/056_5_C28DTACXX_2_250190101/V_cinerea_056_5_250190101/g' $name
sed -i "" '1 s/588221_MERGE/V_cinerea_588221/g' $name
sed -i "" '1 s/588446_a_MERGE/V_cinerea_588446_a/g' $name
sed -i "" '1 s/588447_d_MERGE/V_cinerea_588447_d/g' $name
sed -i "" '1 s/588460_b_MERGE/V_cinerea_588460_b/g' $name
sed -i "" '1 s/588460_c_C2C9HACXX_3_250225465/V_cinerea_588460_c_250225465/g' $name
sed -i "" '1 s/588460_d_C2C9HACXX_3_250225466/V_cinerea_588460_d_250225466/g' $name
sed -i "" '1 s/588460_g_C2C9HACXX_3_250225467/V_cinerea_588460_g_250225467/g' $name
sed -i "" '1 s/588688_b_MERGE/V_cinerea_588688_b/g' $name
sed -i "" '1 s/DVIT2217_10_C0TCDACXX_2_250088363/V_cinerea_DVIT2217_10_250088363/g' $name
sed -i "" '1 s/588216_MERGE/V_cinerea_var_helleri_588216/g' $name
sed -i "" '1 s/588443_a_MERGE/V_cinerea_var_helleri_588443_a/g' $name
sed -i "" '1 s/588444_b_MERGE/V_cinerea_var_helleri_588444_b/g' $name
sed -i "" '1 s/588445_c_MERGE/V_cinerea_var_helleri_588445_c/g' $name
sed -i "" '1 s/588445_d_C2C9HACXX_3_250225463/V_cinerea_var_helleri_588445_d_250225463/g' $name
sed -i "" '1 s/588451_c_MERGE/V_coignetiae_588451_c/g' $name
sed -i "" '1 s/588451_g_C2C9HACXX_3_250225483/V_coignetiae_588451_g_250225483/g' $name
sed -i "" '1 s/588643_MERGE/V_coignetiae_588643/g' $name
sed -i "" '1 s/588645_MERGE/V_coignetiae_588645/g' $name
sed -i "" '1 s/588055_d_MERGE/V_ficifolia_588055_d/g' $name
sed -i "" '1 s/DVIT1385_C0TCDACXX_2_250088337/V_flexuosa_DVIT1385_250088337/g' $name
sed -i "" '1 s/DVIT2554_C0KDJACXX_1_250087413/V_heyneana_DVIT2554_250087413/g' $name
sed -i "" '1 s/DVIT2559_C0KDJACXX_1_250087425/V_heyneana_DVIT2559_250087425/g' $name
sed -i "" '1 s/Bianca_C2C7HACXX_7_250232036/V_Bianca_250232036/g' $name
sed -i "" '1 s/Concord_C0KDJACXX_1_250087491/V_Concord_250087491/g' $name
sed -i "" '1 s/PC10_100_1_MERGE/V_PC10_100_1/g' $name
sed -i "" '1 s/PC10_100_2_MERGE/V_PC10_100_2/g' $name
sed -i "" '1 s/PC10_112_1_MERGE/V_PC10_112_1/g' $name
sed -i "" '1 s/116_1_C28DTACXX_2_250190116/V_aestivalis_250190116/g' $name
sed -i "" '1 s/116_2_C28DTACXX_2_250190117/V_aestivalis_250190117/g' $name
sed -i "" '1 s/116_3_C28DTACXX_2_250190118/V_aestivalis_250190118/g' $name
sed -i "" '1 s/116_4_C28DTACXX_2_250190381/V_aestivalis_250190381/g' $name
sed -i "" '1 s/116_5_C28DTACXX_2_250190382/V_aestivalis_250190382/g' $name
sed -i "" '1 s/100_1_C28DTACXX_2_250190090/V_riparia_250190090/g' $name
sed -i "" '1 s/100_2_C28DTACXX_2_250190091/V_riparia_250190091/g' $name
sed -i "" '1 s/100_3_C28DTACXX_2_250190092/V_riparia_250190092/g' $name
sed -i "" '1 s/118_1_C28DTACXX_2_250189990/V_riparia_250189990/g' $name
sed -i "" '1 s/118_2_C28DTACXX_2_250190353/V_riparia_250190353/g' $name
sed -i "" '1 s/118_3_C28DTACXX_2_250189991/V_riparia_250189991/g' $name
sed -i "" '1 s/118_4_C28DTACXX_2_250189992/V_riparia_250189992/g' $name
sed -i "" '1 s/118_5_C28DTACXX_2_250190354/V_riparia_250190354/g' $name
sed -i "" '1 s/LLK171_C2C7HACXX_6_250241159/V_Ampelopsis_250241159/g' $name
sed -i "" '1 s/012_1_C28DTACXX_2_250190094/V_labrusca_012_1_250190094/g' $name
sed -i "" '1 s/014_1_C28DTACXX_2_250189984/V_labrusca_014_1_250189984/g' $name
sed -i "" '1 s/014_2_C28DTACXX_2_250189985/V_labrusca_014_2_250189985/g' $name
sed -i "" '1 s/014_3_C28DTACXX_2_250189986/V_labrusca_014_3_250189986/g' $name
sed -i "" '1 s/018_1_C28DTACXX_2_250189950/V_labrusca_018_1_250189950/g' $name
sed -i "" '1 s/018_4_C28DTACXX_2_250190139/V_labrusca_018_4_250190139/g' $name
sed -i "" '1 s/018_5_C28DTACXX_2_250190140/V_labrusca_018_5_250190140/g' $name
sed -i "" '1 s/019_2_C28DTACXX_2_250189974/V_labrusca_019_2_250189974/g' $name
sed -i "" '1 s/021_2_C28DTACXX_2_250190109/V_labrusca_021_2_250190109/g' $name
sed -i "" '1 s/021_3_C28DTACXX_2_250190110/V_labrusca_021_3_250190110/g' $name
sed -i "" '1 s/021_4_C28DTACXX_2_250190111/V_labrusca_021_4_250190111/g' $name
sed -i "" '1 s/021_5_C28DTACXX_2_250190378/V_labrusca_021_5_250190378/g' $name
sed -i "" '1 s/023_1_C28DTACXX_2_250189964/V_labrusca_023_1_250189964/g' $name
sed -i "" '1 s/023_10_C28DTACXX_2_250190239/V_labrusca_023_10_250190239/g' $name
sed -i "" '1 s/023_11_C28DTACXX_2_250190240/V_labrusca_023_11_250190240/g' $name
sed -i "" '1 s/023_12_C28DTACXX_2_250190280/V_labrusca_023_12_250190280/g' $name
sed -i "" '1 s/023_13_C28DTACXX_2_250190281/V_labrusca_023_13_250190281/g' $name
sed -i "" '1 s/023_5_C28DTACXX_2_250190168/V_labrusca_023_5_250190168/g' $name
sed -i "" '1 s/023_6_C28DTACXX_2_250190169/V_labrusca_023_6_250190169/g' $name
sed -i "" '1 s/023_8_C28DTACXX_2_250190241/V_labrusca_023_8_250190241/g' $name
sed -i "" '1 s/026_1_C28DTACXX_2_250190016/V_labrusca_026_1_250190016/g' $name
sed -i "" '1 s/026_10_C28DTACXX_2_250190260/V_labrusca_026_10_250190260/g' $name
sed -i "" '1 s/026_11_C28DTACXX_2_250190258/V_labrusca_026_11_250190258/g' $name
sed -i "" '1 s/026_12_C28DTACXX_2_250190299/V_labrusca_026_12_250190299/g' $name
sed -i "" '1 s/026_13_C28DTACXX_2_250190282/V_labrusca_026_13_250190282/g' $name
sed -i "" '1 s/026_14_C28DTACXX_2_250190283/V_labrusca_026_14_250190283/g' $name
sed -i "" '1 s/026_6_C28DTACXX_2_250190257/V_labrusca_026_6_250190257/g' $name
sed -i "" '1 s/026_7_C28DTACXX_2_250190164/V_labrusca_026_7_250190164/g' $name
sed -i "" '1 s/026_8_C28DTACXX_2_250190149/V_labrusca_026_8_250190149/g' $name
sed -i "" '1 s/026_9_C28DTACXX_2_250190150/V_labrusca_026_9_250190150/g' $name
sed -i "" '1 s/027_1_C28DTACXX_2_250189978/V_labrusca_027_1_250189978/g' $name
sed -i "" '1 s/027_2_C28DTACXX_2_250189979/V_labrusca_027_2_250189979/g' $name
sed -i "" '1 s/027_3_C28DTACXX_2_250189980/V_labrusca_027_3_250189980/g' $name
sed -i "" '1 s/027_4_C28DTACXX_2_250190348/V_labrusca_027_4_250190348/g' $name
sed -i "" '1 s/027_5_C28DTACXX_2_250190349/V_labrusca_027_5_250190349/g' $name
sed -i "" '1 s/028_10_C28DTACXX_2_250190286/V_labrusca_028_10_250190286/g' $name
sed -i "" '1 s/028_11_C28DTACXX_2_250190287/V_labrusca_028_11_250190287/g' $name
sed -i "" '1 s/028_3_C28DTACXX_2_250190253/V_labrusca_028_3_250190253/g' $name
sed -i "" '1 s/028_4_C28DTACXX_2_250190146/V_labrusca_028_4_250190146/g' $name
sed -i "" '1 s/028_5_C28DTACXX_2_250190147/V_labrusca_028_5_250190147/g' $name
sed -i "" '1 s/028_6_C28DTACXX_2_250190254/V_labrusca_028_6_250190254/g' $name
sed -i "" '1 s/028_7_C28DTACXX_2_250190148/V_labrusca_028_7_250190148/g' $name
sed -i "" '1 s/028_8_C28DTACXX_2_250190284/V_labrusca_028_8_250190284/g' $name
sed -i "" '1 s/028_9_C28DTACXX_2_250190285/V_labrusca_028_9_250190285/g' $name
sed -i "" '1 s/029_3_C28DTACXX_2_250189975/V_labrusca_029_3_250189975/g' $name
sed -i "" '1 s/029_4_C28DTACXX_2_250189976/V_labrusca_029_4_250189976/g' $name
sed -i "" '1 s/029_5_C28DTACXX_2_250189977/V_labrusca_029_5_250189977/g' $name
sed -i "" '1 s/030_1_C28DTACXX_2_250189981/V_labrusca_030_1_250189981/g' $name
sed -i "" '1 s/030_2_C28DTACXX_2_250189982/V_labrusca_030_2_250189982/g' $name
sed -i "" '1 s/030_3_C28DTACXX_2_250189983/V_labrusca_030_3_250189983/g' $name
sed -i "" '1 s/030_4_C28DTACXX_2_250190350/V_labrusca_030_4_250190350/g' $name
sed -i "" '1 s/030_5_C28DTACXX_2_250190351/V_labrusca_030_5_250190351/g' $name
sed -i "" '1 s/031_2_C28DTACXX_2_250190013/V_labrusca_031_2_250190013/g' $name
sed -i "" '1 s/032_2_C28DTACXX_2_250190159/V_labrusca_032_2_250190159/g' $name
sed -i "" '1 s/034_1_C28DTACXX_2_250189955/V_labrusca_034_1_250189955/g' $name
sed -i "" '1 s/034_2_C28DTACXX_2_250189956/V_labrusca_034_2_250189956/g' $name
sed -i "" '1 s/034_3_C28DTACXX_2_250189957/V_labrusca_034_3_250189957/g' $name
sed -i "" '1 s/034_4_C28DTACXX_2_250190335/V_labrusca_034_4_250190335/g' $name
sed -i "" '1 s/035_1_C28DTACXX_2_250190003/V_labrusca_035_1_250190003/g' $name
sed -i "" '1 s/035_2_MERGE/V_labrusca_035_2/g' $name
sed -i "" '1 s/035_3_C28DTACXX_2_250190166/V_labrusca_035_3_250190166/g' $name
sed -i "" '1 s/035_4_C28DTACXX_2_250190238/V_labrusca_035_4_250190238/g' $name
sed -i "" '1 s/035_6_C28DTACXX_2_250190167/V_labrusca_035_6_250190167/g' $name
sed -i "" '1 s/035_7_C28DTACXX_2_250190237/V_labrusca_035_7_250190237/g' $name
sed -i "" '1 s/035_8_C28DTACXX_2_250190288/V_labrusca_035_8_250190288/g' $name
sed -i "" '1 s/035_9_C28DTACXX_2_250190289/V_labrusca_035_9_250190289/g' $name
sed -i "" '1 s/037_1_C28DTACXX_2_250190017/V_labrusca_037_1_250190017/g' $name
sed -i "" '1 s/037_10_C28DTACXX_2_250190405/V_labrusca_037_10_250190405/g' $name
sed -i "" '1 s/037_11_C28DTACXX_2_250190424/V_labrusca_037_11_250190424/g' $name
sed -i "" '1 s/037_6_C28DTACXX_2_250190273/V_labrusca_037_6_250190273/g' $name
sed -i "" '1 s/037_7_C28DTACXX_2_250190274/V_labrusca_037_7_250190274/g' $name
sed -i "" '1 s/037_8_C28DTACXX_2_250190275/V_labrusca_037_8_250190275/g' $name
sed -i "" '1 s/037_9_MERGE/V_labrusca_037_9/g' $name
sed -i "" '1 s/038_1_C28DTACXX_2_250189961/V_labrusca_038_1_250189961/g' $name
sed -i "" '1 s/038_10_C28DTACXX_2_250190155/V_labrusca_038_10_250190155/g' $name
sed -i "" '1 s/038_11_C28DTACXX_2_250190250/V_labrusca_038_11_250190250/g' $name
sed -i "" '1 s/038_12_C28DTACXX_2_250190251/V_labrusca_038_12_250190251/g' $name
sed -i "" '1 s/038_13_C28DTACXX_2_250190156/V_labrusca_038_13_250190156/g' $name
sed -i "" '1 s/038_14_C28DTACXX_2_250190290/V_labrusca_038_14_250190290/g' $name
sed -i "" '1 s/038_15_C28DTACXX_2_250190291/V_labrusca_038_15_250190291/g' $name
sed -i "" '1 s/038_16_C28DTACXX_2_250190292/V_labrusca_038_16_250190292/g' $name
sed -i "" '1 s/038_9_C28DTACXX_2_250190249/V_labrusca_038_9_250190249/g' $name
sed -i "" '1 s/039_1_C28DTACXX_2_250190098/V_labrusca_039_1_250190098/g' $name
sed -i "" '1 s/039_3_C28DTACXX_2_250190134/V_labrusca_039_3_250190134/g' $name
sed -i "" '1 s/040_1_C28DTACXX_2_250190029/V_labrusca_040_1_250190029/g' $name
sed -i "" '1 s/040_2_C28DTACXX_2_250190030/V_labrusca_040_2_250190030/g' $name
sed -i "" '1 s/040_3_C28DTACXX_2_250190031/V_labrusca_040_3_250190031/g' $name
sed -i "" '1 s/042_1_C28DTACXX_2_250190122/V_labrusca_042_1_250190122/g' $name
sed -i "" '1 s/042_6_C28DTACXX_2_250190137/V_labrusca_042_6_250190137/g' $name
sed -i "" '1 s/044_2_C28DTACXX_2_250190244/V_labrusca_044_2_250190244/g' $name
sed -i "" '1 s/044_6_C28DTACXX_2_250190245/V_labrusca_044_6_250190245/g' $name
sed -i "" '1 s/044_7_C28DTACXX_2_250190395/V_labrusca_044_7_250190395/g' $name
sed -i "" '1 s/044_8_C28DTACXX_2_250190396/V_labrusca_044_8_250190396/g' $name
sed -i "" '1 s/044_9_C28DTACXX_2_250190397/V_labrusca_044_9_250190397/g' $name
sed -i "" '1 s/045_1_C28DTACXX_2_250190000/V_labrusca_045_1_250190000/g' $name
sed -i "" '1 s/045_2_C28DTACXX_2_250190001/V_labrusca_045_2_250190001/g' $name
sed -i "" '1 s/045_3_C28DTACXX_2_250190002/V_labrusca_045_3_250190002/g' $name
sed -i "" '1 s/045_4_C28DTACXX_2_250190355/V_labrusca_045_4_250190355/g' $name
sed -i "" '1 s/045_5_C28DTACXX_2_250190356/V_labrusca_045_5_250190356/g' $name
sed -i "" '1 s/046_1_C28DTACXX_2_250190042/V_labrusca_046_1_250190042/g' $name
sed -i "" '1 s/046_2_C28DTACXX_2_250190043/V_labrusca_046_2_250190043/g' $name
sed -i "" '1 s/046_3_C28DTACXX_2_250190044/V_labrusca_046_3_250190044/g' $name
sed -i "" '1 s/046_4_C28DTACXX_2_250190365/V_labrusca_046_4_250190365/g' $name
sed -i "" '1 s/046_5_C28DTACXX_2_250190366/V_labrusca_046_5_250190366/g' $name
sed -i "" '1 s/048_1_C28DTACXX_2_250189997/V_labrusca_048_1_250189997/g' $name
sed -i "" '1 s/048_2_C28DTACXX_2_250189998/V_labrusca_048_2_250189998/g' $name
sed -i "" '1 s/048_3_C28DTACXX_2_250189999/V_labrusca_048_3_250189999/g' $name
sed -i "" '1 s/049_2_C28DTACXX_2_250190026/V_labrusca_049_2_250190026/g' $name
sed -i "" '1 s/049_4_C28DTACXX_2_250190027/V_labrusca_049_4_250190027/g' $name
sed -i "" '1 s/050_10_C28DTACXX_2_250190411/V_labrusca_050_10_250190411/g' $name
sed -i "" '1 s/050_11_C28DTACXX_2_250190425/V_labrusca_050_11_250190425/g' $name
sed -i "" '1 s/050_4_C28DTACXX_2_250190083/V_labrusca_050_4_250190083/g' $name
sed -i "" '1 s/050_6_C28DTACXX_2_250190270/V_labrusca_050_6_250190270/g' $name
sed -i "" '1 s/050_8_C28DTACXX_2_250190271/V_labrusca_050_8_250190271/g' $name
sed -i "" '1 s/050_9_C28DTACXX_2_250190410/V_labrusca_050_9_250190410/g' $name
sed -i "" '1 s/052_1_C28DTACXX_2_250189993/V_labrusca_052_1_250189993/g' $name
sed -i "" '1 s/052_2_C28DTACXX_2_250189994/V_labrusca_052_2_250189994/g' $name
sed -i "" '1 s/052_4_C28DTACXX_2_250190170/V_labrusca_052_4_250190170/g' $name
sed -i "" '1 s/052_5_C28DTACXX_2_250190171/V_labrusca_052_5_250190171/g' $name
sed -i "" '1 s/052_6_C28DTACXX_2_250190242/V_labrusca_052_6_250190242/g' $name
sed -i "" '1 s/052_7_C28DTACXX_2_250190243/V_labrusca_052_7_250190243/g' $name
sed -i "" '1 s/052_8_C28DTACXX_2_250190293/V_labrusca_052_8_250190293/g' $name
sed -i "" '1 s/054_1_C28DTACXX_2_250190036/V_labrusca_054_1_250190036/g' $name
sed -i "" '1 s/054_2_C28DTACXX_2_250190037/V_labrusca_054_2_250190037/g' $name
sed -i "" '1 s/054_3_C28DTACXX_2_250190038/V_labrusca_054_3_250190038/g' $name
sed -i "" '1 s/058_2_C28DTACXX_2_250190077/V_labrusca_058_2_250190077/g' $name
sed -i "" '1 s/058_3_C28DTACXX_2_250190078/V_labrusca_058_3_250190078/g' $name
sed -i "" '1 s/058_4_C28DTACXX_2_250190079/V_labrusca_058_4_250190079/g' $name
sed -i "" '1 s/071_1_C28DTACXX_2_250190119/V_labrusca_071_1_250190119/g' $name
sed -i "" '1 s/078_1_C28DTACXX_2_250190084/V_labrusca_078_1_250190084/g' $name
sed -i "" '1 s/078_2_C28DTACXX_2_250190154/V_labrusca_078_2_250190154/g' $name
sed -i "" '1 s/078_4_C28DTACXX_2_250190142/V_labrusca_078_4_250190142/g' $name
sed -i "" '1 s/079_1_C28DTACXX_2_250190264/V_labrusca_079_1_250190264/g' $name
sed -i "" '1 s/079_2_C28DTACXX_2_250190265/V_labrusca_079_2_250190265/g' $name
sed -i "" '1 s/079_3_C28DTACXX_2_250190266/V_labrusca_079_3_250190266/g' $name
sed -i "" '1 s/079_4_MERGE/V_labrusca_079_4/g' $name
sed -i "" '1 s/079_5_MERGE/V_labrusca_079_5/g' $name
sed -i "" '1 s/080_1_C28DTACXX_2_250190143/V_labrusca_080_1_250190143/g' $name
sed -i "" '1 s/080_2_C28DTACXX_2_250190144/V_labrusca_080_2_250190144/g' $name
sed -i "" '1 s/080_3_C28DTACXX_2_250190145/V_labrusca_080_3_250190145/g' $name
sed -i "" '1 s/081_1_C28DTACXX_2_250190014/V_labrusca_081_1_250190014/g' $name
sed -i "" '1 s/081_3_C28DTACXX_2_250190015/V_labrusca_081_3_250190015/g' $name
sed -i "" '1 s/083_1_C28DTACXX_2_250189995/V_labrusca_083_1_250189995/g' $name
sed -i "" '1 s/083_2_C28DTACXX_2_250189996/V_labrusca_083_2_250189996/g' $name
sed -i "" '1 s/083_3_C28DTACXX_2_250190157/V_labrusca_083_3_250190157/g' $name
sed -i "" '1 s/084_1_C28DTACXX_2_250190112/V_labrusca_084_1_250190112/g' $name
sed -i "" '1 s/087_1_C28DTACXX_2_250190028/V_labrusca_087_1_250190028/g' $name
sed -i "" '1 s/087_2_C28DTACXX_2_250190272/V_labrusca_087_2_250190272/g' $name
sed -i "" '1 s/087_3_C28DTACXX_2_250190406/V_labrusca_087_3_250190406/g' $name
sed -i "" '1 s/087_4_C28DTACXX_2_250190407/V_labrusca_087_4_250190407/g' $name
sed -i "" '1 s/087_5_C28DTACXX_2_250190408/V_labrusca_087_5_250190408/g' $name
sed -i "" '1 s/087_6_C28DTACXX_2_250190409/V_labrusca_087_6_250190409/g' $name
sed -i "" '1 s/094_1_C28DTACXX_2_250190336/V_labrusca_094_1_250190336/g' $name
sed -i "" '1 s/094_2_C28DTACXX_2_250189958/V_labrusca_094_2_250189958/g' $name
sed -i "" '1 s/094_3_C28DTACXX_2_250189959/V_labrusca_094_3_250189959/g' $name
sed -i "" '1 s/094_4_C28DTACXX_2_250189960/V_labrusca_094_4_250189960/g' $name
sed -i "" '1 s/094_5_C28DTACXX_2_250190337/V_labrusca_094_5_250190337/g' $name
sed -i "" '1 s/095_1_C28DTACXX_2_250190113/V_labrusca_095_1_250190113/g' $name
sed -i "" '1 s/095_2_C28DTACXX_2_250190114/V_labrusca_095_2_250190114/g' $name
sed -i "" '1 s/095_3_C28DTACXX_2_250190115/V_labrusca_095_3_250190115/g' $name
sed -i "" '1 s/095_4_C28DTACXX_2_250190379/V_labrusca_095_4_250190379/g' $name
sed -i "" '1 s/095_5_C28DTACXX_2_250190380/V_labrusca_095_5_250190380/g' $name
sed -i "" '1 s/096_1_C28DTACXX_2_250189968/V_labrusca_096_1_250189968/g' $name
sed -i "" '1 s/096_2_C28DTACXX_2_250189969/V_labrusca_096_2_250189969/g' $name
sed -i "" '1 s/096_3_C28DTACXX_2_250189970/V_labrusca_096_3_250189970/g' $name
sed -i "" '1 s/096_4_C28DTACXX_2_250190345/V_labrusca_096_4_250190345/g' $name
sed -i "" '1 s/096_5_C28DTACXX_2_250190346/V_labrusca_096_5_250190346/g' $name
sed -i "" '1 s/098_1_C28DTACXX_2_250190087/V_labrusca_098_1_250190087/g' $name
sed -i "" '1 s/098_2_C28DTACXX_2_250190088/V_labrusca_098_2_250190088/g' $name
sed -i "" '1 s/098_3_C28DTACXX_2_250190370/V_labrusca_098_3_250190370/g' $name
sed -i "" '1 s/098_4_C28DTACXX_2_250190089/V_labrusca_098_4_250190089/g' $name
sed -i "" '1 s/098_5_C28DTACXX_2_250190371/V_labrusca_098_5_250190371/g' $name
sed -i "" '1 s/099_1_C28DTACXX_2_250190085/V_labrusca_099_1_250190085/g' $name
sed -i "" '1 s/099_2_C28DTACXX_2_250190086/V_labrusca_099_2_250190086/g' $name
sed -i "" '1 s/099_4_C28DTACXX_2_250190252/V_labrusca_099_4_250190252/g' $name
sed -i "" '1 s/099_5_C28DTACXX_2_250190123/V_labrusca_099_5_250190123/g' $name
sed -i "" '1 s/099_7_C28DTACXX_2_250190294/V_labrusca_099_7_250190294/g' $name
sed -i "" '1 s/101_2_C28DTACXX_2_250190160/V_labrusca_101_2_250190160/g' $name
sed -i "" '1 s/101_3_C28DTACXX_2_250190161/V_labrusca_101_3_250190161/g' $name
sed -i "" '1 s/102_10_C28DTACXX_2_250190399/V_labrusca_102_10_250190399/g' $name
sed -i "" '1 s/102_11_C28DTACXX_2_250190400/V_labrusca_102_11_250190400/g' $name
sed -i "" '1 s/102_12_C28DTACXX_2_250190401/V_labrusca_102_12_250190401/g' $name
sed -i "" '1 s/102_3_C28DTACXX_2_250190018/V_labrusca_102_3_250190018/g' $name
sed -i "" '1 s/102_4_C28DTACXX_2_250190019/V_labrusca_102_4_250190019/g' $name
sed -i "" '1 s/102_8_C28DTACXX_2_250190246/V_labrusca_102_8_250190246/g' $name
sed -i "" '1 s/102_9_C28DTACXX_2_250190398/V_labrusca_102_9_250190398/g' $name
sed -i "" '1 s/103_1_C28DTACXX_2_250190130/V_labrusca_103_1_250190130/g' $name
sed -i "" '1 s/103_2_C28DTACXX_2_250190131/V_labrusca_103_2_250190131/g' $name
sed -i "" '1 s/103_3_C28DTACXX_2_250190132/V_labrusca_103_3_250190132/g' $name
sed -i "" '1 s/103_4_C28DTACXX_2_250190387/V_labrusca_103_4_250190387/g' $name
sed -i "" '1 s/104_2_C28DTACXX_2_250190023/V_labrusca_104_2_250190023/g' $name
sed -i "" '1 s/104_4_C28DTACXX_2_250190024/V_labrusca_104_4_250190024/g' $name
sed -i "" '1 s/104_5_C28DTACXX_2_250190025/V_labrusca_104_5_250190025/g' $name
sed -i "" '1 s/105_1_C28DTACXX_2_250190007/V_labrusca_105_1_250190007/g' $name
sed -i "" '1 s/105_2_C28DTACXX_2_250190008/V_labrusca_105_2_250190008/g' $name
sed -i "" '1 s/105_3a_C28DTACXX_2_250190358/V_labrusca_105_3a_250190358/g' $name
sed -i "" '1 s/105_3b_C28DTACXX_2_250190359/V_labrusca_105_3b_250190359/g' $name
sed -i "" '1 s/105_4_C28DTACXX_2_250190009/V_labrusca_105_4_250190009/g' $name
sed -i "" '1 s/105_5_C28DTACXX_2_250190360/V_labrusca_105_5_250190360/g' $name
sed -i "" '1 s/106_1_C28DTACXX_2_250190120/V_labrusca_106_1_250190120/g' $name
sed -i "" '1 s/106_2_C28DTACXX_2_250190121/V_labrusca_106_2_250190121/g' $name
sed -i "" '1 s/106_3_C28DTACXX_2_250190388/V_labrusca_106_3_250190388/g' $name
sed -i "" '1 s/106_4_C28DTACXX_2_250190389/V_labrusca_106_4_250190389/g' $name
sed -i "" '1 s/106_5_C28DTACXX_2_250190133/V_labrusca_106_5_250190133/g' $name
sed -i "" '1 s/107_1_C28DTACXX_2_250190172/V_labrusca_107_1_250190172/g' $name
sed -i "" '1 s/107_2_C28DTACXX_2_250190383/V_labrusca_107_2_250190383/g' $name
sed -i "" '1 s/107_3_C28DTACXX_2_250190125/V_labrusca_107_3_250190125/g' $name
sed -i "" '1 s/107_4_C28DTACXX_2_250190384/V_labrusca_107_4_250190384/g' $name
sed -i "" '1 s/107_5_C28DTACXX_2_250190126/V_labrusca_107_5_250190126/g' $name
sed -i "" '1 s/108_10_C28DTACXX_2_250190298/V_labrusca_108_10_250190298/g' $name
sed -i "" '1 s/108_2_C28DTACXX_2_250189963/V_labrusca_108_2_250189963/g' $name
sed -i "" '1 s/108_3_C28DTACXX_2_250190255/V_labrusca_108_3_250190255/g' $name
sed -i "" '1 s/108_4_C28DTACXX_2_250190162/V_labrusca_108_4_250190162/g' $name
sed -i "" '1 s/108_5_C28DTACXX_2_250190163/V_labrusca_108_5_250190163/g' $name
sed -i "" '1 s/108_6_C28DTACXX_2_250190256/V_labrusca_108_6_250190256/g' $name
sed -i "" '1 s/108_7_C28DTACXX_2_250190295/V_labrusca_108_7_250190295/g' $name
sed -i "" '1 s/108_8_C28DTACXX_2_250190296/V_labrusca_108_8_250190296/g' $name
sed -i "" '1 s/108_9_C28DTACXX_2_250190297/V_labrusca_108_9_250190297/g' $name
sed -i "" '1 s/109_1_C28DTACXX_2_250189987/V_labrusca_109_1_250189987/g' $name
sed -i "" '1 s/109_2_C28DTACXX_2_250189988/V_labrusca_109_2_250189988/g' $name
sed -i "" '1 s/109_3_C28DTACXX_2_250190045/V_labrusca_109_3_250190045/g' $name
sed -i "" '1 s/109_4_C28DTACXX_2_250190352/V_labrusca_109_4_250190352/g' $name
sed -i "" '1 s/110_1_C28DTACXX_2_250190103/V_labrusca_110_1_250190103/g' $name
sed -i "" '1 s/110_2_C28DTACXX_2_250190104/V_labrusca_110_2_250190104/g' $name
sed -i "" '1 s/110_3_C28DTACXX_2_250190105/V_labrusca_110_3_250190105/g' $name
sed -i "" '1 s/110_4_C28DTACXX_2_250190376/V_labrusca_110_4_250190376/g' $name
sed -i "" '1 s/110_5_C28DTACXX_2_250190377/V_labrusca_110_5_250190377/g' $name
sed -i "" '1 s/111_1_C28DTACXX_2_250190020/V_labrusca_111_1_250190020/g' $name
sed -i "" '1 s/111_4_C28DTACXX_2_250190021/V_labrusca_111_4_250190021/g' $name
sed -i "" '1 s/111_5_C28DTACXX_2_250190022/V_labrusca_111_5_250190022/g' $name
sed -i "" '1 s/112_1_C28DTACXX_2_250190127/V_labrusca_112_1_250190127/g' $name
sed -i "" '1 s/112_2_C28DTACXX_2_250190128/V_labrusca_112_2_250190128/g' $name
sed -i "" '1 s/112_3_C28DTACXX_2_250190129/V_labrusca_112_3_250190129/g' $name
sed -i "" '1 s/112_4_C28DTACXX_2_250190385/V_labrusca_112_4_250190385/g' $name
sed -i "" '1 s/112_5_C28DTACXX_2_250190386/V_labrusca_112_5_250190386/g' $name
sed -i "" '1 s/113_1_C28DTACXX_2_250189965/V_labrusca_113_1_250189965/g' $name
sed -i "" '1 s/113_10_C28DTACXX_2_250190344/V_labrusca_113_10_250190344/g' $name
sed -i "" '1 s/113_2_C28DTACXX_2_250189966/V_labrusca_113_2_250189966/g' $name
sed -i "" '1 s/113_3_C28DTACXX_2_250189967/V_labrusca_113_3_250189967/g' $name
sed -i "" '1 s/113_4_C28DTACXX_2_250190338/V_labrusca_113_4_250190338/g' $name
sed -i "" '1 s/113_5_C28DTACXX_2_250190339/V_labrusca_113_5_250190339/g' $name
sed -i "" '1 s/113_6_C28DTACXX_2_250190340/V_labrusca_113_6_250190340/g' $name
sed -i "" '1 s/113_7_C28DTACXX_2_250190341/V_labrusca_113_7_250190341/g' $name
sed -i "" '1 s/113_8_C28DTACXX_2_250190342/V_labrusca_113_8_250190342/g' $name
sed -i "" '1 s/113_9_C28DTACXX_2_250190343/V_labrusca_113_9_250190343/g' $name
sed -i "" '1 s/114_1_C28DTACXX_2_250190080/V_labrusca_114_1_250190080/g' $name
sed -i "" '1 s/114_2_C28DTACXX_2_250190081/V_labrusca_114_2_250190081/g' $name
sed -i "" '1 s/114_3_C28DTACXX_2_250190082/V_labrusca_114_3_250190082/g' $name
sed -i "" '1 s/114_4_C28DTACXX_2_250190368/V_labrusca_114_4_250190368/g' $name
sed -i "" '1 s/114_5_C28DTACXX_2_250190369/V_labrusca_114_5_250190369/g' $name
sed -i "" '1 s/115_1_C28DTACXX_2_250190095/V_labrusca_115_1_250190095/g' $name
sed -i "" '1 s/115_2_C28DTACXX_2_250190096/V_labrusca_115_2_250190096/g' $name
sed -i "" '1 s/115_3_C28DTACXX_2_250190097/V_labrusca_115_3_250190097/g' $name
sed -i "" '1 s/115_4_C28DTACXX_2_250190372/V_labrusca_115_4_250190372/g' $name
sed -i "" '1 s/115_5_C28DTACXX_2_250190373/V_labrusca_115_5_250190373/g' $name
sed -i "" '1 s/20_4_C28DTACXX_2_250190392/V_labrusca_20_4_250190392/g' $name
sed -i "" '1 s/20_5_C28DTACXX_2_250190393/V_labrusca_20_5_250190393/g' $name
sed -i "" '1 s/483133_MERGE/V_labrusca_483133/g' $name
sed -i "" '1 s/483156_MERGE/V_labrusca_483156/g' $name
sed -i "" '1 s/483159_MERGE/V_labrusca_483159/g' $name
sed -i "" '1 s/483164_MERGE/V_labrusca_483164/g' $name
sed -i "" '1 s/588173_MERGE/V_labrusca_588173/g' $name
sed -i "" '1 s/588277_MERGE/V_labrusca_588277/g' $name
sed -i "" '1 s/588648_MERGE/V_labrusca_588648/g' $name
sed -i "" '1 s/597203_MERGE/V_labrusca_597203/g' $name
sed -i "" '1 s/PCJL_115_1_C0TCDACXX_2_250088383/V_labrusca_PCJL_115_1_250088383/g' $name
sed -i "" '1 s/PCJL_117_1_C0TCDACXX_2_250088384/V_labrusca_PCJL_117_1_250088384/g' $name
sed -i "" '1 s/PCJL_117_2_C0TCDACXX_2_250088385/V_labrusca_PCJL_117_2_250088385/g' $name
sed -i "" '1 s/Rt8_2_C28DTACXX_2_250190263/V_labrusca_Rt8_2_250190263/g' $name
sed -i "" '1 s/Rt8_3_C28DTACXX_2_250190419/V_labrusca_Rt8_3_250190419/g' $name
sed -i "" '1 s/Rt8_4_C28DTACXX_2_250190420/V_labrusca_Rt8_4_250190420/g' $name
sed -i "" '1 s/Rt8_5_C28DTACXX_2_250190421/V_labrusca_Rt8_5_250190421/g' $name
sed -i "" '1 s/Rt8_6_C28DTACXX_2_250190422/V_labrusca_Rt8_6_250190422/g' $name
sed -i "" '1 s/DVIT1815_C0TCDACXX_2_250088336/V_lanata_DVIT1815_250088336/g' $name
sed -i "" '1 s/DVIT1373_C0TCDACXX_2_250088306/V_monticola_DVIT1373_250088306/g' $name
sed -i "" '1 s/DVIT1892_MERGE/V_mustangensis_DVIT1892/g' $name
sed -i "" '1 s/DVIT2236_11_C0TCDACXX_2_250088315/V_nesbittiana_DVIT2236_11_250088315/g' $name
sed -i "" '1 s/DVIT2236_12_C0TCDACXX_2_250088303/V_nesbittiana_DVIT2236_12_250088303/g' $name
sed -i "" '1 s/DVIT2600_C0TCDACXX_2_250088308/V_peninsularis_DVIT2600_250088308/g' $name
sed -i "" '1 s/DVIT2970_C0KDJACXX_1_250087461/V_popenoei_DVIT2970_250087461/g' $name
sed -i "" '1 s/483167_MERGE/V_riparia_483167/g' $name
sed -i "" '1 s/483173_MERGE/V_riparia_483173/g' $name
sed -i "" '1 s/483178_MERGE/V_riparia_483178/g' $name
sed -i "" '1 s/495622_d_C2C9HACXX_3_250225385/V_riparia_495622_d_250225385/g' $name
sed -i "" '1 s/495622_e_C2C9HACXX_3_250225386/V_riparia_495622_e_250225386/g' $name
sed -i "" '1 s/495622_f_C2C9HACXX_3_250225387/V_riparia_495622_f_250225387/g' $name
sed -i "" '1 s/495622_g_C2C9HACXX_3_250225388/V_riparia_495622_g_250225388/g' $name
sed -i "" '1 s/495622_h_C2C9HACXX_3_250225389/V_riparia_495622_h_250225389/g' $name
sed -i "" '1 s/495622_i_C2C9HACXX_3_250225390/V_riparia_495622_i_250225390/g' $name
sed -i "" '1 s/495622_l_C2C9HACXX_3_250225391/V_riparia_495622_l_250225391/g' $name
sed -i "" '1 s/495622_m_C2C9HACXX_3_250225392/V_riparia_495622_m_250225392/g' $name
sed -i "" '1 s/495622_n_C2C9HACXX_3_250225393/V_riparia_495622_n_250225393/g' $name
sed -i "" '1 s/495622_s_C2C9HACXX_3_250225395/V_riparia_495622_s_250225395/g' $name
sed -i "" '1 s/495622_t_C2C9HACXX_3_250225396/V_riparia_495622_t_250225396/g' $name
sed -i "" '1 s/495622_u_C2C9HACXX_3_250225397/V_riparia_495622_u_250225397/g' $name
sed -i "" '1 s/495622_v_C2C9HACXX_3_250225398/V_riparia_495622_v_250225398/g' $name
sed -i "" '1 s/495622_w_MERGE/V_riparia_495622_w/g' $name
sed -i "" '1 s/588450_a_MERGE/V_riparia_588450_a/g' $name
sed -i "" '1 s/588450_c_C2C9HACXX_3_250225491/V_riparia_588450_c_250225491/g' $name
sed -i "" '1 s/588450_d_C2C9HACXX_3_250225492/V_riparia_588450_d_250225492/g' $name
sed -i "" '1 s/588450_e_C2C9HACXX_3_250225493/V_riparia_588450_e_250225493/g' $name
sed -i "" '1 s/588453_a_MERGE/V_riparia_588453_a/g' $name
sed -i "" '1 s/588453_c_C2C9HACXX_3_250225480/V_riparia_588453_c_250225480/g' $name
sed -i "" '1 s/588457_MERGE/V_riparia_588457/g' $name
sed -i "" '1 s/588565_C0KDJACXX_1_250087420/V_riparia_588565_250087420/g' $name
sed -i "" '1 s/588568_MERGE/V_riparia_588568/g' $name
sed -i "" '1 s/588586_a_C2C9HACXX_3_250225516/V_riparia_588586_a_250225516/g' $name
sed -i "" '1 s/588586_b_MERGE/V_riparia_588586_b/g' $name
sed -i "" '1 s/588586_c_C2C9HACXX_3_250225518/V_riparia_588586_c_250225518/g' $name
sed -i "" '1 s/588586_d_C2C9HACXX_3_250225519/V_riparia_588586_d_250225519/g' $name
sed -i "" '1 s/588586_e_C2C9HACXX_3_250225520/V_riparia_588586_e_250225520/g' $name
sed -i "" '1 s/588586_f_C2C9HACXX_3_250225521/V_riparia_588586_f_250225521/g' $name
sed -i "" '1 s/588586_g_C2C9HACXX_3_250225522/V_riparia_588586_g_250225522/g' $name
sed -i "" '1 s/588587_a_MERGE/V_riparia_588587_a/g' $name
sed -i "" '1 s/588588_c_C2C9HACXX_3_250225597/V_riparia_588588_c_250225597/g' $name
sed -i "" '1 s/588588_d_MERGE/V_riparia_588588_d/g' $name
sed -i "" '1 s/588588_e_C2C9HACXX_3_250225599/V_riparia_588588_e_250225599/g' $name
sed -i "" '1 s/588588_f_C2C9HACXX_3_250225600/V_riparia_588588_f_250225600/g' $name
sed -i "" '1 s/588588_g_C2C9HACXX_3_250225601/V_riparia_588588_g_250225601/g' $name
sed -i "" '1 s/588588_h_C2C9HACXX_3_250225602/V_riparia_588588_h_250225602/g' $name
sed -i "" '1 s/588588_j_C2C9HACXX_3_250225604/V_riparia_588588_j_250225604/g' $name
sed -i "" '1 s/588588_k_C2C9HACXX_3_250225605/V_riparia_588588_k_250225605/g' $name
sed -i "" '1 s/588588_l_C2C9HACXX_3_250225606/V_riparia_588588_l_250225606/g' $name
sed -i "" '1 s/588588_m_C2C9HACXX_3_250225607/V_riparia_588588_m_250225607/g' $name
sed -i "" '1 s/588588_n_C2C9HACXX_3_250225608/V_riparia_588588_n_250225608/g' $name
sed -i "" '1 s/588588_o_C2C9HACXX_3_250225609/V_riparia_588588_o_250225609/g' $name
sed -i "" '1 s/588588_p_C2C9HACXX_3_250225610/V_riparia_588588_p_250225610/g' $name
sed -i "" '1 s/588588_q_C2C9HACXX_3_250225611/V_riparia_588588_q_250225611/g' $name
sed -i "" '1 s/588588_r_C2C9HACXX_3_250225612/V_riparia_588588_r_250225612/g' $name
sed -i "" '1 s/588588_s_C2C9HACXX_3_250225613/V_riparia_588588_s_250225613/g' $name
sed -i "" '1 s/588588_t_C2C9HACXX_3_250225614/V_riparia_588588_t_250225614/g' $name
sed -i "" '1 s/588588_u_C2C9HACXX_3_250225615/V_riparia_588588_u_250225615/g' $name
sed -i "" '1 s/588588_v_C2C9HACXX_3_250225616/V_riparia_588588_v_250225616/g' $name
sed -i "" '1 s/588588_w_C2C9HACXX_3_250225617/V_riparia_588588_w_250225617/g' $name
sed -i "" '1 s/588588_x_C2C9HACXX_3_250225618/V_riparia_588588_x_250225618/g' $name
sed -i "" '1 s/588590_a_MERGE/V_riparia_588590_a/g' $name
sed -i "" '1 s/588590_c_C2C9HACXX_3_250225525/V_riparia_588590_c_250225525/g' $name
sed -i "" '1 s/588590_e_C2C9HACXX_3_250225628/V_riparia_588590_e_250225628/g' $name
sed -i "" '1 s/588590_f_C2C9HACXX_3_250225558/V_riparia_588590_f_250225558/g' $name
sed -i "" '1 s/588590_g_C2C9HACXX_3_250225559/V_riparia_588590_g_250225559/g' $name
sed -i "" '1 s/588590_h_C2C9HACXX_3_250225560/V_riparia_588590_h_250225560/g' $name
sed -i "" '1 s/588590_i_C2C9HACXX_3_250225561/V_riparia_588590_i_250225561/g' $name
sed -i "" '1 s/588590_j_C2C9HACXX_3_250225562/V_riparia_588590_j_250225562/g' $name
sed -i "" '1 s/588590_k_C2C9HACXX_3_250225563/V_riparia_588590_k_250225563/g' $name
sed -i "" '1 s/588590_l_C2C9HACXX_3_250225564/V_riparia_588590_l_250225564/g' $name
sed -i "" '1 s/588590_m_C2C9HACXX_3_250225565/V_riparia_588590_m_250225565/g' $name
sed -i "" '1 s/588590_n_C2C9HACXX_3_250225566/V_riparia_588590_n_250225566/g' $name
sed -i "" '1 s/588590_o_C2C9HACXX_3_250225567/V_riparia_588590_o_250225567/g' $name
sed -i "" '1 s/588590_p_C2C9HACXX_3_250225568/V_riparia_588590_p_250225568/g' $name
sed -i "" '1 s/588590_q_C2C9HACXX_3_250225569/V_riparia_588590_q_250225569/g' $name
sed -i "" '1 s/588590_r_C2C9HACXX_3_250225570/V_riparia_588590_r_250225570/g' $name
sed -i "" '1 s/588590_s_C2C9HACXX_3_250225571/V_riparia_588590_s_250225571/g' $name
sed -i "" '1 s/588590_t_C2C9HACXX_3_250225572/V_riparia_588590_t_250225572/g' $name
sed -i "" '1 s/588590_v_C2C9HACXX_3_250225573/V_riparia_588590_v_250225573/g' $name
sed -i "" '1 s/588590_w_C2C9HACXX_3_250225574/V_riparia_588590_w_250225574/g' $name
sed -i "" '1 s/588590_z_C2C9HACXX_3_250225575/V_riparia_588590_z_250225575/g' $name
sed -i "" '1 s/588710_a_C2C9HACXX_3_250225627/V_riparia_588710_a_250225627/g' $name
sed -i "" '1 s/588710_b_C2C9HACXX_3_250225629/V_riparia_588710_b_250225629/g' $name
sed -i "" '1 s/588710_c_C2C9HACXX_3_250225630/V_riparia_588710_c_250225630/g' $name
sed -i "" '1 s/588710_d_C2C9HACXX_3_250225631/V_riparia_588710_d_250225631/g' $name
sed -i "" '1 s/588710_e_C2C9HACXX_3_250225632/V_riparia_588710_e_250225632/g' $name
sed -i "" '1 s/588710_f_C2C9HACXX_3_250225633/V_riparia_588710_f_250225633/g' $name
sed -i "" '1 s/588710_g_C2C9HACXX_3_250225634/V_riparia_588710_g_250225634/g' $name
sed -i "" '1 s/588710_h_C2C9HACXX_3_250225635/V_riparia_588710_h_250225635/g' $name
sed -i "" '1 s/588710_i_C2C9HACXX_3_250225636/V_riparia_588710_i_250225636/g' $name
sed -i "" '1 s/588710_j_MERGE/V_riparia_588710_j/g' $name
sed -i "" '1 s/588710_k_C2C9HACXX_3_250225638/V_riparia_588710_k_250225638/g' $name
sed -i "" '1 s/588710_l_C2C9HACXX_3_250225639/V_riparia_588710_l_250225639/g' $name
sed -i "" '1 s/588710_m_C2C9HACXX_3_250225640/V_riparia_588710_m_250225640/g' $name
sed -i "" '1 s/588710_n_C2C9HACXX_3_250225641/V_riparia_588710_n_250225641/g' $name
sed -i "" '1 s/588710_o_C2C9HACXX_3_250225642/V_riparia_588710_o_250225642/g' $name
sed -i "" '1 s/588710_p_C2C9HACXX_3_250225643/V_riparia_588710_p_250225643/g' $name
sed -i "" '1 s/588710_q_C2C9HACXX_3_250225644/V_riparia_588710_q_250225644/g' $name
sed -i "" '1 s/588710_r_C2C9HACXX_3_250225645/V_riparia_588710_r_250225645/g' $name
sed -i "" '1 s/588710_s_C2C9HACXX_3_250225646/V_riparia_588710_s_250225646/g' $name
sed -i "" '1 s/588710_t_C2C9HACXX_3_250225647/V_riparia_588710_t_250225647/g' $name
sed -i "" '1 s/588710_u_C2C9HACXX_3_250225648/V_riparia_588710_u_250225648/g' $name
sed -i "" '1 s/588710_v_C2C9HACXX_3_250225649/V_riparia_588710_v_250225649/g' $name
sed -i "" '1 s/588710_w_MERGE/V_riparia_588710_w/g' $name
sed -i "" '1 s/PI588214_MERGE/V_riparia_PI588214/g' $name
sed -i "" '1 s/PI588262_MERGE/V_riparia_PI588262/g' $name
sed -i "" '1 s/V_riparia_Barret_MERGE/V_riparia_V_riparia_Barret/g' $name
sed -i "" '1 s/V_riparia_Bemidji_MERGE/V_riparia_V_riparia_Bemidji/g' $name
sed -i "" '1 s/V_riparia_Farm2_MERGE/V_riparia_V_riparia_Farm2/g' $name
sed -i "" '1 s/V_riparia_Iowa1_MERGE/V_riparia_V_riparia_Iowa1/g' $name
sed -i "" '1 s/V_riparia_Mitchell_MERGE/V_riparia_V_riparia_Mitchell/g' $name
sed -i "" '1 s/V_riparia_MNTC_MERGE/V_riparia_V_riparia_MNTC/g' $name
sed -i "" '1 s/V_riparia_MT2_MERGE/V_riparia_V_riparia_MT2/g' $name
sed -i "" '1 s/V_riparia_Okoboji_MERGE/V_riparia_V_riparia_Okoboji/g' $name
sed -i "" '1 s/V_riparia_TurnerCity_MERGE/V_riparia_V_riparia_TurnerCity/g' $name
sed -i "" '1 s/V_riparia_VT1_MERGE/V_riparia_V_riparia_VT1/g' $name
sed -i "" '1 s/V_riparia_WI2_MERGE/V_riparia_V_riparia_WI2/g' $name
sed -i "" '1 s/V_riparia35_MERGE/V_riparia_V_riparia35/g' $name
sed -i "" '1 s/Vrip1_2_C18UMACXX_5_250135409/V_riparia_Vrip1_2_250135409/g' $name
sed -i "" '1 s/Vrip1_C18UMACXX_5_250135350/V_riparia_Vrip1_250135350/g' $name
sed -i "" '1 s/Vrip2_2_C18UMACXX_5_250135421/V_riparia_Vrip2_2_250135421/g' $name
sed -i "" '1 s/Vrip2_C18UMACXX_5_250135362/V_riparia_Vrip2_250135362/g' $name
sed -i "" '1 s/Vrip3_C18UMACXX_5_250135374/V_riparia_Vrip3_250135374/g' $name
sed -i "" '1 s/Vrip4_C18UMACXX_5_250135386/V_riparia_Vrip4_250135386/g' $name
sed -i "" '1 s/Vrip5_C18UMACXX_5_250135398/V_riparia_Vrip5_250135398/g' $name
sed -i "" '1 s/Vrip6_C18UMACXX_5_250135410/V_riparia_Vrip6_250135410/g' $name
sed -i "" '1 s/LLK33_C2C7HACXX_8_250232541/V_riparia_250232541/g' $name
sed -i "" '1 s/LLK34_C2C7HACXX_8_250232542/V_riparia_250232542/g' $name
sed -i "" '1 s/LLK35_C2C7HACXX_8_250232544/V_riparia_250232544/g' $name
sed -i "" '1 s/LLK36_C2C7HACXX_8_250232545/V_riparia_250232545/g' $name
sed -i "" '1 s/597296_C2C9HACXX_3_250225318/V_romanetii_597296_250225318/g' $name
sed -i "" '1 s/597297_C2C9HACXX_3_250225314/V_romanetii_597297_250225314/g' $name
sed -i "" '1 s/DVIT2732_C0KDJACXX_1_250087437/V_romanetii_DVIT2732_250087437/g' $name
sed -i "" '1 s/588223_C0KDJACXX_1_250087471/V_rupestris_588223_250087471/g' $name
sed -i "" '1 s/588224_C0KDJACXX_1_250087436/V_rupestris_588224_250087436/g' $name
sed -i "" '1 s/588384_MERGE/V_rupestris_588384/g' $name
sed -i "" '1 s/588401_MERGE/V_rupestris_588401/g' $name
sed -i "" '1 s/588454_b_MERGE/V_rupestris_588454_b/g' $name
sed -i "" '1 s/588454_h_C2C9HACXX_3_250225500/V_rupestris_588454_h_250225500/g' $name
sed -i "" '1 s/588454_j_C2C9HACXX_3_250225501/V_rupestris_588454_j_250225501/g' $name
sed -i "" '1 s/588454_k_C2C9HACXX_3_250225502/V_rupestris_588454_k_250225502/g' $name
sed -i "" '1 s/588454_m_C2C9HACXX_3_250225578/V_rupestris_588454_m_250225578/g' $name
sed -i "" '1 s/588454_n_C2C9HACXX_3_250225579/V_rupestris_588454_n_250225579/g' $name
sed -i "" '1 s/588454_MERGE/V_rupestris_588454/g' $name
sed -i "" '1 s/588683_MERGE/V_rupestris_588683/g' $name
sed -i "" '1 s/588684_MERGE/V_rupestris_588684/g' $name
sed -i "" '1 s/AM500A_C18UMACXX_5_250135351/V_rupestris_AM500A_250135351/g' $name
sed -i "" '1 s/AM500B_C18UMACXX_5_250135363/V_rupestris_AM500B_250135363/g' $name
sed -i "" '1 s/AM500C_C18UMACXX_5_250135375/V_rupestris_AM500C_250135375/g' $name
sed -i "" '1 s/AM500D_C18UMACXX_5_250135387/V_rupestris_AM500D_250135387/g' $name
sed -i "" '1 s/AM500I_C18UMACXX_5_250135423/V_rupestris_AM500I_250135423/g' $name
sed -i "" '1 s/AM500L_C18UMACXX_5_250135352/V_rupestris_AM500L_250135352/g' $name
sed -i "" '1 s/AM500M_C18UMACXX_5_250135364/V_rupestris_AM500M_250135364/g' $name
sed -i "" '1 s/AM500Q_C18UMACXX_5_250135376/V_rupestris_AM500Q_250135376/g' $name
sed -i "" '1 s/AM500S_C18UMACXX_5_250135388/V_rupestris_AM500S_250135388/g' $name
sed -i "" '1 s/AM503_C18UMACXX_5_250135422/V_rupestris_AM503_250135422/g' $name
sed -i "" '1 s/AM504B_C18UMACXX_5_250135412/V_rupestris_AM504B_250135412/g' $name
sed -i "" '1 s/AM504C_C18UMACXX_5_250135424/V_rupestris_AM504C_250135424/g' $name
sed -i "" '1 s/AM504D_C18UMACXX_5_250135341/V_rupestris_AM504D_250135341/g' $name
sed -i "" '1 s/AM504E_C18UMACXX_5_250135353/V_rupestris_AM504E_250135353/g' $name
sed -i "" '1 s/AM504F_C18UMACXX_5_250135365/V_rupestris_AM504F_250135365/g' $name
sed -i "" '1 s/AM504G_C18UMACXX_5_250135377/V_rupestris_AM504G_250135377/g' $name
sed -i "" '1 s/AM513A_C18UMACXX_5_250135389/V_rupestris_AM513A_250135389/g' $name
sed -i "" '1 s/AM513AA_C18UMACXX_5_250135399/V_rupestris_AM513AA_250135399/g' $name
sed -i "" '1 s/AM513BB_C18UMACXX_5_250135411/V_rupestris_AM513BB_250135411/g' $name
sed -i "" '1 s/AM513C_C18UMACXX_5_250135401/V_rupestris_AM513C_250135401/g' $name
sed -i "" '1 s/AM513CC_C18UMACXX_5_250135340/V_rupestris_AM513CC_250135340/g' $name
sed -i "" '1 s/AM513DD_C18UMACXX_5_250135400/V_rupestris_AM513DD_250135400/g' $name
sed -i "" '1 s/AM513EE_C18UMACXX_5_250135413/V_rupestris_AM513EE_250135413/g' $name
sed -i "" '1 s/AM513FF_C18UMACXX_5_250135425/V_rupestris_AM513FF_250135425/g' $name
sed -i "" '1 s/AM513GG_C18UMACXX_5_250135342/V_rupestris_AM513GG_250135342/g' $name
sed -i "" '1 s/AM513HH_C18UMACXX_5_250135354/V_rupestris_AM513HH_250135354/g' $name
sed -i "" '1 s/AM513I_C18UMACXX_5_250135366/V_rupestris_AM513I_250135366/g' $name
sed -i "" '1 s/AM513II_C18UMACXX_5_250135378/V_rupestris_AM513II_250135378/g' $name
sed -i "" '1 s/AM513JJ_C18UMACXX_5_250135390/V_rupestris_AM513JJ_250135390/g' $name
sed -i "" '1 s/AM513KK_C18UMACXX_5_250135402/V_rupestris_AM513KK_250135402/g' $name
sed -i "" '1 s/AM513LL_C18UMACXX_5_250135414/V_rupestris_AM513LL_250135414/g' $name
sed -i "" '1 s/AM523_C18UMACXX_5_250135434/V_rupestris_AM523_250135434/g' $name
sed -i "" '1 s/Vrup_100_V2_C28DTACXX_2_250190225/V_rupestris_Vrup_100_V2_250190225/g' $name
sed -i "" '1 s/Vrup_101_V2_C28DTACXX_2_250190226/V_rupestris_Vrup_101_V2_250190226/g' $name
sed -i "" '1 s/Vrup_104_V2_C28DTACXX_2_250190227/V_rupestris_Vrup_104_V2_250190227/g' $name
sed -i "" '1 s/Vrup_105_V2_C28DTACXX_2_250190228/V_rupestris_Vrup_105_V2_250190228/g' $name
sed -i "" '1 s/Vrup_108_V2_C28DTACXX_2_250190229/V_rupestris_Vrup_108_V2_250190229/g' $name
sed -i "" '1 s/Vrup_110_V2_C28DTACXX_2_250190230/V_rupestris_Vrup_110_V2_250190230/g' $name
sed -i "" '1 s/Vrup_111_V2_C28DTACXX_2_250190231/V_rupestris_Vrup_111_V2_250190231/g' $name
sed -i "" '1 s/Vrup_112_V2_C28DTACXX_2_250190232/V_rupestris_Vrup_112_V2_250190232/g' $name
sed -i "" '1 s/Vrup_119_V2_C28DTACXX_2_250190233/V_rupestris_Vrup_119_V2_250190233/g' $name
sed -i "" '1 s/Vrup_120_V2_C28DTACXX_2_250190234/V_rupestris_Vrup_120_V2_250190234/g' $name
sed -i "" '1 s/Vrup_123_V2_C28DTACXX_2_250190235/V_rupestris_Vrup_123_V2_250190235/g' $name
sed -i "" '1 s/Vrup_49_V2_C28DTACXX_2_250190204/V_rupestris_Vrup_49_V2_250190204/g' $name
sed -i "" '1 s/Vrup_53_V2_C28DTACXX_2_250190205/V_rupestris_Vrup_53_V2_250190205/g' $name
sed -i "" '1 s/Vrup_54_V2_C28DTACXX_2_250190206/V_rupestris_Vrup_54_V2_250190206/g' $name
sed -i "" '1 s/Vrup_55_V2_C28DTACXX_2_250190207/V_rupestris_Vrup_55_V2_250190207/g' $name
sed -i "" '1 s/Vrup_56_V2_C28DTACXX_2_250190208/V_rupestris_Vrup_56_V2_250190208/g' $name
sed -i "" '1 s/Vrup_57_V2_C28DTACXX_2_250190209/V_rupestris_Vrup_57_V2_250190209/g' $name
sed -i "" '1 s/Vrup_60_V2_C28DTACXX_2_250190210/V_rupestris_Vrup_60_V2_250190210/g' $name
sed -i "" '1 s/Vrup_72_V2_C28DTACXX_2_250190211/V_rupestris_Vrup_72_V2_250190211/g' $name
sed -i "" '1 s/Vrup_75_V2_C28DTACXX_2_250190212/V_rupestris_Vrup_75_V2_250190212/g' $name
sed -i "" '1 s/Vrup_76_V2_C28DTACXX_2_250190213/V_rupestris_Vrup_76_V2_250190213/g' $name
sed -i "" '1 s/Vrup_77_V2_C28DTACXX_2_250190214/V_rupestris_Vrup_77_V2_250190214/g' $name
sed -i "" '1 s/Vrup_79_V2_C28DTACXX_2_250190215/V_rupestris_Vrup_79_V2_250190215/g' $name
sed -i "" '1 s/Vrup_80_V2_C28DTACXX_2_250190216/V_rupestris_Vrup_80_V2_250190216/g' $name
sed -i "" '1 s/Vrup_81_V2_C28DTACXX_2_250190217/V_rupestris_Vrup_81_V2_250190217/g' $name
sed -i "" '1 s/Vrup_82_V2_C28DTACXX_2_250190218/V_rupestris_Vrup_82_V2_250190218/g' $name
sed -i "" '1 s/Vrup_84_V2_C28DTACXX_2_250190219/V_rupestris_Vrup_84_V2_250190219/g' $name
sed -i "" '1 s/Vrup_85_V2_C28DTACXX_2_250190220/V_rupestris_Vrup_85_V2_250190220/g' $name
sed -i "" '1 s/Vrup_86_V2_C28DTACXX_2_250190221/V_rupestris_Vrup_86_V2_250190221/g' $name
sed -i "" '1 s/Vrup_87_V2_C28DTACXX_2_250190222/V_rupestris_Vrup_87_V2_250190222/g' $name
sed -i "" '1 s/Vrup_88_V2_C28DTACXX_2_250190223/V_rupestris_Vrup_88_V2_250190223/g' $name
sed -i "" '1 s/Vrup_92_V2_C28DTACXX_2_250190224/V_rupestris_Vrup_92_V2_250190224/g' $name
sed -i "" '1 s/Vrup102_C18UMACXX_5_250135419/V_rupestris_Vrup102_250135419/g' $name
sed -i "" '1 s/Vrup103_C18UMACXX_5_250135431/V_rupestris_Vrup103_250135431/g' $name
sed -i "" '1 s/Vrup105_C18UMACXX_5_250135348/V_rupestris_Vrup105_250135348/g' $name
sed -i "" '1 s/Vrup106_C18UMACXX_5_250135360/V_rupestris_Vrup106_250135360/g' $name
sed -i "" '1 s/Vrup107_C18UMACXX_5_250135384/V_rupestris_Vrup107_250135384/g' $name
sed -i "" '1 s/Vrup108_C18UMACXX_5_250135372/V_rupestris_Vrup108_250135372/g' $name
sed -i "" '1 s/Vrup109_C18UMACXX_5_250135396/V_rupestris_Vrup109_250135396/g' $name
sed -i "" '1 s/Vrup112_C18UMACXX_5_250135408/V_rupestris_Vrup112_250135408/g' $name
sed -i "" '1 s/Vrup113_C18UMACXX_5_250135420/V_rupestris_Vrup113_250135420/g' $name
sed -i "" '1 s/Vrup114_C18UMACXX_5_250135432/V_rupestris_Vrup114_250135432/g' $name
sed -i "" '1 s/Vrup115_C18UMACXX_5_250135349/V_rupestris_Vrup115_250135349/g' $name
sed -i "" '1 s/Vrup116_C18UMACXX_5_250135361/V_rupestris_Vrup116_250135361/g' $name
sed -i "" '1 s/Vrup118_C18UMACXX_5_250135373/V_rupestris_Vrup118_250135373/g' $name
sed -i "" '1 s/Vrup120_C18UMACXX_5_250135385/V_rupestris_Vrup120_250135385/g' $name
sed -i "" '1 s/Vrup36_C18UMACXX_5_250135343/V_rupestris_Vrup36_250135343/g' $name
sed -i "" '1 s/Vrup37_C18UMACXX_5_250135355/V_rupestris_Vrup37_250135355/g' $name
sed -i "" '1 s/Vrup38_C18UMACXX_5_250135367/V_rupestris_Vrup38_250135367/g' $name
sed -i "" '1 s/Vrup39_C18UMACXX_5_250135379/V_rupestris_Vrup39_250135379/g' $name
sed -i "" '1 s/Vrup41_C18UMACXX_5_250135391/V_rupestris_Vrup41_250135391/g' $name
sed -i "" '1 s/Vrup42_C18UMACXX_5_250135403/V_rupestris_Vrup42_250135403/g' $name
sed -i "" '1 s/Vrup44_C18UMACXX_5_250135415/V_rupestris_Vrup44_250135415/g' $name
sed -i "" '1 s/Vrup45_C18UMACXX_5_250135427/V_rupestris_Vrup45_250135427/g' $name
sed -i "" '1 s/Vrup46_C18UMACXX_5_250135344/V_rupestris_Vrup46_250135344/g' $name
sed -i "" '1 s/Vrup48_C18UMACXX_5_250135356/V_rupestris_Vrup48_250135356/g' $name
sed -i "" '1 s/Vrup49_C18UMACXX_5_250135368/V_rupestris_Vrup49_250135368/g' $name
sed -i "" '1 s/Vrup50_C18UMACXX_5_250135380/V_rupestris_Vrup50_250135380/g' $name
sed -i "" '1 s/Vrup51_C18UMACXX_5_250135392/V_rupestris_Vrup51_250135392/g' $name
sed -i "" '1 s/Vrup52_C18UMACXX_5_250135404/V_rupestris_Vrup52_250135404/g' $name
sed -i "" '1 s/Vrup55_C18UMACXX_5_250135416/V_rupestris_Vrup55_250135416/g' $name
sed -i "" '1 s/Vrup61_C18UMACXX_5_250135428/V_rupestris_Vrup61_250135428/g' $name
sed -i "" '1 s/Vrup72_C18UMACXX_5_250135345/V_rupestris_Vrup72_250135345/g' $name
sed -i "" '1 s/Vrup73_C18UMACXX_5_250135357/V_rupestris_Vrup73_250135357/g' $name
sed -i "" '1 s/Vrup75_C18UMACXX_5_250135369/V_rupestris_Vrup75_250135369/g' $name
sed -i "" '1 s/Vrup76_C18UMACXX_5_250135381/V_rupestris_Vrup76_250135381/g' $name
sed -i "" '1 s/Vrup77_C18UMACXX_5_250135393/V_rupestris_Vrup77_250135393/g' $name
sed -i "" '1 s/Vrup78_C18UMACXX_5_250135405/V_rupestris_Vrup78_250135405/g' $name
sed -i "" '1 s/Vrup79_C18UMACXX_5_250135417/V_rupestris_Vrup79_250135417/g' $name
sed -i "" '1 s/Vrup82_C18UMACXX_5_250135429/V_rupestris_Vrup82_250135429/g' $name
sed -i "" '1 s/Vrup83_C18UMACXX_5_250135346/V_rupestris_Vrup83_250135346/g' $name
sed -i "" '1 s/Vrup84_C18UMACXX_5_250135358/V_rupestris_Vrup84_250135358/g' $name
sed -i "" '1 s/Vrup85_C18UMACXX_5_250135370/V_rupestris_Vrup85_250135370/g' $name
sed -i "" '1 s/Vrup88_C18UMACXX_5_250135382/V_rupestris_Vrup88_250135382/g' $name
sed -i "" '1 s/Vrup89_C18UMACXX_5_250135394/V_rupestris_Vrup89_250135394/g' $name
sed -i "" '1 s/Vrup90_C18UMACXX_5_250135406/V_rupestris_Vrup90_250135406/g' $name
sed -i "" '1 s/Vrup91_C18UMACXX_5_250135418/V_rupestris_Vrup91_250135418/g' $name
sed -i "" '1 s/Vrup92_C18UMACXX_5_250135430/V_rupestris_Vrup92_250135430/g' $name
sed -i "" '1 s/Vrup93_C18UMACXX_5_250135347/V_rupestris_Vrup93_250135347/g' $name
sed -i "" '1 s/Vrup94_2_C18UMACXX_5_250135397/V_rupestris_Vrup94_2_250135397/g' $name
sed -i "" '1 s/Vrup94_C18UMACXX_5_250135359/V_rupestris_Vrup94_250135359/g' $name
sed -i "" '1 s/Vrup95_C18UMACXX_5_250135371/V_rupestris_Vrup95_250135371/g' $name
sed -i "" '1 s/Vrup96_C18UMACXX_5_250135383/V_rupestris_Vrup96_250135383/g' $name
sed -i "" '1 s/Vrup98_C18UMACXX_5_250135395/V_rupestris_Vrup98_250135395/g' $name
sed -i "" '1 s/Vrup99_C18UMACXX_5_250135407/V_rupestris_Vrup99_250135407/g' $name
sed -i "" '1 s/588476_C2C9HACXX_3_250225311/V_spp_588476_250225311/g' $name
sed -i "" '1 s/DVIT1377_C0KDJACXX_1_250087438/V_treleasei_DVIT1377_250087438/g' $name
sed -i "" '1 s/DVIT1410_C0KDJACXX_1_250087450/V_treleasei_DVIT1410_250087450/g' $name
sed -i "" '1 s/LLK248_C2C7HACXX_6_250241163/V_cinerea_250241163/g' $name
sed -i "" '1 s/LLK298_C2C7HACXX_6_250241124/V_cinerea_250241124/g' $name
sed -i "" '1 s/LLK305_C2C7HACXX_6_250241129/V_cinerea_250241129/g' $name
sed -i "" '1 s/LLK183_C2C7HACXX_6_250241136/V_cinerea_250241136/g' $name
sed -i "" '1 s/LLK187_C2C7HACXX_6_250241135/V_riparia_250241135/g' $name
sed -i "" '1 s/LLK179_C2C7HACXX_6_250241146/V_riparia_250241146/g' $name
sed -i "" '1 s/LLK232_C2C7HACXX_6_250241168/V_riparia_250241168/g' $name
sed -i "" '1 s/LLK163_C2C7HACXX_6_250241148/V_riparia_250241148/g' $name
sed -i "" '1 s/LLK240_C2C7HACXX_6_250241164/V_riparia_250241164/g' $name
sed -i "" '1 s/LLK270_C2C7HACXX_6_250241178/V_riparia_250241178/g' $name
sed -i "" '1 s/LLK262_C2C7HACXX_6_250241171/V_riparia_250241171/g' $name
sed -i "" '1 s/LLK297_C2C7HACXX_6_250241116/V_riparia_250241116/g' $name
sed -i "" '1 s/LLK164_C2C7HACXX_6_250241155/V_riparia_250241155/g' $name
sed -i "" '1 s/LLK166_C2C7HACXX_6_250241151/V_riparia_250241151/g' $name
sed -i "" '1 s/LLK167_C2C7HACXX_6_250241144/V_riparia_250241144/g' $name
sed -i "" '1 s/LLK168_C2C7HACXX_6_250241150/V_riparia_250241150/g' $name
sed -i "" '1 s/LLK172_C2C7HACXX_6_250241137/V_riparia_250241137/g' $name
sed -i "" '1 s/LLK176_C2C7HACXX_6_250241154/V_riparia_250241154/g' $name
sed -i "" '1 s/LLK186_C2C7HACXX_6_250241156/V_riparia_250241156/g' $name
sed -i "" '1 s/LLK267_C2C7HACXX_6_250241172/V_riparia_250241172/g' $name
sed -i "" '1 s/LLK294_MERGE/V_riparia_LLK294/g' $name
sed -i "" '1 s/LLK223_C2C7HACXX_6_250241169/V_riparia_250241169/g' $name
sed -i "" '1 s/LLK174_C2C7HACXX_6_250241147/V_rupestris_250241147/g' $name
sed -i "" '1 s/LLK177_C2C7HACXX_6_250241153/V_rupestris_250241153/g' $name
sed -i "" '1 s/LLK181_MERGE/V_rupestris_LLK181/g' $name
sed -i "" '1 s/LLK178_C2C7HACXX_6_250241143/V_rupestris_250241143/g' $name
sed -i "" '1 s/LLK182_C2C7HACXX_6_250241142/V_rupestris_250241142/g' $name
sed -i "" '1 s/Early_Muscat_MERGE/V_vinifera_Early_Muscat/g' $name
sed -i "" '1 s/Merlot-lub_C1B3NACXX_1_250117205/V_vinifera_Merlot-lub_250117205/g' $name
sed -i "" '1 s/Pinot_Noir_MERGE/V_vinifera_Pinot_Noir/g' $name
sed -i "" '1 s/Pixie-cad_MERGE/V_vinifera_Pixie-cad/g' $name
sed -i "" '1 s/Rubired_MERGE/V_vinifera_Rubired/g' $name
sed -i "" '1 s/Scarlet_Royal_C0DBVACXX_6_250073382/V_vinifera_Scarlet_Royal_250073382/g' $name
sed -i "" '1 s/Zengoe_C0DBVACXX_5_250072636/V_vinifera_Zengoe_250072636/g' $name
sed -i "" '1 s/Autumn_King_MERGE/V_vitis_Autumn_King/g' $name
sed -i "" '1 s/Cabernet_Sauvignon-cad_MERGE/V_vitis_Cabernet_Sauvignon-cad/g' $name
sed -i "" '1 s/Chardonnay-lub_C1B3NACXX_1_250117206/V_vitis_Chardonnay-lub_250117206/g' $name
sed -i "" '1 s/Chardonnay-rei_MERGE/V_vitis_Chardonnay-rei/g' $name
sed -i "" '1 s/Chardonnay_MERGE/V_vitis_Chardonnay/g' $name
sed -i "" '1 s/LLK233_C2C7HACXX_6_250241170/V_Vitis_aestivalis_250241170/g' $name
sed -i "" '1 s/LLK243_C2C7HACXX_6_250241166/V_Vitis_cinerea_250241166/g' $name
sed -i "" '1 s/LLK254_C2C7HACXX_6_250241167/V_Vitis_cinerea_V_aestivalis_250241167/g' $name
sed -i "" '1 s/LLK160_C2C7HACXX_6_250241139/V_Vitis_250241139/g' $name
sed -i "" '1 s/LLK161_C2C7HACXX_6_250241160/V_Vitis_250241160/g' $name
sed -i "" '1 s/LLK258_C2C7HACXX_6_250241173/V_Vitis_250241173/g' $name
sed -i "" '1 s/LLK269_C2C7HACXX_6_250241175/V_Vitis_rupestris_250241175/g' $name
sed -i "" '1 s/LLK42_C2C7HACXX_6_250241113/V_Vitis_sp_aestivalis_250241113/g' $name
sed -i "" '1 s/LLK43_C2C7HACXX_6_250241109/V_Vitis_sp_aestivalis_250241109/g' $name
sed -i "" '1 s/LLK44_C2C7HACXX_6_250241111/V_Vitis_sp_aestivalis_250241111/g' $name
sed -i "" '1 s/LLK45_C2C7HACXX_6_250241112/V_Vitis_sp_aestivalis_250241112/g' $name
sed -i "" '1 s/LLK46_C2C7HACXX_6_250241110/V_Vitis_sp_aestivalis_250241110/g' $name
sed -i "" '1 s/055_1_C28DTACXX_2_250189971/V_vulpina_055_1_250189971/g' $name
sed -i "" '1 s/055_2_C28DTACXX_2_250189972/V_vulpina_055_2_250189972/g' $name
sed -i "" '1 s/055_4_C28DTACXX_2_250189973/V_vulpina_055_4_250189973/g' $name
sed -i "" '1 s/055_5_C28DTACXX_2_250190347/V_vulpina_055_5_250190347/g' $name
sed -i "" '1 s/057_1_C28DTACXX_2_250190004/V_vulpina_057_1_250190004/g' $name
sed -i "" '1 s/057_2_C28DTACXX_2_250190005/V_vulpina_057_2_250190005/g' $name
sed -i "" '1 s/057_3_C28DTACXX_2_250190357/V_vulpina_057_3_250190357/g' $name
sed -i "" '1 s/057_4_C28DTACXX_2_250190006/V_vulpina_057_4_250190006/g' $name
sed -i "" '1 s/059_1_C28DTACXX_2_250189951/V_vulpina_059_1_250189951/g' $name
sed -i "" '1 s/059_2_C28DTACXX_2_250189952/V_vulpina_059_2_250189952/g' $name
sed -i "" '1 s/059_3_C28DTACXX_2_250189953/V_vulpina_059_3_250189953/g' $name
sed -i "" '1 s/059_4_C28DTACXX_2_250190331/V_vulpina_059_4_250190331/g' $name
sed -i "" '1 s/059_5_MERGE/V_vulpina_059_5/g' $name
sed -i "" '1 s/059_6_C28DTACXX_2_250190333/V_vulpina_059_6_250190333/g' $name
sed -i "" '1 s/059_7_C28DTACXX_2_250190334/V_vulpina_059_7_250190334/g' $name
sed -i "" '1 s/064_1_C28DTACXX_2_250190010/V_vulpina_064_1_250190010/g' $name
sed -i "" '1 s/064_2a_C28DTACXX_2_250190361/V_vulpina_064_2a_250190361/g' $name
sed -i "" '1 s/064_2b_C28DTACXX_2_250190362/V_vulpina_064_2b_250190362/g' $name
sed -i "" '1 s/064_3_C28DTACXX_2_250190011/V_vulpina_064_3_250190011/g' $name
sed -i "" '1 s/064_4_C28DTACXX_2_250190012/V_vulpina_064_4_250190012/g' $name
sed -i "" '1 s/064_5_C28DTACXX_2_250190363/V_vulpina_064_5_250190363/g' $name
sed -i "" '1 s/483180_MERGE/V_vulpina_483180/g' $name
sed -i "" '1 s/483184_MERGE/V_vulpina_483184/g' $name
sed -i "" '1 s/483186_MERGE/V_vulpina_483186/g' $name
sed -i "" '1 s/483187_MERGE/V_vulpina_483187/g' $name
sed -i "" '1 s/483188_MERGE/V_vulpina_483188/g' $name
sed -i "" '1 s/483189_MERGE/V_vulpina_483189/g' $name
sed -i "" '1 s/483190_MERGE/V_vulpina_483190/g' $name
sed -i "" '1 s/588133_MERGE/V_vulpina_588133/g' $name
sed -i "" '1 s/588142_MERGE/V_vulpina_588142/g' $name
sed -i "" '1 s/588589_a_MERGE/V_vulpina_588589_a/g' $name
sed -i "" '1 s/588589_c_C2C9HACXX_3_250225583/V_vulpina_588589_c_250225583/g' $name
sed -i "" '1 s/588589_e_C2C9HACXX_3_250225584/V_vulpina_588589_e_250225584/g' $name
sed -i "" '1 s/588589_f_C2C9HACXX_3_250225585/V_vulpina_588589_f_250225585/g' $name
sed -i "" '1 s/588589_g_C2C9HACXX_3_250225586/V_vulpina_588589_g_250225586/g' $name
sed -i "" '1 s/588589_j_C2C9HACXX_3_250225587/V_vulpina_588589_j_250225587/g' $name
sed -i "" '1 s/588589_k_C2C9HACXX_3_250225588/V_vulpina_588589_k_250225588/g' $name
sed -i "" '1 s/588589_l_C2C9HACXX_3_250225589/V_vulpina_588589_l_250225589/g' $name
sed -i "" '1 s/588589_m_C2C9HACXX_3_250225590/V_vulpina_588589_m_250225590/g' $name
sed -i "" '1 s/588589_n_C2C9HACXX_3_250225591/V_vulpina_588589_n_250225591/g' $name
sed -i "" '1 s/588589_o_C2C9HACXX_3_250225592/V_vulpina_588589_o_250225592/g' $name
sed -i "" '1 s/588589_p_C2C9HACXX_3_250225593/V_vulpina_588589_p_250225593/g' $name
sed -i "" '1 s/588591_b_C2C9HACXX_3_250225504/V_vulpina_588591_b_250225504/g' $name
sed -i "" '1 s/588591_c_C2C9HACXX_3_250225505/V_vulpina_588591_c_250225505/g' $name
sed -i "" '1 s/588591_d_C2C9HACXX_3_250225506/V_vulpina_588591_d_250225506/g' $name
sed -i "" '1 s/588591_e_C2C9HACXX_3_250225507/V_vulpina_588591_e_250225507/g' $name
sed -i "" '1 s/588591_f_C2C9HACXX_3_250225508/V_vulpina_588591_f_250225508/g' $name
sed -i "" '1 s/588591_g_C2C9HACXX_3_250225509/V_vulpina_588591_g_250225509/g' $name
sed -i "" '1 s/588591_h_C2C9HACXX_3_250225510/V_vulpina_588591_h_250225510/g' $name
sed -i "" '1 s/588591_i_C2C9HACXX_3_250225511/V_vulpina_588591_i_250225511/g' $name
sed -i "" '1 s/588591_j_C2C9HACXX_3_250225512/V_vulpina_588591_j_250225512/g' $name
sed -i "" '1 s/588591_k_MERGE/V_vulpina_588591_k/g' $name
sed -i "" '1 s/588591_l_C2C9HACXX_3_250225514/V_vulpina_588591_l_250225514/g' $name
sed -i "" '1 s/588591_m_C2C9HACXX_3_250225515/V_vulpina_588591_m_250225515/g' $name
sed -i "" '1 s/588679_MERGE/V_vulpina_588679/g' $name
sed -i "" '1 s/588680_MERGE/V_vulpina_588680/g' $name
sed -i "" '1 s/597115_MERGE/V_vulpina_597115/g' $name
sed -i "" '1 s/588421_b_C2C9HACXX_3_250225364/V_yenshanensis_588421_b_250225364/g' $name
sed -i "" '1 s/588421_c_C2C9HACXX_3_250225365/V_yenshanensis_588421_c_250225365/g' $name
sed -i "" '1 s/588421_d_C2C9HACXX_3_250225366/V_yenshanensis_588421_d_250225366/g' $name
sed -i "" '1 s/588421_e_C2C9HACXX_3_250225367/V_yenshanensis_588421_e_250225367/g' $name
sed -i "" '1 s/588421_f_C2C9HACXX_3_250225368/V_yenshanensis_588421_f_250225368/g' $name
sed -i "" '1 s/588421_h_C2C9HACXX_3_250225370/V_yenshanensis_588421_h_250225370/g' $name
sed -i "" '1 s/588421_i_C2C9HACXX_3_250225371/V_yenshanensis_588421_i_250225371/g' $name
sed -i "" '1 s/588421_j_C2C9HACXX_3_250225372/V_yenshanensis_588421_j_250225372/g' $name
sed -i "" '1 s/588421_k_C2C9HACXX_3_250225373/V_yenshanensis_588421_k_250225373/g' $name
sed -i "" '1 s/588421_l_C2C9HACXX_3_250225374/V_yenshanensis_588421_l_250225374/g' $name
sed -i "" '1 s/588421_m_C2C9HACXX_3_250225375/V_yenshanensis_588421_m_250225375/g' $name
sed -i "" '1 s/588421_n_C2C9HACXX_3_250225376/V_yenshanensis_588421_n_250225376/g' $name
sed -i "" '1 s/588421_o_C2C9HACXX_3_250225377/V_yenshanensis_588421_o_250225377/g' $name
sed -i "" '1 s/588421_p_MERGE/V_yenshanensis_588421_p/g' $name
sed -i "" '1 s/588421_q_C2C9HACXX_3_250225379/V_yenshanensis_588421_q_250225379/g' $name
sed -i "" '1 s/588421_r_C2C9HACXX_3_250225380/V_yenshanensis_588421_r_250225380/g' $name
sed -i "" '1 s/588421_s_C2C9HACXX_3_250225381/V_yenshanensis_588421_s_250225381/g' $name
sed -i "" '1 s/588421_u_C2C9HACXX_3_250225382/V_yenshanensis_588421_u_250225382/g' $name
sed -i "" '1 s/588421_v_C2C9HACXX_3_250225383/V_yenshanensis_588421_v_250225383/g' $name
sed -i "" '1 s/588421_w_C2C9HACXX_3_250225384/V_yenshanensis_588421_w_250225384/g' $name
sed -i "" '1 s/588422_c_C2C9HACXX_3_250225469/V_yenshanensis_588422_c_250225469/g' $name
sed -i "" '1 s/588422_d_C2C9HACXX_3_250225470/V_yenshanensis_588422_d_250225470/g' $name
sed -i "" '1 s/588422_e_C2C9HACXX_3_250225471/V_yenshanensis_588422_e_250225471/g' $name
sed -i "" '1 s/588422_f_MERGE/V_yenshanensis_588422_f/g' $name
sed -i "" '1 s/588422_h_C2C9HACXX_3_250225473/V_yenshanensis_588422_h_250225473/g' $name
sed -i "" '1 s/588422_i_C2C9HACXX_3_250225474/V_yenshanensis_588422_i_250225474/g' $name
sed -i "" '1 s/588422_j_C2C9HACXX_3_250225475/V_yenshanensis_588422_j_250225475/g' $name

echo ""
echo "Finished"
echo ""


```


## Making data matrices for phylogenetic analyses

There are two programs that I cannot live without while working with DNA sequences. Both of them deal with format conversion (e.g., fasta to nexus) or concatenation very smoothly. These programs are:

Download and install [Phyutility](https://code.google.com/archive/p/phyutility/downloads) to do file format conversion.

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

Start with a file with all loci (NSPs) concatenated into a NEXUS file. Get the latest command-line version of [Paup](https://people.sc.fsu.edu/~dswofford/paup_test/) and type the following:

```
paup

#Within Paup

exe file.nex

#No Bootstrap
SVDQuartets nthreads=[number of processors] nquartets=10000000 [or other number]

#Save the tree
SaveTrees file = Vitis_SVDquartet.tre format = Newick brLens = yes supportValues = Both trees = all

#With Bootstrap
SVDQuartets nthreads=25 nquartets=10000000 bootstrap=standard nreps=50 treeFile= Vitis_SVDquartet_Bootstrap.trees


```



