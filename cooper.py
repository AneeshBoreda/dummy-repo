# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def sumlogs(array):
    ''' This function finds the sum of the logs of the values in an array.
    It also takes the absolute value to ignore logs of negatives
    
    Parameters
    ---------
    array: numpy array, shape = (M,)
    
    
    Returns
    -------
    The sum of all logs, floating point number
    '''
    
    return np.sum(np.log(np.abs(array)))