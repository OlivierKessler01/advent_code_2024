from typing import Optional, Tuple, List
from fire import Fire
from functools import cache

def day_7_first():
    ans = 0

    def rec(operands, index):
        if index == 0:
            return [int(operands[0])]
        
        next = rec(operands, index-1)
        
        new_next = []
        for nn in next:
            new_next.append(nn*int(operands[index]))
            new_next.append(nn+int(operands[index]))
        
        return new_next

    with open("day_7.data", "r") as file:
        for line in file:
            line = line.strip()
            split = line.split(":")
            test_value = int(split[0])
            operands = split[1]
            operands = tuple(operands.split(" ")[1:])
            results = rec(operands, len(operands)-1)
            if test_value in results:
                  ans+=test_value

    return ans


    



def day_7_second():
    ans = 0 
    grid = []
    direction =0 
    curr = [0,0]
    visited = set()

    with open("day_7.data", "r") as file:
        for line in file:
            line = list(line.strip())
            grid.append(line)
            
            for nn, char in enumerate(line):
                if char == "^":
                    curr = [len(grid) -1, nn]
                    break

    m = len(grid)
    n = len(grid[0])






if __name__ == "__main__":
    Fire()

