from typing import Optional, Tuple, List
from fire import Fire
from functools import cache

def day_8_first():
    antennas = dict()
    m = 0
    n = 0
    antinode = set()

    with open("day_8.data", "r") as file:
        for line in file:
            line = line.strip()
            n = len(line)
            for nn,char in enumerate(line):
                if char != ".":
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((m,nn))
            m+=1

    
    for type_a, locations in antennas.items():
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                loc = [locations[i], locations[j]]
                loc.sort(key=lambda x:x[0])
                m_diff = loc[1][0] - loc[0][0]
                n_diff = abs(loc[0][1] - loc[1][1])
                
                first_antinode_mm = loc[0][0] - m_diff
                second_antinode_mm = loc[1][0] + m_diff

                if loc[0][1] >= loc[1][1]:
                    #increasing
                    first_antinode_nn = loc[0][1] + n_diff
                    second_antinode_nn = loc[1][1] - n_diff
                else:
                    first_antinode_nn = loc[0][1] - n_diff
                    second_antinode_nn = loc[1][1] + n_diff
            
                if first_antinode_mm > -1 and first_antinode_mm < m and \
                    first_antinode_nn > -1 and first_antinode_nn < n:
                   antinode.add((first_antinode_mm, first_antinode_nn))

                if second_antinode_mm > -1  and second_antinode_mm < m and \
                    second_antinode_nn > -1 and second_antinode_nn < n:
                   antinode.add((second_antinode_mm, second_antinode_nn))
    
    print(sorted(antinode,key=lambda x:x[0]))
    return len(antinode)


def day_8_second():
    ans = 0

    def rec(operands, index):
        if index == 0:
            return [int(operands[0])]
        
        next = rec(operands, index-1)
        
        new_next = []
        for nn in next:
            new_next.append(nn*int(operands[index]))
            new_next.append(nn+int(operands[index]))
            new_next.append(int(str(nn)+operands[index]))
        
        return new_next

    with open("day_8.data", "r") as file:
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




if __name__ == "__main__":
    Fire()

