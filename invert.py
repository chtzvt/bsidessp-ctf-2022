import sys 

# Read two files as byte arrays
file1_b = bytearray(open(sys.argv[1], 'rb').read())


# Set the length to be the smaller one
size = len(file1_b)
xord_byte_array = bytearray(size)

for i, v in enumerate(xord_byte_array):
    xord_byte_array[i] = 0xFF & ~v

# Write the XORd bytes to the output file	
open(sys.argv[2], 'wb').write(xord_byte_array)
