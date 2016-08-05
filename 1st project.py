""" ---------------- """
""" Ohm Namashivaya  """
""" ---------------- """

import array
arr=[]
inp = open ("sum.txt","r")
for line in inp.readlines():
        numbers = map(int, line.split())
	arr.append(numbers)
line = arr[0:3]
line2 = line[0]
sum = line2[0] + line2[1]
print sum

