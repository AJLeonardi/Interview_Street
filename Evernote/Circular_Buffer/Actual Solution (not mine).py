def parse_action(str):
    if str.startswith("R"):
        n = int(str[1:])
        remove_items(n)
    elif str.startswith("L"):
        print_buffer();
    elif str.startswith("Q"):
        raise SystemExit

def remove_items(n):
    del buffer[0:n]

def print_buffer():
    for val in buffer:
        print val

buffer = []
add = 0
n = int(raw_input())
while (1):
    line = raw_input()

    if len(buffer) > n:
        del buffer[0]

    if add > 0:
        add -= 1
        buffer.append(line)

    elif line.startswith("A"):
        add = int(line[1:])

    else:
        parse_action(line)