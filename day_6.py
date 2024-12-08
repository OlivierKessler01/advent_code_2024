from typing import Tuple
from fire import Fire

def day_6_first():
    ans = 1 
    grid = []
    direction =0 
    current = (None,None)
    visited = set()

    with open("day_6.data", "r") as file:
        for line in file:
            line = list(line.strip())
            grid.append(line)

            for nn, char in enumerate(line):
                if char == "^":
                    direction = 0
                    current = (len(grid) -1, nn)
                    break

    m = len(grid)
    n = len(grid[0])

    
    def search(current, direction) -> Tuple[int, Tuple[int,int]]:
        distance_to_block = 0
        
        if direction == 0:
            for i in range(current[0]-1, -2, -1):
                if i == -1 or grid[i][current[1]] == "#":
                    return distance_to_block, (i+1, current[1])
                elif (i, current[1]) not in visited:
                    distance_to_block+=1
                    visited.add((i, current[1]))
        elif direction == 1:
            for i in range(current[1]+1, n+1):
                if i == n or grid[current[0]][i] == "#":
                    return distance_to_block, (current[0], i-1)
                elif (current[0], i) not in visited:
                    distance_to_block+=1
                    visited.add((current[0], i))
        elif direction == 2:
            for i in range(current[0]+1, m+1):
                if i == m or grid[i][current[1]] == "#":
                    return distance_to_block, (i-1, current[1])
                elif (i, current[1]) not in visited:
                    distance_to_block+=1
                    visited.add((i, current[1]))
        elif direction == 3:
            for i in range(current[1]-1, -2, -1):
                if i == -1 or grid[current[0]][i] == "#":
                    return distance_to_block, (current[0], i+1)
                elif (current[0], i) not in visited:
                    distance_to_block+=1
                    visited.add((current[0], i))

        return 0, (0,0)

    while True:
        distance_to_block, current = search(current, direction)
        direction+=1
        direction%=4
        ans+=distance_to_block
        
        print(current)
        if current[0] in [0, m-1] or current[1] in [0, n-1] :
            return ans





if __name__ == "__main__":
    Fire()

