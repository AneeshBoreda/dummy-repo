# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:37:26 2019

@author: jiink
"""

import numpy as np
from random import uniform

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def audio_random_samples(audio):
    
    audio = audio.tolist()
    t = np.linspace(0, len(audio) / 44.1 / 1000, 1000)
    start = audio[find_nearest(audio, uniform(0, t[-1] - 4406))] 
    # 4406 is 10(seconds) / delta_t
    stop = audio[audio.index(start) + 4406]
    
    
    
    #start = uniform(0, t[-1] - 10)
    #stop = find_nearest(audio, start + 10)
    
    audio_sample = audio[audio.index(start):audio.index(stop)]
    
    return np.asarray(audio_sample)
    
    """
    this function produces a 10 second sample of the audio at a random point
    in time
    
    Parameters
    --------------------------------------------------------------------------
    audio: [np array]
        array containing the numbers that represent the audio file
    
    Returns
    --------------------------------------------------------------------------
    audio_sample: [np array]
        array containing the numbers that represent a random 10-second 
        interval of the audio file"""