import struct
import argparse

#parser = argparse.ArgumentParser(description='Convert fp32 to bfloat16 Example')
#parser.add_argument('floats', type=float, metavar='F', nargs='+', help='input float numbers')
#args = parser.parse_args()
                   
bin_num = []
bin_num1 = []
num_array = []
#num_array=args.floats[0]

num_array = 56.090896, 8.138961, 5.709567
div_array = []
diff_array = []

def binary(num):
    return(''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num)))

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def Average(lst):
    return sum(lst) / len(lst)

for num in num_array:
   print("Input FP32 num: ", num)
   bin_num = binary(num)
   #print("Input num in binary:  ", bin_num)
   
   bin_num1 = '0000000000000000'
   #print("Input BF16 in binary: ", bin_num[0:16]+bin_num1)
   num_BF16 = bin_to_float(bin_num[0:16]+bin_num1)
   print("Output BF16 num:", num_BF16)
   
   diff_array.append(num - num_BF16)
   #print("FP32 - BF16 : ", num - num_BF16)
   #div_array.append(num / num_BF16)
   #print("FP32 / BF16 : ", num / num_BF16)
   
   print("---------------------------------\n")


print("*******************************")
print("FP32 - BF16 : ", diff_array)

# Printing average of the list
average = Average(diff_array)
print("Average of the list : ", round(average, 9))

result = [item + average for item in num_array]
print("new numbers : ", result)
print("*******************************\n")

bin_num = []
bin_num1 = []

for num in result:
   print("Input FP32 num: ", num)
   bin_num = binary(num)
   #print("Input num in binary:  ", bin_num)
   
   bin_num1 = '0000000000000000'
   #print("Input BF16 in binary: ", bin_num[0:16]+bin_num1)
   num_BF16 = bin_to_float(bin_num[0:16]+bin_num1)
   print("Output BF16 num:", num_BF16)
   
   #diff_array.append(num - num_BF16)
   #print("FP32 - BF16 : ", num - num_BF16)
   #div_array.append(num / num_BF16)
   #print("FP32 / BF16 : ", num / num_BF16)
   
   print("---------------------------------\n")