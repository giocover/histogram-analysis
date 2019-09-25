# histogram-analysis

This algorithm generates cortical gray matter and white matter histograms. As inputs, it takes an MRI T1-weighted image, cortical white and gray matter segmentations from Freesurfer and computes histograms for every slice, outputting a single averaged histogram. The user has to select the folder where files are and also where it should save all results. The input folder needs the T1-weighted image to be analyzed and the following Freesurfer files:

* brain.mgz
* lh.ribbon.mgz
* rh.ribbon.mgz
* wm.mgz
* wm.seg.mgz
![Test Image 4](https://github.com/tograh/testrepository/3DTest.png)
