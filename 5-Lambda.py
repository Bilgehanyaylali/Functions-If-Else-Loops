# Zip #

names = ["Bilgehan", "Penelope", "Auberta", "Craig"]
cities = ["Ankara", "Atina", " Berlin", "London"]
countries = ["Turkiye", "Greece", "Germany", "England"]
list(zip(names, cities, countries))
# [('Bilgehan', 'Ankara', 'Turkiye'), ('Penelope', 'Atina', 'Greece'),
# ('Auberta', ' Berlin', 'Germany'), ('Craig', 'London', 'England')]

# lambda #

hi = "I am Bilge"
up = lambda string: string.upper()
print(up(hi))
# I AM BILGE

##################################
a = lambda x: x ** x

a(4)  # 256

numbers = [2000, 2500, 3000, 3500, 4000]

list(map(lambda x: x + x * 20 / 100, numbers))
# [2400.0, 3000.0, 3600.0, 4200.0, 4800.0]

tuple(map(lambda x: x + x * 20 / 100, numbers))
# (2400.0, 3000.0, 3600.0, 4200.0, 4800.0)

set(map(lambda x: x + x * 20 / 100, numbers))
# {2400.0, 4800.0, 4200.0, 3600.0, 3000.0}

