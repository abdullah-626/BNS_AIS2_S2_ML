import numpy as np

def secure_reshape_and_stack(data1, data2, new_shape):
    """
    1. Validates and converts inputs to NumPy arrays.
    2. Reshapes the first dataset to a specific dimension.
    3. Vertically stacks both datasets into one matrix.
    """
    try:
        arr1 = np.array(data1)
        arr2 = np.array(data2)
        reshaped_arr1 = arr1.reshape(new_shape)
        combined_dataset = np.hstack(reshaped_arr1,arr2)
        return combined_dataset
    except ValueError as e:
        raise ValueError(f"Company-grade Error: {e}")

x = [1,2,3,4,5,6]
y = [[7,8,9],
     [10,11,12]]

print(secure_reshape_and_stack(x,y,(2,3)))