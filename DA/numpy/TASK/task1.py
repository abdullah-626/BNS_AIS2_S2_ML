import numpy as np

def array_factory(mode = None, shape = (0,0), value=None):
    """
    Creates various NumPy arrays based on the mode.
    - 'zeros': Array filled with 0.
    - 'ones': Array filled with 1.
    - 'full': Array filled with a specified 'value'.
    - 'identity': A square identity matrix of size 'shape'.
    """
    mods = ['zeros', 'ones', 'full', 'identity']
    if mode in mods :
        if mode == 'zeros':
            return np.zeros(shape)
        elif mode == 'ones':
            return np.ones(shape)
        elif mode == 'full':
            return np.full(shape,value)
        else:
            return np.identity(shape)
    else:
        return "invalid mod"

print(array_factory())