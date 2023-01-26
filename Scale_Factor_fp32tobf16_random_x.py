import struct
import argparse
import random
                   
bin_num = []
bin_num1 = []
num_array = []
div_array = []
bf16_old = []
bf16_new = []

for i in range(0, 32):
  num_array.append(random.uniform(0.5, 5675.5))
print('\nFP32 original :' , num_array)

def binary(num):
    return(''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num)))

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def Average(lst):
    return sum(lst) / len(lst)

for num in num_array:
   bin_num = binary(num)   
   bin_num1 = '0000000000000000'

   num_BF16 = bin_to_float(bin_num[0:16]+bin_num1)
   bf16_old.append(num_BF16)   
   div_array.append(num / num_BF16)

print("\nBF16 original : ", bf16_old)
print("\nFP32 / BF16 : ", div_array)

random_num = random.choice(div_array)
print("\nRandom num : " + str(random_num))

#Pass BF16 original
#result = [item * random_num for item in bf16_old]
#print("\nNew number - Randon num x BF16 original : ", result, '\n')

#Pass FP32 original
result = [item * random_num for item in num_array]
print("\nRandon num x FP32 original : ", result, '\n')

for num in result:
   bin_num = binary(num)   
   bin_num1 = '0000000000000000'

   num_BF16 = bin_to_float(bin_num[0:16]+bin_num1)
   bf16_new.append(num_BF16)

print("Output BF16 num:", bf16_new)

