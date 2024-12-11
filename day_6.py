from typing import Optional, Tuple
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


def day_6_second():
    ans = 0 
    grid = []
    direction =0 
    curr = [0,0]
    visited = set()

    with open("day_6.data", "r") as file:
        for line in file:
            line = list(line.strip())
            grid.append(line)
            
            for nn, char in enumerate(line):
                if char == "^":
                    curr = [len(grid) -1, nn]
                    break

    m = len(grid)
    n = len(grid[0])

    for mm in range(m):
        for nn in range(n):
            if [mm, nn] == curr:
                continue

            prev_val = grid[mm][nn]
            grid[mm][nn]="#"
            
            current = list(curr)
            visited = set() 
            direction = 0
            
            while True:
                if current[0] == -1  or current[1] == -1 or current[0] > m-1 or current[1] > n-1:
                    break
                elif grid[current[0]][current[1]] == "#":
                    if direction == 0:
                        current[0]+=1
                    elif direction == 1:
                        current[1]-=1
                    elif direction == 2:
                        current[0]-=1
                    else:
                        current[1]+=1

                    direction+=1
                    direction%=4
                elif (current[0], current[1],direction) not in visited:
                    visited.add((current[0], current[1],direction))
                else:
                    ans+=1
                    break

                if direction == 0:
                    current[0]-=1
                elif direction == 1:
                    current[1]+=1
                elif direction == 2:
                    current[0]+=1
                else:
                    current[1]-=1


            grid[mm][nn]=prev_val

    return ans





if __name__ == "__main__":
    Fire()

