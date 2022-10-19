import numpy as ps
a = ps.random.randint(1,20,15)
print("array:")
print(a)
a.resize((3,5))
print(a)
print(a.shape)
for i in a:
    i[ps.where(i==i.max())] = 0
print("maximum value replaced by 0:")
print(a)