#convert input Arff files to TAB format that is accepted by Orange ML
from scipy.io.arff import loadarff
import scipy as sp
import os
import csv
 
rel_path = "3001_All_Data_Arff.arff"
rel_path_csv = "3001_All_Data_BSP.tab"
abs_file_path = os.path.join(rel_path)
dataset = loadarff(open(abs_file_path,'r'))
 
abs_file_path_csv = os.path.join(rel_path_csv)
f=open(abs_file_path_csv, 'wb');
writer = csv.writer(f,delimiter="\t")
 
#write attribute header
for i in dataset[1]:
    f.write(i)
    f.write('\t')
f.write('\n')
 
#write datatype header
for i in dataset[1]:
    if i== 'condition':
        f.write('d')
    else:
        f.write('c')
    f.write('\t')
f.write('\n')

#write class header
for i in dataset[1]:
    if i== 'condition':
        f.write('class')
    else:
        f.write(' ')
    f.write('\t')
f.write('\n')
   
 
 
writer.writerows(dataset[0])
f.close()
