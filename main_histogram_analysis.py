# ----------------------------------------- Libraries --------------------------------------------- #
import numpy as np
import histogram_library as his

#subjects = ['tp2tomean1to6','tp2tomean1to6_filt','tp4tomean1to6','tp4tomean1to6_filt','tp5tomean1to6','tp5tomean1to6_filt','tp6tomean1to6','tp6tomean1to6_filt']

subjects = ['meanimage_filt','meanimage_nofilt']
            
for i,j in enumerate(subjects):

    # -------------------------------------- Defined Variables ---------------------------------------- #
    #subject = '\meanimage_filt.nii'
    #nu = '\\meanimage_filt.nii'
    
    subject = '\\'+str(j)+'.nii'
    nu = '\\'+str(j)+'.nii'
    
    slices = range(94,372)
    #slices = range(94,97)
    
    # -------------------------------------- Global Variables ----------------------------------------- #
    hist_mat = np.zeros((20))
    even_mat = np.zeros((20))
    odd_mat = np.zeros((20))
    
    # ---------------------------------------- Main Script -------------------------------------------- #
    for slice in slices:
        
        # ---------------- loading WM and GM files -------------------- #
        wm, gm = his.load_data(slice, subject = str(subject), nu = str(nu), image='yes')
        # ----------------------------- calculating histogram ---------------------------------- #
        hist_mat = his.hist_calc(wm, gm, 20, slice, hist_mat, subject = str(subject), image='yes')
    
    # - correcting matrix -- #    
    hist_mat = hist_mat.T
    hist_mat = hist_mat[:,:-1]
    
    # ----------------------------------- creating right folder according to subjectec --------------------------------------------------------- #
    name='\\mat_hist'
    his.save_dir(subject,name,hist_mat,fig='no')
    
    # -------- calculating mean histogram for all slices ------------- #
    his.mean_hist(even_mat,odd_mat,slices,hist_mat,subject,image='yes')
