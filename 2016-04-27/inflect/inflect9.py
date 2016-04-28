import inflect
p = inflect.engine()

for n in range(3):
    print(p.inflect("num({0},)There plural(is) number_to_words({0}) plural(person) who plural(eats) pie.".format(n)))

# There are zero people who eat pie.
# There is one person who eats pie.
# There are two people who eat pie.
