import os 
from tqdm import tqdm

from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout
	
configs = ['8bits', '9bits', '10bits', '11bits', '12bits']
runs = ['One', 'Two', 'Three']


for i in tqdm(configs):
	for j in runs:
		configDir = 'configs/' + i + '/' + i + j + '.yaml'

		currTrainCall = 'python train.py -d -c ' + configDir
		currTestCall = 'python test.py -d -c ' + configDir
		with suppress_stdout():
			os.system(currTrainCall)
			os.system(currTestCall)			

print('completed')	
