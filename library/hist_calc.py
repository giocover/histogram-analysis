import cv2
import ia636 as ia
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import numpy as np
import histogram_library as his

def hist_calc(wm,gm,bins,slice,hist_mat,subject,image):
    
    if image == 'yes':
        
        hist_wm = cv2.calcHist([ia.ianormalize(wm.astype('float32'))],[0],None,[bins],[0,256])
        hist_gm = cv2.calcHist([ia.ianormalize(gm.astype('float32'))],[0],None,[bins],[0,256])
        
        tags = ['wm_slice_'+str(slice),'gm_slice_'+str(slice)]
    
        hist_mat_0 = np.hstack((tags[0],hist_wm[1:,0]))
        hist_mat_1 = np.hstack((tags[1],hist_gm[1:,0]))
        
        fig = plt.figure()  
        line1, = plt.plot(hist_mat_0[1:].astype('float'), color='blue', label='WM Histogram')
        line2, = plt.plot(hist_mat_1[1:].astype('float'), color='red', label='GM Histogram')
        plt.grid(True, color = "#a6a6a6", linestyle='dotted')
        plt.legend(handler_map={line1: HandlerLine2D(numpoints=3)})
        plt.title('slice '+str(slice))
        
        name='\\hist_slice_'+str(slice)
        
        his.save_dir(subject,name,hist_mat_0,fig='yes')
        
        hist_mat = np.vstack((hist_mat_0,hist_mat))
        hist_mat = np.vstack((hist_mat_1,hist_mat))
    else:
        
        hist_wm = cv2.calcHist([ia.ianormalize(wm.astype('float32'))],[0],None,[bins],[0,256])
        hist_gm = cv2.calcHist([ia.ianormalize(gm.astype('float32'))],[0],None,[bins],[0,256])
        
        tags = ['wm_slice_'+str(slice),'gm_slice_'+str(slice)]
    
        hist_mat_0 = np.hstack((tags[0],hist_wm[1:,0]))
        hist_mat_1 = np.hstack((tags[1],hist_gm[1:,0]))
        
        hist_mat = np.vstack((hist_mat_0,hist_mat))
        hist_mat = np.vstack((hist_mat_1,hist_mat))
        
    return hist_mat
