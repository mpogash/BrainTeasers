
import numpy as np
from distributions import normal_dist_1D

mean_val = 23.8
std_val = 3
noise_level = 0.1
x_array = np.arange(-100,100)

dist_normal_noise = noise_level*np.random.rand(len(x_array))
dist_normal = normal_dist_1D(x_array, [mean_val, std_val]) + dist_normal_noise

# FIXME: Automate the initial guess
init_guess = [23, 4]
fit_normal = least_squares(min_fun_normal, init_guess, args=(x_array,dist_normal))

dist_normal_mean = fit_normal.x[0]
dist_normal_std = fit_normal.x[1]
print(f"normal distribution mean and standard deviation are {dist_normal_mean} , {dist_normal_std}")