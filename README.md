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
the code will generate these files: 
1-**FORCE_CONSTANTS**: 2nd order IFCs in phonopy format
2-**stability**: it shows the words "stable" or "unstable" based on the "stability_criteria" argument
3- **band.conf**: file that can be used later by phonopy to plot the phonon dispersion
4- **orig_band.conf**: file that has the q-points or phonon wavevectors that were used to get the frequencies to output the **stability** file
5- **SPOSCAR_###**: # represents the supercell dimension

## args explanation
**--atoms_path**: structure path ('./POSCAR' by default) \
**--relax**: whether chgnet will relax the structure or not (False by default) \
**--supercell-dims**: supercell dimensions (222 by default)\
**--disp**: atomic displacement amplitude in Angstroms (0.01 by default)\
**--num_rand_disp**: # of random displacements. you might have to install alm to produce 2nd order IFCs (None by default) \
**--output_disp**: whether to output the displacements in POSCAR format or not (True by default)\
**--pretrained_model**: whether to use the pretrained chgnet model (True by default)\
**--model_path**: new chgnet model path if the pretrained model is not used (None by default)\
**--stability_criteria**: frequency stability threshold. If one frequency is less than that value, "unstable" is written on **stability** file (-0.1 by default)\
**--output_ph_band**: output phonon dispersion plot in file **phonopy_bands_dos.png**(True by default)\

## credit
* please cite this work since the code was used to produce it:</br>
Ojih, J.; Al-Fahdi, M.; Yao, Y.; Hu, J.; Hu, M. Graph Theory and Graph Neural Network Assisted High-Throughput Crystal Structure Prediction and Screening for Energy Conversion and Storage. **Journal of Materials Chemistry A** *2024*, 12 (14), 8502–8515

* also please consider reading my published work in Google Scholar using this [link](https://scholar.google.com/citations?user=5tkWy4AAAAAJ&hl=en&oi=ao) thank you :)
