'''
Pysolation course project #1
27th of May 2020
Tonya White, Vera Bouwman, Louk de Mol, Elisabet Blok
'''

import nibabel as nib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from nibabel.freesurfer.mghformat import load



#######################
##### Hard coded ######
#######################

#ORDER
#1.V Read in IDC paths
#2.V Check how large output arrays should be
#3. Make output data arrays
#4. Array for LH thickness cases and array LH thickness controls (similar for all following outputs)
#5. Make loop to cycle through all vertices 
#6. Run paired ttest
#7. Write output 
#8. Go to next morph
#9. Apply multiple testing (and figure out how!) --> check with Sander

#Loop order
#1. Length of morph
#2. Cycle through vertices
#Why this way? To circumvent having to load the data every time

#Data on IDC with in the first column the ASD cases and in the second column the matched controls
input_idcs = "/home/eblok/data/Pysolation/IDC_case_control_2cols.csv"

#Load imaging data
path1 = "/data/mounts/scs-fs-20/kpsy/genr/mrdata/rbraid/xnat/nii/GenR_F9_MRI/freesurfer/v6.0.0/"
path2 = "/surf/"
#These are our outcomes
morph = ["lh.thickness.fwhm10.fsaverage.mgh", "rh.thickness.fwhm10.fsaverage.mgh", "lh.area.pial.fwhm10.fsaverage.mgh", "rh.area.pial.fwhm10.fsaverage.mgh", "lh.pial_lgi.fwhm5.fsaverage.mgh", "rh.pial_lgi.fwhm5.fsaverage.mgh"]
morph_add = "_ASD_ttest"


#output path
out_path = '/home/eblok/data/Pysolation/ASD_ttest/'

###########################################################

idclist = np.genfromtxt(input_idcs, delimiter = ',', dtype = np.str)

idc1 = path1 + idclist[0,0] + path2 + morph[0]
test = load(idc1)
data_t = test.get_fdata()

len_idc = len(idclist)
len_morph = len(morph)
len_vert = len(data_t)


for a in range(len_morph):
    print(morph[a])
    data_t = np.zeros([len_vert,1,1])
    data_p = np.zeros([len_vert,1,1])
    data_cases = np.zeros([len_idc, len_vert])
    data_controls = np.zeros([len_idc, len_vert])
    for b in range(len_idc):
        idc_cases = path1 + idclist[b,0] + path2 + morph[a]
        img_cases = load(idc_cases)
        img_cases_data = img_cases.get_fdata()
        data_cases[b,:] = img_cases_data[:,0,0]
        idc_controls = path1 + idclist[b,1] + path2 + morph[a]
        img_controls = load(idc_controls)
        img_controls_data = img_controls.get_fdata()
        data_controls[b,:] = img_controls_data[:,0,0]
    for c in range(len_vert):
        v0 = np.max(data_cases[:,c])
        v1 = np.max(data_controls[:,c])
        if (v0 > 0 and v1 > 0):
            t_out = stats.ttest_rel(data_cases[:,c], data_controls[:,c])
            v2 = t_out[0].astype(np.float32)
            v3 = t_out[1].astype(np.float32)
            data_t[c,0,0] = v2
            data_p[c,0,0] = 1 - v3
    output_ttest_t = nib.MGHImage(data_t.astype(np.float32), affine = None)
    nib.save(output_ttest_t, out_path + morph[a] + "out_t.mgh")
    output_ttest_p = nib.MGHImage(data_p.astype(np.float32), affine = None)
    nib.save(output_ttest_p, out_path + morph[a] + "out_p.mgh")