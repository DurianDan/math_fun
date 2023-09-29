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
from typing import List

def category_scheme_name(schemes: List[str]) -> List[str]:

    # sort the name => sub-categories are always after the bigger categories
    schemes.sort()

    # get the full scheme from categories' name suffix
    for idx in range(len(schemes)-1):
        
        name = schemes[idx]
        after_idx = idx+1

        # loop stops, if the next category doesn't
        #  starts with the now-category "name"  
        while after_idx<len(schemes) and schemes[after_idx].startswith(name):
            # turn string to list, to modify
            array_char = list( schemes[after_idx] )

            # change "-" to ">"
            array_char[ len(name) ] = ">"
            
            # rejoin characters
            schemes[after_idx] = "".join(array_char)
            
            # increment after_idx => to access the next category
            after_idx+=1

    return schemes

if __name__=="__main__":
    case = [
        "food",
        "food-ice-cream",
        "food-ice-cream-vanilla",
        "food-grilled-steak",
        "southest-asia",
        "southest-asia-vietnam",
        "southest-asia-vietnam-dak-lak"
    ]

    edge_case_1 = case + [
        "food-ice-cream-chocolate-proccessed",
        "food-ice-cream-chocolate-raw",
    ]

    edge_case_2 = edge_case_1 + ["food-ice-cream-chocolate"]

    print("+ Categories naming schemes of `case`:\n" + str(category_scheme_name(case)))
    print("+ Categories naming schemes of `edge_case_1`:\n" + str(category_scheme_name(edge_case_1)))
    print("+ Categories naming schemes of `edge_case_2`:\n" + str(category_scheme_name(edge_case_2)))