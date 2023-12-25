# First glance #

i = 1
while i <= 10:
    print(i)
    i += 1  # 1,2,3,4,5,6,7,8,9,10

# The Break Statement #

j = 1
while j < 9:
    print(j)
    if j == 5:
        break
    j += 2  # 1, 3, 5

# The Continue Statement #

k = -1
while k < 9:
    k += 2
    if k == 5:
        continue
    print(k)  # 1,3, 7, 9

# Else #

m = 1
while m < 5:
    print(m)
    m += 1
else:
    print("the end")  # 1, 2, 3, 4, the end

    
