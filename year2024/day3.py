debug = False

from utils import dprint, warn
from collections import defaultdict
from pprint import pprint
import copy
import re

pattern = '(do\\(\\))|(don\'t\\(\\))|(mul\\(\\d{1,3},\\d{1,3}\\))'

def solution(sections):

    result1 = result2 = 0

    lines = sections[0]

    enabled = True

    for line in lines:
        matches = re.findall(pattern, line)

        for match in matches:
            if match[0]:
                enabled = True
            elif match[1]:
                enabled = False
            else:
                numbers = match[2][4:-1]
                a, b = numbers.split(',')
                a, b = int(a), int(b)
                res = a * b
                result1 += res
                if enabled:
                    result2 += res

    return (result1, result2)
