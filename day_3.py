from enum import Enum
from fire import Fire


class State(Enum):
    START = 1
    M = 2
    U = 3
    L =4 
    FIRST =5 
    SECOND = 6

d = {
    State.START: {"m": State.M},
    State.M: {"u": State.U},
    State.U: {"l": State.L},
    State.L: {"(": State.FIRST},
    State.FIRST: {
        ",": State.SECOND,
        "0": State.FIRST,
        "1": State.FIRST,
        "2": State.FIRST,
        "3": State.FIRST,
        "4": State.FIRST,
        "5": State.FIRST,
        "6": State.FIRST,
        "7": State.FIRST,
        "8": State.FIRST,
        "9": State.FIRST,
    },
    State.SECOND: {
        ")": State.START,
        "0": State.SECOND,
        "1": State.SECOND,
        "2": State.SECOND,
        "3": State.SECOND,
        "4": State.SECOND,
        "5": State.SECOND,
        "6": State.SECOND,
        "7": State.SECOND,
        "8": State.SECOND,
        "9": State.SECOND,
    },
}


def day_3_first():
    muls = []

    with open("day_3.data", "r+") as file:
        content = file.read()

    current_state = State.START
    acc_1 = ""
    acc_2 = ""

    for char in content:
        if char in d[current_state]:
            if char == ")":
                muls.append((int(acc_1), int(acc_2)))
                acc_1 = ""
                acc_2 = ""
            elif char in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if current_state == State.FIRST:
                    acc_1 += char
                else:
                    acc_2 += char

            current_state = d[current_state][char]
        else:
            acc_1 = ""
            acc_2 = ""
            current_state = State.START

    return sum(mul[0] * mul[1] for mul in muls)


if __name__ == "__main__":
    Fire()
