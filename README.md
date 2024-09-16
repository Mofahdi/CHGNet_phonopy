# CHGNet_phonopy
code to generate 2nd order interatomic force constants from phonopy using CHGNet

you can test the code by running the following:</br>
<code>
python chgnet_phonopy_run.py "\"
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
