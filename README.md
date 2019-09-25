# histogram-analysis

This algorithm generates cortical gray matter and white matter histograms. As inputs, it takes a MRI T1-weighted image, cortical white and gray matter segmentations from Freesurfer and compute histograms for every slice and outputs a single averaged histogram. First the user has to select the folder where the files are and also where it should save all results. The input folder needs the following Freesurfer files:

brain.mgz\\
lh.ribbon.mgz
rh.ribbon.mgz
wm.mgz
wm.seg.mgz
