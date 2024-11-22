import numpy as np
import random

def decode(file_path, keys, max_bin_digit=16):

    with open(file_path, 'rb') as file:
        binary_values = file.read()
    code = ''.join(format(byte, '08b') for byte in binary_values)
    idx = np.arange(len(code))
    for key in keys:
        random.seed(key)
        random.shuffle(idx)
    ordered = ''.join(np.array(list(code))[np.argsort(np.array(idx))])

    with open(file_path.replace(".bin", "_decoded.txt"), 'w') as file:
        file.write(
            ''.join([chr(int(ordered[i*max_bin_digit:(i+1)*max_bin_digit], 2)) for i in range(len(ordered)//max_bin_digit)])
        )
    return

# Setup
code_file_path = ''
keys = []
decode(code_file_path, keys)