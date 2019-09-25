import os
import numpy as np
import matplotlib.pyplot as plt

def save_dir(subject,name,variable,fig):
    folder = 'C:\Users\FarivarLabPC\OneDrive - McGill University\Research\Study\Python\Brain_Analysis\histogram_library\\files\\'+str(subject[1:])
    
    try:
        os.makedirs(folder)
    except:
        pass
    
    if fig == 'yes':
        plt.savefig('C:\Users\FarivarLabPC\OneDrive - McGill University\Research\Study\Python\Brain_Analysis\histogram_library\\files\\'+str(subject[1:])+str(name)+'.png', dpi=600, transparent=True, bbox_inches='tight')
    else:
        np.save('C:\Users\FarivarLabPC\OneDrive - McGill University\Research\Study\Python\Brain_Analysis\histogram_library\\files\\'+str(subject[1:])+str(name),variable)
 
