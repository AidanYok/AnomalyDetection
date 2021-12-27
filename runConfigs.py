import os 
from tqdm import tqdm

configs = ['8bits', '9bits', '10bits', '11bits', '12bits']
runs = ['One', 'Two', 'Three']


for i in tqdm(configs):
	for j in runs:
			configDir = 'configs/' + i + '/' + i + j + '.yaml'
		 
			currTrainCall = 'python train.py -d -c ' + configDir
			currTestCall = 'python test.py -d -c ' + configDir
			os.system(currTrainCall)
			os.system(currTestCall)			

print('completed')	