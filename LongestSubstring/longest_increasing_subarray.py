"""
Get longest subarray that is strictly increasing
return the longest subarray
if multiple are present, return any


---
should ask how to handle None

"""

# Solution 1: Brute Froce
# - Loop over indices, ii
# ---- if index ii > index ii+1
# ------ if index ii+1 > index ii+2
# ---------- if index ii+2 > index ii+3
# ---------- ... recruse
# ---- if index ii !> index ii+1
# ------  store overall length in substr_length_arr



# Solution 2: Keep informaiton of previous subarray to advance
# - Define start at index 0
# - if index 0 > index 1
# --- if index 1 > index 2
# ------- if index 2 > index 3
# ---------- ... recruse
# - if index 0 !> index 1
# ---  store overall length in substr_length_arr
# - Move to index 1
# ---- if index 1 > index X # here, index X is the index that the
#                           # previous substring ended at. we do 
#                           # not ned to repeat the > evaluation again. 
#                           


# Solution 3: Solution 2 with better None handling


# == CREATE BASE ARRAY =========================================
arr = [5, 9, 8, 8, 7, 1, -2, None, 8, 0.2, 1, 2, 4, 5, 6, 8, 12, 2, 5, 6, 12]

# Solution 1
verbose_flag = True
len_arr = len(arr)
substr_len = []
for idx_arr, arr_ii in enumerate(arr):
    if arr_ii is None:
        substr_len.append(None)
        continue    
    arr_curr = arr_ii
    for count_ss, idx_ss in enumerate(range(idx_arr+1,len_arr)): 
        arr_ff = arr[idx_ss]
        if arr_ff is None:
            substr_len.append(count_ss+1)
            break 
        if not arr_curr < arr_ff:
            substr_len.append(count_ss+1)
            if verbose_flag:
                print(f"arr_curr is not < arr_ff, idx_arr is {idx_arr}: \
                      arr_ii is {arr_ii}, arr_curr is {arr_curr}, arr_ff is {arr_ff}, \
                      count_ss is {count_ss}, idx_ss is {idx_ss}")   
            break
        else:
            arr_curr = arr_ff
            if verbose_flag:
                 print(f"arr_curr is < arr_ff, idx_arr is {idx_arr}: \
                      arr_ii is {arr_ii}, arr_curr is {arr_curr}, arr_ff is {arr_ff}, \
                      count_ss is {count_ss}, idx_ss is {idx_ss}")  

print(f"length of the array is {substr_len}")


