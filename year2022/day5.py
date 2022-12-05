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
        lines = file.readlines()

    stack_height = 0
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            stack_height = i - 1
            break

    # print(stack_height)

    stacks1 = []
    stacks2 = []
    marker_line = lines[stack_height]
    # print(marker_line)
    num_stacks = len(marker_line.split())

    # for stack in stacks:
        #print(stack)

    #[D] [D] [T] [F] [G] [B] [B] [H] [Z]
    #0123456789012345678
    # 1   5   9   1   1
    #             3   7

    for j in range(num_stacks):
        stacks1.append([])
        stacks2.append([])

    for i in range(stack_height-1, -1, -1):
        line = lines[i].rstrip()
        # print(line)
        for j in range(num_stacks):
            if len(line)>j*4+1:
                c = line[j*4+1]
                if c != ' ':
                    stacks1[j].append(c)
                    stacks2[j].append(c)
    
    for i in range(stack_height + 2, len(lines)):
        line = lines[i].strip()
        _, quantity, _, fro, _, to = line.split()
        quantity, fro, to = ints([quantity, fro, to])
        # print(quantity, fro, to)

        # Part 1
        for j in range(quantity):
            crate = stacks1[fro-1].pop()
            stacks1[to-1].append(crate)

        # Part 2
        for j in range(quantity):
            crate = stacks2[fro-1][0 - quantity + j]
            stacks2[to-1].append(crate)
        for j in range(quantity):
            stacks2[fro-1].pop()

    #for stack in stacks:
        #print(stack)


    tops1 = []
    for i in range(num_stacks):
        if stacks1[i]:
            tops1.append(stacks1[i][-1])
    result1 = ''.join(tops1)

    tops2 = []
    for i in range(num_stacks):
        if stacks2[i]:
            tops2.append(stacks2[i][-1])
    result2 = ''.join(tops2)

    return (result1, result2)

