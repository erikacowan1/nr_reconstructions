#program that plots BayesFactor vs. max(SNR) and BayesFactor vs. total SNR

import numpy as np
import os, sys
import argparse
import glob

#command line parsing
parser = argparse.ArgumentParser(
	description= 'BF_vs_SNR.py is a program that plots the Bayes Factor versus max(SNR) and network SNR')
parser.add_argument('base_dir', type=str, help='Please enter directory where /posterior_samples and /engine directories are located')
args = parser.parse_args()

bayes_factor_pattern = os.path.join(args.base_dir, 'posterior_samples','posterior_H1L1_*-{}.dat_B.txt')
snr_pattern = os.path.join(args.base_dir, 'engine', 'lalinferencenest-{}-*.dat_snr.txt')


for run in range(0, 12, 1):
	wildcard_bayes_factor = bayes_factor_pattern.format(run)
	wildcard_snr = snr_pattern.format(run)

#	for filename in glob.glob(wildcard_snr)
#		ratio = H1_snr / L1_snr
#                max_SNR = max((ratio),(1/ratio))
	bayesfactor = 0
	for filename in glob.glob(wildcard_bayes_factor):
		f = open(filename, 'r')
		for line in f:
			line = line.strip()
			columns = line.split()
			bayesfactor = columns[0]
		f.close()

	print bayesfactor
