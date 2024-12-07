from fire import Fire

def day_5_first():
    need = {}
    updates = []

    with open("day_5.data", "r") as file:
        for line in file:
            if "|" in line:
                line_s = line.strip().split("|")
                if line_s[1] not in need:
                    need[line_s[1]] = []
                need[line_s[1]].append(line_s[0])
            elif line.strip() == "":
                continue
            else:
                updates.append(line.strip().split(","))
     
    
    ans = 0

    for update in updates:
        valid = True
        seen = set() 

        for page in update:
            if valid is False:
                break

            if page in seen:
                continue

            if page in need: 
                for dependency in need[page]:
                    if dependency in update and dependency not in seen:
                        print(f"{page} {dependency} {seen}")
                        valid = False
                        break
        
            seen.add(page)

        if valid:
            ans+=int(update[len(update)//2])
    
    return ans

def day_5_second():

    return sum(mul[0] * mul[1] for mul in muls)


if __name__ == "__main__":
    Fire()
