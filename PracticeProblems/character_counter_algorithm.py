# Run via : python -m character_counter_algorithm

## == INPUTS ======================================
test_str = "Today I ran to the beach."
# =================================================

# set-up counter 
ii = 0

# remove spaces
test_str = test_str.replace(" ","")
print(f"{ii} {test_str}") ; ii += 1

# strip whitespace at end of str
test_str = test_str.strip()
print(f"{ii} {test_str}") ; ii += 1

# set the entire string to lower case
test_str = test_str.lower()

# sort the string; a list is return
test_str_list = sorted(test_str)
print(f"{ii} {test_str_list}") ; ii += 1
# -- key=str.lower tells not to prioritize capital letters above lower case
#test_str_list = sorted(test_str,key=str.lower)

# conver the list to a string
test_str = "".join(test_str_list)
print(f"{ii} {test_str}") ; ii += 1

# keep only letters
test_str_p = test_str
del test_str
test_str = ""
for char in test_str_p:
    if char.isalpha():
        test_str += char

# define the ouput string
str_out_list = []
prev_char = None
new_char_flag = True
unq_char_counter = -1 # start at -1 so first one becomes 0
for char in test_str:
    if prev_char == char:
        char_count_ii += 1
        str_out_list[-2] = char_count_ii
    else:
        char_count_ii = 1
        unq_char_counter += 1
        str_out_list.append(char_count_ii) 
        str_out_list.append(char)

    prev_char = char
    print(f"{ii} {str_out_list}") ; ii += 1

    #if new_char is True:
    #    char_count_ii = 1
    #    char_counter=char_counter+1
    #else:
    #    char_count_ii += 1

str_out = str(str_out_list)
print(f"{ii} {str_out}") ; ii += 1
print(f"str_out is {type(str_out)} and has value {str_out}")


