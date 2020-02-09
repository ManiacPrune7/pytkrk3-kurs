"""
    rysowanie choinki
"""


def draw_tree(n, offset=0):
    if n == 0:
        return
    else:
        draw_tree(n-1, offset+1)
    print(offset*" " + "*"*(2*n-1))

draw_tree(5)