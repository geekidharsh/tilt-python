import os
import csv

with open("testdatin.txt") as fin, open("testdataout.txt") as fout:
	o=csv.writer(fout)
	for line in fin:
		o.writerow(",".join(map(str, line)))
