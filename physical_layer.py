import random
import numpy as np

def awgn_noise():
    return np.random.normal(0, 1)

def transmit_signal(base_delay, load):
    noise = abs(awgn_noise())
    delay = base_delay * load + noise
    return delay
