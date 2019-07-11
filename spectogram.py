# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:27:35 2019

@author: jiink
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

def spectogram(audio_address):
    
    with open(audio_address, 'r') as R:
        audio = np.asarray([int(i) for i in R])
    
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
    audio_address: [string]
        the name of the text file in which the audio's data is stored in
        the form of numbers
    
    Returns
    ----------------------------------------------------------------------
    np.log(S): [array]
        the clipped and logged version of the array that represents values
        of the spectogram"""
        