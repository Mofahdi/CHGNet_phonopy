# CHGNet_phonopy
code to generate 2nd order interatomic force constants from phonopy using CHGNet

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

* please cite this work since the code was used to produce it:</br>
Ojih, J.; Al-Fahdi, M.; Yao, Y.; Hu, J.; Hu, M. Graph Theory and Graph Neural Network Assisted High-Throughput Crystal Structure Prediction and Screening for Energy Conversion and Storage. Journal of Materials Chemistry A 2024, 12 (14), 8502–8515

* also please consider reading my published work in Google Scholar using this [link](https://scholar.google.com/citations?user=5tkWy4AAAAAJ&hl=en&oi=ao) thank you :)
