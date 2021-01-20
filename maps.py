'Learning about how to represent maps/areas/and places in code'

char = 'O'
start_pos = [0, 0]
area = [
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
]

def place_char(char:str=char, cord:list=start_pos, map:list=area) -> None:
    # map = [
    # ['x', 'x', 'x', 'x', 'x'],
    # ['x', 'x', 'x', 'x', 'x'],
    # ['x', 'x', 'x', 'x', 'x'],
    # ['x', 'x', 'x', 'x', 'x'],
    # ['x', 'x', 'x', 'x', 'x'],
    # ]
    map[cord[0]][cord[1]] = char
    # area = map    

def print_map(map:list=area) -> None:
    for row in map:
        print(" ".join(row))

place_char(cord=[0, 2])
print_map()