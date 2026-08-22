import numpy as np

def apply_threshold(arr, threshold, replacement_value=-1):
    """
    Finds elements satisfying a condition (>= threshold) 
    and replaces them with a new value.
    """
    arr = np.array(arr)
    condition = arr >= threshold
    modified_arr = np.where(condition, replacement_value, arr)
    return modified_arr