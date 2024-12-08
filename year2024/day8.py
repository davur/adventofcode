debug = False

from utils import dprint, warn, char_grid_from_lines
from collections import defaultdict
from pprint import pprint
import copy


def solution(sections):

    result1 = result2 = 0

    grid = char_grid_from_lines(sections[0])

    frequency_antennas = {}

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            frequency = grid[r][c]
            if frequency != '.':
                if frequency not in frequency_antennas:
                    frequency_antennas[frequency] = []
                frequency_antennas[frequency].append((r, c))


    antinodes = {}
    antinodes_p2 = {}

    for frequency in frequency_antennas:
        antennas = frequency_antennas[frequency]

        for i in range(len(antennas)):
            for j in range(i+1, len(antennas)):
                if i == j:
                    continue

                pos_i = antennas[i]  # 1, 8
                pos_j = antennas[j]  # 2, 5

                                     # 1, -3
                diff = (pos_j[0] - pos_i[0], pos_j[1] - pos_i[1])

                # j + diff

                # P1
                antinode_a = (pos_j[0] + diff[0], pos_j[1] + diff[1])
                antinode_b = (pos_i[0] - diff[0], pos_i[1] - diff[1])
                if in_bounds(antinode_a, grid):
                    antinodes[antinode_a] = True
                if in_bounds(antinode_b, grid):
                    antinodes[antinode_b] = True

                # P2
                antinodes_p2[pos_i] = True
                antinodes_p2[pos_j] = True

                while in_bounds(antinode_a, grid):
                    antinodes_p2[antinode_a] = True
                    antinode_a = (antinode_a[0] + diff[0], antinode_a[1] + diff[1])

                while in_bounds(antinode_b, grid):
                    antinodes_p2[antinode_b] = True
                    antinode_b = (antinode_b[0] - diff[0], antinode_b[1] - diff[1])

    result1 = len(antinodes)
    result2 = len(antinodes_p2)

    return (result1, result2)


def in_bounds(pos, grid):
    r, c = pos
    row_count = len(grid)
    col_count = len(grid[0])

    if not (0 <= r < row_count and 0 <= c < col_count):
        return False
    return True

