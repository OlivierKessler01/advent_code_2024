from fire import Fire

def day_5_first():
    need = {}
    updates = []

    with open("day_5.data", "r") as file:
        for line in file:
            if "|" in line:
                line_s = line.strip().split("|")
                if line_s[1] not in need:
                    need[line_s[1]] = set()
                need[line_s[1]].add(line_s[0])
            elif line.strip() == "":
                continue
            else:
                updates.append(line.strip().split(","))
     
    
    ans = 0

    for update in updates:
        valid = True
        seen = set() 
        update_s = set(update)

        for page in update:
            if page in seen:
                continue

            if page in need: 
                if len(need[page].intersection(update_s).difference(seen)) > 0:
                    valid = False
                    break
        
            seen.add(page)

        if valid:
            ans+=int(update[len(update)//2])
    
    return ans

def day_5_second():
    need = {}
    updates = []
    incorrect_updates = []

    with open("day_5.data", "r") as file:
        for line in file:
            if "|" in line:
                line_s = line.strip().split("|")
                if line_s[1] not in need:
                    need[line_s[1]] = set()
                need[line_s[1]].add(line_s[0])
            elif line.strip() == "":
                continue
            else:
                updates.append(line.strip().split(","))
     
    
    ans = 0

    for update in updates:
        valid = True
        seen = set() 
        update_s = set(update)


        for page in update:
            if page in seen:
                continue

            if page in need: 
                if len(need[page].intersection(update_s).difference(seen)) > 0:
                    valid = False
                    break
        
            seen.add(page)

        if not valid:
            incorrect_updates.append(update)

    
    for update in incorrect_updates:
        queue = update
        sorted = []
        seen = set()
        update_s = set(update)

        while len(queue) > 0:
            page = queue.pop(0)
            if len(need[page].intersection(update_s).difference(seen)) != 0:
                queue.append(page)
            else:
                sorted.append(page)
                seen.add(page)


        ans+=int(sorted[len(sorted)//2])
    
    return ans


if __name__ == "__main__":
    Fire()
