import re
from functools import reduce

pattern = r'mul\(\d{1,3},\d{1,3}\)'
num_pattern = r'\d{1,3}'

with open('input.txt', 'r') as f:
    data = f.read()
    print(data)
    matches = re.findall(pattern, data)
    res = 0
    for match in matches:
        nums = re.findall(num_pattern, match)
        res += reduce(lambda x, y: int(x) * int(y), nums)
    print(res)

