# CHGNet_phonopy
code to generate 2nd order interatomic force constants from phonopy using CHGNet

## Usage
you can test the code by running the following:</br>

<code>
python chgnet_phonopy_run.py \
	--atoms_path='POSCAR' \
	--relax=True \
	--supercell-dims=222 \
	--disp=0.02 \
	--num_rand_disp=None \
	--output_disp=True \
	--pretrained_model=True \
	--model_path=None \
	--stability_criteria=-0.1 \
	--output_ph_band=True
</code>
</br>
the code will generate these files: </br>
1-**FORCE_CONSTANTS**: 2nd order IFCs in phonopy format</br>
2-**stability**: it shows the words "stable" or "unstable" based on the "stability_criteria" argument</br>
3- **band.conf**: file that can be used later by phonopy to plot the phonon dispersion</br>
4- **orig_band.conf**: file that has the q-points or phonon wavevectors that were used to get the frequencies to output the **stability** file</br>
5- **SPOSCAR_###**: supercell of the input structure where # represents the supercell dimension</br>
</br>
**Note:** you have to put both files "*chgnet_phonopy_class.py*" and "*chgnet_phonopy_run.py*" in the same path since "*chgnet_phonopy_run.py*" inherits classes from "*chgnet_phonopy_class.py*". The code will output the above files in the same path where you put "*chgnet_phonopy_class.py*" and "*chgnet_phonopy_run.py*".

## Args Explanation
**--atoms_path**: structure path ('./POSCAR' by default) \
**--relax**: whether chgnet will relax the structure before the displacments or not (False by default) \
**--supercell-dims**: supercell dimensions (222 by default)\
**--disp**: atomic displacement amplitude in Angstroms (0.01 by default)\
**--num_rand_disp**: # of random displacements. you might have to install alm to produce 2nd order IFCs (None by default) \
**--output_disp**: whether to output the displacements in POSCAR format or not (True by default)\
**--pretrained_model**: whether to use the pretrained chgnet model (True by default)\
**--model_path**: new chgnet model path if the pretrained model is not used (None by default)\
**--stability_criteria**: frequency stability threshold. If one frequency is less than that value, "unstable" is written on **stability** file (-0.1 by default)\
**--output_ph_band**: output phonon dispersion plot in file **phonopy_bands_dos.png**(True by default)\

## Required Packages
the code is tested on the following packages and versions:
<code>torch=2.0.1</code>
<code>pymatgen=2023.11.12</code>
<code>ase=3.23.0</code>
<code>chgnet=0.3.5</code>
<code>phonopy=2.20.0</code>
</br>The code can probably work with different versions of the above packages

## Credit and Citation
* please cite this journal article below since the code was used to produce the article:</br>
Ojih, J.; Al-Fahdi, M.; Yao, Y.; Hu, J.; Hu, M. Graph Theory and Graph Neural Network Assisted High-Throughput Crystal Structure Prediction and Screening for Energy Conversion and Storage. **Journal of Materials Chemistry A** *2024*, 12 (14), 8502–8515
*  please consider reading my published work in Google Scholar using this [link](https://scholar.google.com/citations?user=5tkWy4AAAAAJ&hl=en&oi=ao) thank you :)
*  also please let me know if more features are needed to be added and/or improved 
