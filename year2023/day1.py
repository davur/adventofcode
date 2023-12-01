debug = False

from .utils import *
from collections import defaultdict
from pprint import pprint
import copy


def solution(file):

    # print(f'{file=}')

    result1 = result2 = 0

    sections = read(file)
    lines = sections[0]
    # print(lines)

    result1 = 0

    for line in lines:
      # print(f'{line=}')
      l = 0
      r = 0
      for i in range(len(line)):
        c = line[i]
        # print(f'{c=}')
        if c in '0123456789':
          l = c
          break
        if c

      for i in range(len(line)-1, -1, -1):
        c = line[i]
        if c in '0123456789':
          r = c
          break

      val = int(f'{l}{r}')
      print(f'{val=}')

      result1 += val

    result2 = 0

    return (result1, result2)
