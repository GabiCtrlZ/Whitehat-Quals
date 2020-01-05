import netcat as nc
import re

def k_squared_sum(num):
  return int(((num)*(num + 1)*((num * 2) + 1)) / 6)

def k_plus_one_sum(num):
  return int(k_squared_sum(num) + ((num * (num+1))/2)) 

def num_of_triangles(num):
    if (num % 2) == 0:
        k = (num / 2) - 1
        return k_plus_one_sum(k - 1) + k_squared_sum(k)
    else:
        k = ((num - 1) / 2) - 1
        return k_plus_one_sum(k) + k_squared_sum(k)


connection = nc.Netcat()
connection.start(b'15.164.75.32', 1999)

first = b''
while not first == b'Great ! the last challenge. ':
    first = connection.read()
    second = connection.read()
    triangle_in_range = int(re.search(r'\d+', second.decode('utf-8')).group())
    answer = num_of_triangles(triangle_in_range)
    a = f'{int(answer)}\n'.encode()
    print(second)
    print(triangle_in_range)
    print(a)
    connection.write(a)
first = connection.read()
print(first)

