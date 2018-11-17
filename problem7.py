# Leet Code 451. Sort Characters by Frequency
# -------------------------------
# Given a string, sort it in decreasing order based on the frequency of characters.

def sort_decreasing_order(str):
    dict = {}
    for s in str:
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
    
    sorted_dict = sorted(dict, key=dict.get, reverse=True)

    word = ''

    for s in sorted_dict:
        word += s * dict[s]

    return word


print(sort_decreasing_order('bbAa'))


        
        
