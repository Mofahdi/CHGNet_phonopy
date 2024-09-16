import argparse
import sys, os
from typing import Union
from chgnet_phonopy_class import *
# packages needed:
# 1- chgnet
# 2- phonopy
# 3- pymatgen
# 4- jarvis-tools
#
# output POSCARs 
# another band.conf file with ASE high symm path

def none_or_val(value):
	if value == 'None':
		return None
	return int(value)

def bool_vals(value):
	if value.lower() == 'true':
		return True
	if value.lower() == 'false':
		return False

parser = argparse.ArgumentParser(description='chgnet inputs')
parser.add_argument('--atoms_path', default='./POSCAR', type=str)
parser.add_argument('--relax', default=False, type=bool_vals)

parser.add_argument('--supercell-dims','-scell-dims', default=["2", "2", "2"], type=list)
parser.add_argument('--disp', default=0.01, type=float)
parser.add_argument('--num_rand_disp', default=None, type=none_or_val)
parser.add_argument('--output_disp', default=True, type=bool_vals)

parser.add_argument('--pretrained_model', default=True, type=bool_vals)
parser.add_argument('--model_path', default='./', type=str)

parser.add_argument('--stability_criteria', default=-0.1, type=float)
parser.add_argument('--output_ph_band', default=True, type=bool_vals)

args = parser.parse_args(sys.argv[1:])

pmg_struc=Structure.from_file(args.atoms_path)
if args.relax:
	from chgnet.model import StructOptimizer
	relaxer = StructOptimizer()
	result = relaxer.relax(pmg_struc)
	print('initial structure relaxation ended')
	#print("CHGNet relaxed structure", result["final_structure"])
	pmg_struc=result["final_structure"]

chg_phon=chgnet_phonopy(pmg_struc, path='.', supercell_dims=[int(args.supercell_dims[0]), int(args.supercell_dims[1]),int(args.supercell_dims[2])])
chg_phon.save_to_pickle()

#with open('chgnet_data.pkl', 'rb') as inp:
#	chgnet_obj= pickle.load(inp)

chg_phon.mesh_bands()
chg_phon.get_phonon_fc2(
			displacement=args.disp, 
			num_snapshots=args.num_rand_disp, 
			write_fc=True, 
			output_POSCARs=args.output_disp, 
			pretrained_model=args.pretrained_model, 
			trained_path=args.model_path,
			)

# the code only supports the units "THz" and "cm-1". If you enter another unit like eV or Ry, the unit will go back to "THz"
chg_phon.get_phonon_dos_bs(
			line_density=40, 
			units='THz', 
			output_ph_band=args.output_ph_band, 
			stability_threshold=args.stability_criteria, 
			phonopy_bands_dos_figname='phonopy_bands_dos.png', 
			dpi=200,
			)
