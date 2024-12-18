import re
from functools import reduce

pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
num_pattern = r'\d{1,3}'

with open('input.txt', 'r') as f:
    data = f.read()
    print(data)
    matches = re.findall(pattern, data)
    res = 0
    doCompute = True
    for match in matches:
        print(match)
        if match.startswith('don'):
            doCompute = False
            print("Disabled")
        elif match.startswith('do'):
            doCompute = True
            print("Enabled")
        else:
            if doCompute:
                nums = re.findall(num_pattern, match)
                res += reduce(lambda x, y: int(x) * int(y), nums)
    print(res)

