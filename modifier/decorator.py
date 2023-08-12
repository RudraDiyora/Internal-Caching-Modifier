import modifiers

@modifiers.timed
@modifiers.internal_cache
def a(x):
    n=0
    for i in range(x):
        n += 1
    return n
print(a(3000)) 
print(a(3000))