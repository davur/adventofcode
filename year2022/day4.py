debug = False

def dprint(*args):
    if debug:
        print(*args)
    

def ints(nums):
    return [int(num) for num in nums]

def solution(file):

    result1 = 0
    result2 = 0

    lines = []
    with open(file, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            lines.append(line)

    for line in lines:
        first, second = line.split(',')
        first1, first2 = ints(first.split('-'))
        second1, second2 = ints(second.split('-'))

        first_set = set(range(first1, first2+1))
        second_set = set(range(second1, second2+1))

        overlap = first_set & second_set

        dprint(overlap)

        # part 1 if first contains second, or second contains first
        if overlap == first_set or overlap == second_set:
            result1 += 1

        # part 2 if there is any overlap
        if overlap: 
            result2 += 1

    return (result1, result2)
