'''
Input: List of categories' names, each categories' name...
    contains words, seperated by hyphen "-",
    and can be the suffix of other categories' name, indicates sub-category
    E.g.: [
        food,
        food-ice-cream,
        food-grilled-steak,
        food-ice-cream-vanilla,
        southest-asia,
        southest-asia-vietnam,
        southest-asia-vietnam-dak-lak
    ]

Output: words in a categories' name, seperated by hyphen "-",
    and sub-categories, seperated by greater sign ">"
    E.g.: [
        food,
        food>ice-cream,
        food>grilled-steak,
        food>ice-cream>vanilla,
        southest-asia,
        southest-asia>vietnam,
        southest-asia>vietnam>dak-lak
    ]
'''

'''
Solution:
time: O(n!)
space: O(1)
'''

cate_scheme_name = [
        "food",
        "food-ice-cream",
        "food-grilled-steak",
        "food-ice-cream-vanilla",
        "southest-asia",
        "southest-asia-vietnam",
        "southest-asia-vietnam-dak-lak"
    ]

# sort the name => sub-categories are always after the bigger categories
cate_scheme_name.sort()

# get the full scheme from categories' name suffix
for idx in range(len(cate_scheme_name)-1):
    
    name = cate_scheme_name[idx]
    after_idx = idx+1

    # loop stops, if the next category doesn't
    #  starts with the now-category "name"  
    while after_idx<len(cate_scheme_name) and cate_scheme_name[after_idx].startswith(name):
        # turn string to list, to modify
        array_char = list( cate_scheme_name[after_idx] )

        # change "-" to ">"
        array_char[ len(name) ] = ">"
        
        # rejoin characters
        cate_scheme_name[after_idx] = "".join(array_char)
        
        # increment after_idx => to access the next category
        after_idx+=1

print(cate_scheme_name)