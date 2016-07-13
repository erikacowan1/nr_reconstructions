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

BF_SNR_array = []
for run in range(0, 12, 1):
	wildcard_bayes_factor = bayes_factor_pattern.format(run)
	wildcard_snr = snr_pattern.format(run)

	for filename in glob.glob(wildcard_bayes_factor):
		f = open(filename, 'r')
		for line in f:
			line = line.strip()
			columns = line.split()
			bayesfactor = float(columns[0])
		f.close()
		#print bayesfactor

	for filename in glob.glob(wildcard_snr):
		f = open(filename, 'r')
		H1, L1, network = f.readlines()	
		
		columns_H1 = H1.split()
		columns_L1 = L1.split()
		columns_network = network.split()

		H1_snr = float(columns_H1[1])
		L1_snr = float(columns_L1[1])
		network_snr = float(columns_network[1])
		
		ratio = H1_snr / L1_snr
		max_snr = max((ratio),(1/ratio))
	#print H1_snr, L1_snr, network_snr, ratio, max_snr


	BF_SNR_array(bayesfactor, H1_snr, L1_snr, network_snr, ratio, max_snr)

	print BF_SNR_array
