import random

def encode(file_path, keys, max_bin_digit=16):

    with open(file_path, 'r') as file:
        text = file.read()

    bin_str = ''.join([bin(ord(c))[2:].zfill(max_bin_digit) for c in text])
    shuffled_bin = list(bin_str)
    for key in keys:
        random.seed(key)
        random.shuffle(shuffled_bin)

    binary_data = ''.join(shuffled_bin)
    binary_values = bytearray(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))
    with open(file_path.replace(".txt", "_encoded.bin"), 'wb') as file:
        file.write(binary_values)

    if (10 ** len(str(max(keys)))) ** len(keys) < 2**128:
        print("WARNING: Your password might not be safe.")
    print("WARNING: This is only a demo. It is NOT designed for protecting actual secrets.")
    return

# Setup
file_path = ''
keys = []  # Suggestion: use at least ten 4-digit decimal integer keys
encode(file_path, keys)