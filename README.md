#  Autism spectrum disorder multiple testing script
A Python script to walkthrough in isolation

## Data specification
(Draft of assumed data specifications)

The expected data format are files of:
- An MGH file containing the cortical thickness at each vertex of the left hemisphere for each subject
- An MGH file containing the cortical thickness at each vertex of the left hemisphere for each subject
- An MGH file containing the cortical area at each vertex of the left hemisphere for each subject
- An MGH file containing the cortical area at each vertex of the right hemisphere for each subject
- An MGH file containing the cortical local gyrification index at each vertex of the left hemisphere for each subject
- An MGH file containing the cortical local gyrification index at each vertex of the right hemisphere for each subject

The vertices are assumed to be accessible in the first dimension of the MGH file.

## Directory structure
(Draft of assumed directory structure):
```
-- absolute_data_path
|   -- IDC_0
|   -- IDC_1/
|   -- IDC_N-1/
|   -- IDC_N/
|   |   -- surf/
|   |   |   -- lh.thickness.fwhm10.fsaverage.mgh
|   |   |   -- rh.thickness.fwhm10.fsaverage.mgh
|   |   |   -- lh.area.pial.fwhm10.fsaverage.mgh
|   |   |   -- rh.area.pial.fwhm10.fsaverage.mgh
|   |   |   -- lh.pial_lgi.fwhm5.fsaverage.mgh
|   |   |   -- rh.pial_lgi.fwhm5.fsaverage.mgh
```
