import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import numpy as np
import histogram_library as his

def mean_hist(even_mat,odd_mat,slices,hist_mat,subject,image):
    
    for i in range(0,np.array(slices).size):
        i = i+i
        j = i+1
        #print i,j
        even_mat = np.vstack((hist_mat[:,i],even_mat))
        odd_mat = np.vstack((hist_mat[:,j],odd_mat))
        
    even_mat = even_mat.T
    even_mat = even_mat[:,:-1]
    
    odd_mat = odd_mat.T
    odd_mat = odd_mat[:,:-1]
    
    gm_mean = np.mean(even_mat[1:,:].astype('float'),axis=1)
    wm_mean = np.mean(odd_mat[1:,:].astype('float'),axis=1)
    
    name='\\mat_mean_gm'
    his.save_dir(subject,name,gm_mean, fig='no')
    name='\\mat_mean_wm'
    his.save_dir(subject,name,wm_mean, fig='no')
    name='\\mat_wm'
    his.save_dir(subject,name,odd_mat, fig='no')
    name='\\mat_gm'
    his.save_dir(subject,name,even_mat, fig='no')
    
    if image == 'yes':
            
        fig = plt.figure()  
        line1, = plt.plot(wm_mean.astype('float'), color='blue', label='WM Histogram')
        line2, = plt.plot(gm_mean.astype('float'), color='red', label='GM Histogram')
        plt.grid(True, color = "#a6a6a6", linestyle='dotted')
        plt.legend(handler_map={line1: HandlerLine2D(numpoints=3)})
        plt.title(str(subject[1:])+' mean')
        
        name='\\mat_mean_gm'
        his.save_dir(subject,name,gm_mean, fig='no')
        name='\\mean'
        his.save_dir(subject,name,wm_mean,fig='yes')
            
        plt.savefig('C:\Users\FarivarLabPC\OneDrive - McGill University\Research\Study\Python\Brain_Analysis\histogram_library\\files\\'+'mean_'+str(subject[1:])+'.png',dpi=600, transparent=True, bbox_inches='tight')

    else: 
        pass
    
