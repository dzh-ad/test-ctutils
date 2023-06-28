import chardet

# open the file and read it using the 'rb' (read binary) mode
with open('/Users/amelia/Documents/GitHub/test-ctutils/0_test/test-chardet-vgl copy.txt', 'rb') as f:
    binary_data = f.read()

# detect the encoding
detected = chardet.detect(binary_data)
encoding = detected['encoding']

print('The detected encoding is ' + encoding)

# decode the data using the detected encoding
decoded_data = binary_data.decode(encoding)

print ('The decoded message is:')
print(decoded_data)