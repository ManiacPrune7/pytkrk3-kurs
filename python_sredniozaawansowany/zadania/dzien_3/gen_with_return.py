"""
    jak dziala generator ze slowem kluczowym return wewnatrz
"""


def ret():
    for i in range(5):
        if i == 3:
            return
        else:
            yield i


for x in ret():
    print(x)

print("druga petla:")

for x in ret():
    print(x)

gen1 = ret()
gen2 = ret()

print(list(gen1))
print(list(gen2))
