#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
from copy import copy


# In[26]:


def convert_to_complex_binary(number):
    """
    Converts integer to complex binary representation.
    
    Args:
        number: int: Number to convert.
    
    Returns:
        tuple: (Based, Based-4, Normalized, Binary String) 
    """
    
    rev_list=list()
    based_list=list(np.base_repr(number, base=4, padding=0))
    r1 = copy(based_list)

    j = 0
    for i in reversed(based_list):
        if(j%2==0):
            rev_list.append(int(i))
        else:
            rev_list.append(-int(i))
        j=j+1

    rev_list = rev_list[::-1]
    r2 = copy(rev_list)

    normalized = list()
    overflow = False
    for i in range(1, rev_list.__len__() + 1):
        control = rev_list[-i]
        if control < 0:
            added = control + 4
            try:
                rev_list[-i-1] += 1
            except IndexError:
                overflow = True
        else:
            added = control
        normalized.append(added)

        if overflow:
            normalized.append(1)

    normalized = normalized[::-1]

    for i in range(normalized.__len__()):
        # May occur an underflow.
        if normalized[i] == 4:
            normalized[i] = 0
            normalized[i-1] -= 1
            normalized[i-1] = normalized[i-1]%4 
    
    r3 = copy(normalized)

    base_dict = {0: "0000", 1: "0001", 2: "1100", 3: "1101"}
    
    base_string = str()
    for num in normalized:
        base_string += f"{base_dict[num]} "
    
    r4 = copy(base_string)
    return r1, r2, r3, r4


# In[27]:


# Change this number 
number = 2005
based, based4, normalized, bin_str = convert_to_complex_binary(number)

print("Number to Convert: ", number)
print("Based Str: ", based_list)
print("Based -4: ", based4)
print("Normalized: ", normalized)
print("Binary String: ", bin_str)


# In[ ]:




