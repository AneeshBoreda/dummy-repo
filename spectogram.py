# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:27:35 2019

@author: jiink
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

def spectogram(audio):
    
    sampling_rate = 44100
    S, freqs, times = mlab.specgram(audio, NFFT=4096, Fs=sampling_rate,
                                window=mlab.window_hanning,
                                noverlap=int(4096 / 2))
    np.clip(S, 10**-20, None)
    return np.log(S)

    """
    function returns an array of values for the spectogram
    
    Parameters 
    ----------------------------------------------------------------------
    audio: [np array]
        array of numbers containing information about audio
    
    Returns
    ----------------------------------------------------------------------
    np.log(S): [np array]
        the clipped and logged version of the array that represents values
        of the spectogram"""
        