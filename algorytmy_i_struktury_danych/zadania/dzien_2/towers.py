"""
    algorytm sprawdzajacy czy wiezyczki moga byc przeskoczone
"""


def is_hoppable(towers: list) -> bool:
    if towers[0] >= len(towers):
        return True
    for i in range(towers[0]):
        hop = i + 1
        if is_hoppable(towers[hop:]):
            return True
    return False

print(is_hoppable([4,2,0,2,0]))