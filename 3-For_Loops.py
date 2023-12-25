# First glance #

for i in "istanbul":
    print(i)
# i , s , t, a, n ,b ,u ,l (this output one under the other)
##########################

sports = ["volleyball", "basketball", "archery", "car racing"]

for i in sports:
    print(i)
# volleyball, basketball, archery, car racing (this output one under the other)

for i in sports:
    print(i.capitalize())
# Volleyball, Basketball, Archery, Car racing (this output one under the other)

# for loops in function #

listo = [100, 200, 400, 800, 1600]

for i in listo:
    print(i)
# 100, 200, 400, 800, 1600

for i in listo:
    print(i * 20 / 100)
# 20.0, 40.0, 80.0, 160.0, 320.0

for i in listo:
    if i < 300:
        print(int(i + i * 30 / 100))
    elif 300 < i < 800:
        print(int(i + i * 25 / 100))
    else:
        print(int(i + i * 20 / 100))
    # 130, 260, 500, 960, 1920


############################################
def change(n):
    for i in listo:
        if i < 300:
            print(int(i + i * n / 100))
        elif 300 < i < 800:
            print(int(i + i * (n - 5) / 100))
        else:
            print(int(i + i * (n - 10) / 100))


change(30)  # 130, 260, 500, 960, 1920
change(50)  # 150, 300, 580, 1120, 2240
change(100)  # 200, 400, 780, 1520, 3040

# function in for loops #

listo = [100, 200, 400, 800, 1600]


def change2(m, n):
    return int(m + m * n / 100)


for m in listo:
    if m < 300:
        print(change2(m, 30))
    elif 300 < m < 800:
        print(change2(m, 25))
    else:
        print(change2(m, 20))
# 130, 260, 500, 960, 1920

# The break Statement #

listo = [100, 200, 400, 800, 1600]

for i in listo:
    print(i)
    if i == 400:
        break
# 100, 200, 400

# The continue Statement #

for i in listo:
    if i == 400:
        continue
    print(i)
# 100, 200, 800, 1600

# Enumerate #

customers = ["Trevor", "Karissa", "Enzo", "Moria", "Bianca"]

for i, j in enumerate(customers):
    print(i, j)
# 0 Trevor,1 Karissa, 2 Enzo, 3 Moria, 4 Bianca

for i, j in enumerate(customers):
    if i % 2 == 0:
        print("even indexes " + j)
    else:
        print("odd indexes " + j)

"""even indexes Trevor
odd indexes Karissa
even indexes Enzo
odd indexes Moria
even indexes Bianca"""

####################################
customers = ["Trevor", "Karissa", "Enzo", "Moria", "Bianca"]
list_even = []
list_odd = []

for i, j in enumerate(customers):
    if i % 2 == 0:
        list_even.append(j)
    else:
        list_odd.append(j)
print(list_even)
print(list_odd)

# ['Trevor', 'Enzo', 'Bianca']
# ['Karissa', 'Moria']

###################################

hi = "my name is bora and i am three years old."
new_hi = ""

for i, j in enumerate(hi):
    if i % 2 != 0:
        new_hi += j.upper()
    else:
        new_hi += j.lower()
print(new_hi)
# mY NaMe iS BoRa aNd i aM ThReE YeArS OlD.mY NaMe iS BoRa aNd i aM ThReE YeArS OlD.
