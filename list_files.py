import glob
import os

import pandas as pds

datasets = glob.glob('Z:/working/barryd/hpc/python/keras_image_class/Princeton_Data/*')
file_info = pds.DataFrame(data=None, columns=["File", "HPF", "Incubation Temperature"], dtype='float')

for dataset in datasets:
    temp = 28.5
    if dataset.find('Dataset_D') > 0:
        temp = 25.0
    hpfs = glob.glob(dataset + os.sep + '*')
    for hpf in hpfs:
        images = glob.glob(hpf + os.sep + '*.png')
        for image in images:
            row = pds.DataFrame(
                {'File': [
                    os.path.basename(dataset) + '/' + os.path.basename(hpf) + '/' + os.path.basename(image)],
                    'HPF': [os.path.basename(hpf)], 'Incubation Temperature': ["{:.1f}".format(temp)]})
            file_info = pds.concat([file_info, row])

file_info.to_csv('Z:/working/barryd/hpc/python/keras_image_class/Princeton_Data/file_list.tsv', sep='\t', index=False)
