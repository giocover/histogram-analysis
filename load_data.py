#%%Importing Libraries
import nibabel as ni
import numpy as np
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
import histogram_library as his

def load_data(slice,subject,nu,image):
    
    #path = 'C:\Users\FarivarLabPC\OneDrive - McGill University\Virtual_Machine\MEMPRAGE-Dehydration\cedar_dehyd_study\\analysis\\filter\\filter'
    path = 'C:\Users\FarivarLabPC\OneDrive - McGill University\Virtual_Machine\MEMPRAGE-Dehydration\cedar_dehyd_study\\analysis\\filter\\filter\\meanimage'
    
    #--------- Paths --------------------
    nu_path = str(path)+str(nu)
    brain_path = str(path)+'\\brain.mgz'
    wm_path = str(path)+'\\wm.mgz'
    wmseg_path = str(path)+'\\wm.seg.mgz'
    lh_ribbon_path = str(path)+'\\lh.ribbon.mgz'
    rh_ribbon_path = str(path)+'\\rh.ribbon.mgz'
    
    #--------- Load iamges --------------------
    nu = ni.load(nu_path).get_data()
    nu = nu[:,:,slice]
    nu = np.rot90(nu,3) 
    
    brain = ni.load(brain_path).get_data()
    brain = brain[:,:,slice]
    brain = np.rot90(brain,3) 
    
    lh_ribbon = ni.load(lh_ribbon_path).get_data()
    lh_ribbon = lh_ribbon[:,:,slice]
    lh_ribbon = np.rot90(lh_ribbon,3) 
    
    rh_ribbon = ni.load(rh_ribbon_path).get_data()
    rh_ribbon = rh_ribbon[:,:,slice]
    rh_ribbon = np.rot90(rh_ribbon,3) 
    
    wm = ni.load(wm_path).get_data()
    wm = wm[:,:,slice]
    wm = np.rot90(wm,3) 
    
    wmseg = ni.load(wmseg_path).get_data()
    wmseg = wmseg[:,:,slice]
    wmseg = np.rot90(wmseg,3) 
    
    wm = wm*np.array(wmseg)
    
    #--------- create masks --------------------
    gm = lh_ribbon+rh_ribbon
    gm_mask_nu = nu*np.array(gm)
    
    mask = np.ma.masked_array(wm <= 1, wm)
    mask = ndi.morphology.binary_closing(wm).astype(np.int) #eroding mask
                
    wm_mask_nu = nu*np.array(mask)
    
    if image == 'yes':  
        
        fig = plt.figure()            
        plt.subplot(131)
        plt.imshow(nu, cmap='gray')
        plt.axis("off")
        plt.subplot(132)
        plt.imshow(gm_mask_nu, cmap='gray')
        plt.title(str(subject[1:])+' slice '+str(slice)) 
        plt.axis("off")
        plt.subplot(133)
        plt.imshow(wm_mask_nu, cmap='gray')
        plt.axis("off")
        
        name='\\slice_'+str(slice)
        his.save_dir(subject,name,wm_mask_nu, fig='yes')
        
    else:
        pass    
        
    return wm_mask_nu, gm_mask_nu