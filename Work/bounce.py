# bounce.py
#
# Exercise 1.5
def bounce(x, h):
    count, ht = x, h
    while count > 0:
        ht *= (3/5)
        print(round(ht, 4))
        count -= 1


bounce(10, 100.0)
