# import libraries 
import numpy as np

# 1D Normal Distribution
def normal_dist_1D(x_array, mean, std):
    return 1/(std*np.sqrt(2*pi))*np.exp(-(x_array-mean)**2/(2*std**2))

